import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.join(os.path.dirname(__file__), 'Agents'))

import streamlit as st

# Import your agent functions
from Agents.cultural_guide import get_cultural_guide
from Agents.weather_safety_agent import get_weather_and_safety
from Agents.itinerary_planner import generate_clean_itinerary
from Agents.itinerary_planner import plan_itinerary
from Agents.budget_manager import get_budget_estimate
from Agents.experience_narrator import generate_narrative



st.set_page_config(page_title="World Explorer", layout="wide")
st.title("🌍 World Explorer - AI Travel Advisor")

# Step 1: User Preferences
st.header("Step 1: Select Your Preferences")
prefs = []
if st.checkbox("Nature"):
    prefs.append("nature")
if st.checkbox("Food"):
    prefs.append("food")
if st.checkbox("History"):
    prefs.append("history")
budget = st.slider("Budget (PKR)", 5000, 100000, 20000)

if st.button("Find Destinations"):
    # TODO: Replace with your Destination Scout agent
    # For now, use a static list
    st.session_state['destinations'] = ["Lahore", "Islamabad", "Swat", "Karachi"]

# Step 2: Destination Selection
if 'destinations' in st.session_state:
    st.header("Step 2: Choose Your Destination")
    dest = st.selectbox("Select a destination", st.session_state['destinations'])
    days = st.number_input("Trip Duration (days)", 1, 30, 5)
    user_budget = st.number_input("Your Budget (PKR)", 5000, 100000, 20000)
    if st.button("Plan My Trip"):
        st.session_state['selected'] = (dest, days, user_budget)

# Step 3: Show Agent Outputs
if 'selected' in st.session_state:
    dest, days, user_budget = st.session_state['selected']
    st.header("Your AI-Powered Travel Plan")

    # Itinerary
    st.subheader("Itinerary")
    itinerary = plan_itinerary(dest, days)
    st.write(itinerary)


    # Budget
    st.subheader("Budget Estimate")
    budget_info = get_budget_estimate(dest, "medium", days)
    st.write(budget_info)

    # Weather
    st.subheader("Weather & Safety")
    weather = get_weather_and_safety(dest)
    st.write(weather)

    # Culture
    st.subheader("Cultural Guide")
    culture = get_cultural_guide(dest)
    st.write( culture)
    

    # Immersive Narrative
    # Immersive Narrative
    st.subheader("Experience Narrator")

    if itinerary:
        narrative = generate_narrative(dest, itinerary)
        st.markdown(narrative)
    else:
        st.write("No itinerary available for immersive narrative.")


    # (Optional) Image Generation
    # st.subheader("AI-Generated Images")
    # st.image(...)