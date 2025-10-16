E-commerce Product Recommender
Objective

This project combines a simple product recommendation system with LLM-powered explanations to help users understand why specific items are recommended to them.

It demonstrates how recommendation logic and AI-generated explanations can work together in an e-commerce context.

Features

Product Catalog: Stores product names, categories, and prices.

User Behavior Tracking: Logs user interactions to inform recommendations.

LLM-Powered Explanations: Generates personalized text explanations for each recommendation.

Interactive Frontend Dashboard: Built using Streamlit.

RESTful Backend API: Implemented with FastAPI to serve recommendations and product data.

Project Structure
ecommerce-recommender/
│
├── app.py                 # Streamlit frontend
├── main.py                # FastAPI backend
├── recommender.py         # Core recommendation logic
├── llm.py                 # LLM-based explanation generation
├── database.py            # SQLite database setup
├── populate_data.py       # Adds sample data to the database
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation

Tech Stack
Component	Technology Used
Frontend UI	Streamlit
Backend API	FastAPI
Database	SQLite
AI Explanation	Mock LLM (can be replaced with OpenAI API)
Language	Python 3.10+
Setup Instructions
1. Clone the Repository
git clone https://github.com/<your-username>/ecommerce-recommender.git
cd ecommerce-recommender

2. Create and Activate a Virtual Environment

Windows PowerShell:

python -m venv .venv
.venv\Scripts\Activate.ps1


If script execution is blocked:

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\Activate.ps1

3. Install Dependencies
pip install -r requirements.txt

4. Populate Sample Data
python populate_data.py


Expected output:

Sample data added.

Running the Project
Terminal 1 — Start Backend (FastAPI)
uvicorn main:app --reload


The backend will start at:
http://127.0.0.1:8000

Terminal 2 — Start Frontend (Streamlit)
streamlit run app.py


The frontend will open automatically at:
http://localhost:8501

How It Works

The backend (main.py) retrieves user interaction data from the database.

The recommender system (recommender.py) selects products based on user interests or category similarity.

The LLM module (llm.py) generates short, natural language explanations for each recommendation.

The frontend (app.py) displays personalized product recommendations for each user in an interactive dashboard.

Example Output

Input:
User ID = 1

Output:
Recommended Products:

Wireless Headphones
Because user 1 interacted with similar products, Wireless Headphones is recommended.

Bluetooth Speaker
Users like you often buy Bluetooth Speaker.

Customization

If you want to use the OpenAI API instead of a mock LLM:

Update the file llm.py:

import openai
openai.api_key = "your_api_key"


Replace the logic with:

response = openai.ChatCompletion.create(...)


This will generate real AI-based explanations.

Future Improvements

Integrate a real machine learning-based recommender model

Add user authentication and personalization features

Deploy the app (backend + frontend) on cloud services like Render or Vercel

Include real-time user behavior tracking

Replace mock LLM with OpenAI GPT or Hugging Face models

Author

Nishitha
Computer Science Engineer
Passionate about Artificial Intelligence, Machine Learning, and Smart Applications

License

This project is licensed under the MIT License.