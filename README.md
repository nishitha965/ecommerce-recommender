.

🛒 E-commerce Product Recommender
🎯 Objective

This project combines a simple product recommendation system with LLM-powered explanations to help users understand why specific items are recommended to them.

It demonstrates how recommendation logic and AI-driven natural language explanations can work together in an e-commerce context.

🚀 Features

📦 Product Catalog: Stores products with names, categories, and prices.

👤 User Behavior Tracking: Logs user interactions to inform recommendations.

🤖 LLM-Powered Explanations: Generates personalized explanations for each recommendation.

🖥️ Interactive Frontend Dashboard: Built with Streamlit to view recommendations for any user.

⚙️ RESTful Backend API: FastAPI backend serving product and recommendation data.

🧩 Project Structure
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

⚙️ Tech Stack
Component	Technology Used
Frontend UI	Streamlit
Backend API	FastAPI
Database	SQLite
AI Explanation	Mock LLM (replaceable with OpenAI or similar)
Language	Python 3.10+
💻 Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/ecommerce-recommender.git
cd ecommerce-recommender

2️⃣ Create and Activate a Virtual Environment

Windows PowerShell:

python -m venv .venv
.venv\Scripts\Activate.ps1


If script execution is blocked:

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\Activate.ps1

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Populate Sample Data
python populate_data.py


You should see:

Sample data added.

🧠 Running the Project
🖥️ Terminal 1 — Start Backend (FastAPI)
uvicorn main:app --reload


Backend will start at:
👉 http://127.0.0.1:8000

💻 Terminal 2 — Start Frontend (Streamlit)
streamlit run app.py


Frontend will open at:
👉 http://localhost:8501

🧠 How It Works

The backend (main.py) retrieves user interaction data from the database.

The recommender (recommender.py) finds products based on similar categories or interests.

The LLM (llm.py) generates a human-readable explanation of why each product is recommended.

The frontend (app.py) displays recommendations for a selected user in an interactive UI.

📊 Example Output

Input:
User ID = 1

Output:
Recommended Products:

“Wireless Headphones” 🎧
→ Because user 1 interacted with similar products, Wireless Headphones is recommended.

“Bluetooth Speaker” 🔊
→ Users like you often buy Bluetooth Speaker.

🔧 Customization

To replace the mock LLM with OpenAI, update llm.py:

import openai
openai.api_key = "your_api_key"


Then use:

response = openai.ChatCompletion.create(...)

🧾 Future Improvements

✅ Integrate real machine learning recommendation models

✅ Add authentication and user profiles

✅ Deploy backend and frontend on Render or Vercel

✅ Store real-time user clickstream data

✅ Replace mock LLM with OpenAI or Hugging Face model

👨‍💻 Author

Nishitha
🎓 Computer Science Engineer
💡 Passionate about AI, Machine Learning, and Smart Applications.