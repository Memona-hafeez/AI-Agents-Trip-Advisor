from dotenv import load_dotenv
import os
import wikipedia
from agno.agent import Agent
from agno.models.groq import Groq


# Load environment variables (optional)
load_dotenv()

def get_cultural_summary(destination):
    try:
        search_term = f"Culture of {destination}"
        summary = wikipedia.summary(search_term, sentences=10)
        return summary
    except wikipedia.exceptions.PageError:
        return f"Sorry, no cultural page found for **{destination}**."
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Multiple results found for **{destination}**: {e.options[:5]}"
    except Exception as e:
        return f"An error occurred: {e}"

def get_cultural_guide(destination):
    raw_info = get_cultural_summary(destination)

    # If Wikipedia summary failed (already returns user-friendly message), skip LLM agent
    if raw_info.startswith("Sorry") or raw_info.startswith("An error"):
        return raw_info

    # LLM prompt
    prompt = f"""
*Cultural Guide Agent* – Travel Etiquette Helper

You are a helpful AI that provides cultural insights to travelers visiting {destination}.
Below is a brief overview extracted from Wikipedia. Based on it, summarize:

1. Cultural Norms  
2. Common Do's and Don’ts  
3. Etiquette tips  
4. Dress code or behavior that tourists should be aware of  

Keep the tone informative but friendly.

===
{raw_info}
"""

    # Create and run agent
    agent = Agent(
        model=Groq(id="llama3-70b-8192"),
        markdown=True,
        stream=True,
        system_message=prompt
    )

    stream = agent.run("")

    response = ""
    for chunk in stream:
        response += chunk.content

    return response

# CLI testing
if __name__ == "__main__":
    dest = input("Enter destination: ")
    print(get_cultural_guide(dest))
