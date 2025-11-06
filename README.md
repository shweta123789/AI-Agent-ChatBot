# AI Agent Chatbot with Groq LLM

## Project Description
This project is a web-based AI chatbot application built using **FastAPI** for the backend and **Streamlit** for the frontend. The chatbot leverages the **Groq LLM** (`llama-3.3-70b-versatile`) to provide intelligent, context-aware responses. Users can define a custom system prompt, ask questions, and optionally enable web search functionality.  

The project demonstrates integration of large language models, conversational AI agents, and a simple UI to interact with AI in real time.

---

## Features
- Interactive AI chatbot with **custom system prompt**
- Uses **Groq LLM** for generating responses
- Option to allow web search (currently placeholder)
- Built using **FastAPI** backend and **Streamlit** frontend
- Easy configuration with `.env` for API keys

---

## Technologies Used
- Python 3.10+
- [FastAPI](https://fastapi.tiangolo.com/) – Backend API
- [Streamlit](https://streamlit.io/) – Frontend UI
- [LangChain Groq](https://pypi.org/project/langchain-groq/) – Groq LLM integration
- dotenv – Load environment variables
- Requests – HTTP requests from frontend to backend

---

## Project Structure

AI_Agent_Chatbot/
│
├─ backend.py # FastAPI backend

├─ frontend.py # Streamlit frontend

├─ ai_agent.py # AI agent logic with Groq LLM

├─ .env # API keys configuration

└─ README.md # Project documentation



## Install dependencies
   
pip install -r requirements.txt

## Configure environment variables

Create a .env file in the project root:
GROQ_API_KEY=your_groq_api_key

## Run the backend
python backend.py

The backend runs on http://127.0.0.1:8765 (or any port you set in backend.py). 

## 5. Run the frontend
streamlit run frontend.py





