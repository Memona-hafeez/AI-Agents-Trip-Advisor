import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from  Agents.budget_manager import get_budget_estimate

load_dotenv()

# ===== User Inputs =====
destination = "Islamabad"
accommodation_level = "medium"
duration_days = 3
user_budget = 5000

# ===== Logic Output =====
result = get_budget_estimate(destination, accommodation_level, duration_days)

# ===== Format Agent Response =====
if isinstance(result, dict):
    estimated_total = result["Estimated Total Cost"]
    within_budget = estimated_total <= user_budget
    summary = f"""
**Budget Manager Agent Report**

📍 Destination: {result['Destination']}
🏨 Accommodation: {result['Accommodation Total']} PKR
🍽 Meals: {result['Meals Total']} PKR
🚌 Transport: {result['Transport']} PKR
🧮 Estimated Total: {estimated_total} PKR

💰 User Budget: {user_budget} PKR
{"✅ Within Budget" if within_budget else "❌ Over Budget"}
"""
else:
    summary = result

# ===== Agent Response =====
agent = Agent(
    model=Groq(id="qwen-qwq-32b"),
    tools=[DuckDuckGoTools()],
    markdown=True,
    stream=True,
    system_message=f"""
You are a **Budget Manager AI Agent** for Pakistan trips.

Trip Details:
- Destination: {destination}
- Accommodation: {accommodation_level}
- Duration: {duration_days} days
- Budget: {user_budget} PKR

Provide:
1. Estimated cost breakdown
2. Comparison with budget
3. Suggest alternatives if over budget

Use the logic and summary provided below.

{summary}
"""
)

print(agent.print_response())
