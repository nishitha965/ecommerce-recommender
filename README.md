# E-commerce Product Recommender

A simple **E-commerce product recommendation system** that combines user behavior tracking with **LLM-powered explanations**. It provides personalized product recommendations and explains why each product is suggested.

## Features

- Interactive **frontend dashboard** using Streamlit  
- **Product recommendation** based on user interaction history  
- **LLM-powered explanations** for each recommendation  
- **Backend API** using FastAPI  
- **SQLite database** for storing product catalog and user interactions  
- Top product suggestions if a user has no history  

## Tech Stack

- Python 3.10+  
- **Streamlit** for frontend  
- **FastAPI** for backend API  
- **SQLite** for database  
- **Mock LLM / OpenAI API** for explanation generation  

## Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/<your-username>/ecommerce-recommender.git
cd ecommerce-recommender

### 2. Create and activate a virtual environment

Windows PowerShell:

python -m venv .venv
.venv\Scripts\Activate.ps1


If script execution is blocked:

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\Activate.ps1

### 3. Install dependencies
pip install -r requirements.txt

### 4. Populate sample data
python populate_data.py

Running the Project
Terminal 1 — Start Backend (FastAPI)
uvicorn main:app --reload


The backend will be available at:
http://127.0.0.1:8000

Terminal 2 — Start Frontend (Streamlit)
streamlit run app.py


The frontend will open at:
http://localhost:8501

## How It Works

- Backend retrieves **user interactions** from the database  
- Recommender system identifies **products of interest** based on categories or user behavior  
- LLM generates a **human-readable explanation** for each recommendation  
- Frontend displays **personalized product suggestions** for the selected user  

## Example Output

**Input:**  
User ID = 1

**Output:**  
- **Wireless Headphones**  
  _Because user 1 interacted with similar products, Wireless Headphones is recommended_  

- **Bluetooth Speaker**  
  _Users like you often buy Bluetooth Speaker_  

## Customization

- Replace the mock LLM in `llm.py` with **OpenAI API**  
```python
import openai
openai.api_key = "your_api_key"