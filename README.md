# 🧭 AI-Agents-Trip-Advisor

AI-Agents-Trip-Advisor is a smart multi-agent travel planning system that uses Artificial Intelligence to generate personalized travel plans.  
It allows users to enter trip details and automatically receives recommendations for destinations, hotels, attractions, activities, events, and weather conditions.

The project demonstrates how multiple autonomous AI agents can collaborate to solve a complex task such as trip planning.

---

## 📌 Problem Statement

Planning a trip manually requires searching multiple websites, comparing prices, checking weather, and creating itineraries.  
This project automates the entire process using AI agents that collect, analyze, and combine information into a single optimized travel plan.

---

## 🎯 Objectives

- Build an AI-based travel advisor  
- Implement multi-agent architecture  
- Provide personalized recommendations  
- Reduce manual research time  
- Demonstrate practical use of LLM-powered agents  

---

## 🚀 Features

- Multi-agent collaboration  
- Destination research agent  
- Hotel recommendation agent  
- Attraction & activity agent  
- Weather forecasting agent  
- Trip itinerary generation  
- User-friendly interface  
- Modular and extensible design  

---

## 🏗 Project Architecture

User → Frontend → Backend Controller → AI Agents → APIs → Response → Frontend

Agents communicate independently and send results to the controller which builds the final trip plan.

---

## 📁 Project Structure

AI-Agents-Trip-Advisor/
├── Agents/  
│   ├── destination_agent.py  
│   ├── hotel_agent.py  
│   ├── activity_agent.py  
│   ├── weather_agent.py  
│   └── planner_agent.py  
│
├── Backend/  
│   ├── app.py  
│   └── routes.py  
│
├── Frontend/  
│   ├── src/  
│   └── package.json  
│
├── Tools/  
├── requirements.txt  
├── Tour-Plan-Purposal.pdf  
├── README.md  
└── LICENSE  

---

## 🛠 Technology Stack

- Python  
- OpenAI API  
- LangChain / Agent Framework  
- Flask / FastAPI  
- React.js / Streamlit  
- External APIs (Weather, Search, Travel)

---

## ⚙ Installation

### Step 1: Clone Repository

git clone https://github.com/Memona-hafeez/AI-Agents-Trip-Advisor.git  
cd AI-Agents-Trip-Advisor  

---

### Step 2: Create Virtual Environment

python -m venv venv  

Windows:
venv\Scripts\activate  

Linux/Mac:
source venv/bin/activate  

---

### Step 3: Install Dependencies

pip install -r requirements.txt  

---

## 🔐 Environment Setup

Create a `.env` file in project root:

OPENAI_API_KEY=your_openai_key  
WEATHER_API_KEY=your_weather_api_key  
SEARCH_API_KEY=your_search_api_key  

---

## ▶ Running the Application

### Run Backend

cd Backend  
python app.py  

Backend runs at:
http://localhost:5000  

---

### Run Frontend

cd Frontend  
npm install  
npm start  

Frontend runs at:
http://localhost:3000  

---

## 🧪 Example Usage

User Input:

Plan a 5 day trip to Paris with budget 2000 USD.

System Output:

- Destination Overview  
- 5 Day Itinerary  
- Hotel Suggestions  
- Attractions List  
- Weather Forecast  

---

## 🧠 Agent Responsibilities

Destination Agent  
- Finds popular places  
- Gives city overview  

Hotel Agent  
- Suggests hotels by budget  

Activity Agent  
- Finds attractions  
- Suggests events  

Weather Agent  
- Fetches weather info  

Planner Agent  
- Builds final itinerary  

---

## 🧩 Adding New Agents

1. Create new file inside Agents folder  
2. Implement class with run() method  
3. Register agent in backend controller  

Example:

class BudgetAgent:
    def run(self, data):
        return result  

---

## 🔄 Workflow

1. User submits form  
2. Backend receives request  
3. Controller assigns tasks  
4. Agents call APIs / LLM  
5. Results returned  
6. Planner merges responses  
7. Frontend displays plan  

---

## 🧪 Testing

Run backend tests:

python -m pytest  

---

## 📈 Future Improvements

- Flight booking integration  
- Map visualization  
- User accounts  
- Save trip history  
- Mobile app  

---

## ❗ Troubleshooting

- Check API keys  
- Install all dependencies  
- Activate virtual environment  
- Ensure correct ports  

---

## 📜 License

MIT License  

---

## 👩‍💻 Author

Memona Hafeez  
GitHub: https://github.com/Memona-hafeez  

---

⭐ If you find this project useful, please star the repository!
