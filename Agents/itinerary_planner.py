import re
import os
from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv

load_dotenv()

# System prompt
prompt = """
You are a helpful travel assistant. Your task is to take raw travel information about a city (scraped from Wikivoyage or similar websites) and convert it into a short, well-structured, and readable itinerary format.

Instructions:
- Only generate a 3-day itinerary.
- Use concise and simple language.
- Divide the plan clearly by Day 1, Day 2, and Day 3.
- Highlight must-see attractions, cultural sites, food recommendations, and tips if available.
- Do not add information not provided in the raw input.
- Keep the tone friendly and informative.

Now, please generate a 3-day travel itinerary based on the following information:
"""

# Clean LLM response from extra assistant-like lines
def clean_response(text):
    text = re.sub(r"(?i)^.*?(i am|i'm|here (is|'s)).*?\n+", "", text)
    return text.strip()

# Generate clean itinerary from raw data
def generate_clean_itinerary(raw_data):
    agent = Agent(
        model=Groq(id="llama3-70b-8192"),
        markdown=True,
        stream=True,
        system_message=prompt
    )

    stream = agent.run(raw_data)
    response = ""
    for chunk in stream:
        response += chunk.content

    return clean_response(response)

# Main function frontend calls
def plan_itinerary(destination, days):
    # Placeholder for future scraped data
    raw_data = f"{destination} is a well-known travel destination. Here is information for a {days}-day visit. Popular sites include heritage buildings, food streets, museums, and cultural landmarks."
    return generate_clean_itinerary(raw_data)

# Test via terminal
if __name__ == "__main__":
    city = input("Enter your destination city: ")
    days = int(input("How many days is your trip? (for future use): "))
    raw_data = f"{city} is a cultural hub in Pakistan known for its Mughal architecture, vibrant food scene, and historical landmarks like Badshahi Mosque and Lahore Fort."

    print("\n🗺️ Wikivoyage-based itinerary:\n")
    plan = generate_clean_itinerary(raw_data)
    print(plan)
