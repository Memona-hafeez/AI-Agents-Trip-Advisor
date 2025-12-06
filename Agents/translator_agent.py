from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Load model and tokenizer once (this may take time the first time)
model_name = "facebook/nllb-200-distilled-600M"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Language codes for NLLB
lang_codes = {
    "english": "eng_Latn",
    "urdu": "urd_Arab",
    "punjabi": "pan_Guru",
    # Add more as needed
}

def translate(text, src_lang, tgt_lang):
    src_code = lang_codes.get(src_lang.lower())
    tgt_code = lang_codes.get(tgt_lang.lower())
    if not src_code or not tgt_code:
        return "❌ Language not supported."
    inputs = tokenizer(text, return_tensors="pt")
    translated_tokens = model.generate(
        **inputs,
        forced_bos_token_id=tokenizer.lang_code_to_id[tgt_code]
    )
    return tokenizer.decode(translated_tokens[0], skip_special_tokens=True)

# Simple phrasebook for demo
phrasebook = {
    "hello": {"urdu": "سلام", "punjabi": "ਸਤ ਸ੍ਰੀ ਅਕਾਲ"},
    "thank you": {"urdu": "شکریہ", "punjabi": "ਧੰਨਵਾਦ"},
    "how much?": {"urdu": "کتنے کا ہے؟", "punjabi": "ਕਿੰਨਾ ਹੋਇਆ?"},
    "where is the hotel?": {"urdu": "ہوٹل کہاں ہے؟", "punjabi": "ਹੋਟਲ ਕਿੱਥੇ ਹੈ?"},
}

def get_phrase(phrase, lang):
    return phrasebook.get(phrase.lower(), {}).get(lang.lower(), "Not available.")

if __name__ == "__main__":
    print("Sample Phrasebook:")
    for phrase in phrasebook:
        print(f"{phrase.title()} (Urdu): {phrasebook[phrase]['urdu']}")
        print(f"{phrase.title()} (Punjabi): {phrasebook[phrase]['punjabi']}")
        print()
    # Sample translation
    text = input("Enter text to translate: ")
    src = input("Source language (english/urdu/punjabi): ")
    tgt = input("Target language (english/urdu/punjabi): ")
    print("Translation:", translate(text, src, tgt)) 