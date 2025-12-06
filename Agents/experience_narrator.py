from dotenv import load_dotenv
import os
from agno.agent import Agent
from agno.models.groq import Groq

# Load environment variables (e.g., GROQ_API_KEY)
load_dotenv()

def generate_narrative(destination, itinerary, user_name="Traveler"):
    """
    Generate an immersive day-in-the-life travel story using Groq LLM.
    """
    # Format the itinerary for the prompt
    if isinstance(itinerary, list):
        itinerary_str = "\n".join([f"Day {i + 1}: {item}" for i, item in enumerate(itinerary)])
    else:
        itinerary_str = str(itinerary)

    prompt = f"""
**Experience Narrator Agent** – Immersive Travel Story

You are a creative AI travel narrator. Your job is to take the following destination and itinerary,
and write a vivid, immersive, second-person narrative as if the user ({user_name}) is experiencing the trip.
Make it engaging, sensory, and full of local color. Use present tense. Add small cultural or emotional details.

Destination: {destination}
Itinerary:
{itinerary_str}

Write a story for the user’s journey, day by day, as if they are living it.
"""

    agent = Agent(
        model=Groq(id="llama3-70b-8192"),  # Change to another model ID if desired
        markdown=True,
        stream=True,
        system_message=prompt
    )

    stream = agent.run("")

    response = ""
    for chunk in stream:
        response += chunk.content


    return response


if __name__ == "__main__":
    destination = input("Enter your destination: ")
    itinerary = [
        "Arrive and explore the old city bazaar.",
        "Visit the grand mosque and try local street food.",
        "Take a day trip to the mountains and enjoy scenic views."
    ]
    print("\n🧳 Generating your immersive travel story...\n")
    print(generate_narrative(destination, itinerary))
