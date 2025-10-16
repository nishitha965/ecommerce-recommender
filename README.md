# E-commerce Product Recommender

A simple e-commerce recommender system that combines product recommendations based on user behavior with LLM-generated explanations. Includes a backend API (FastAPI) and a frontend dashboard (Streamlit).

## Features

- Personalized product recommendations based on user behavior
- LLM-generated explanations for each recommendation
- Fallback recommendations for new users
- Interactive frontend dashboard with Streamlit

## Project Structure

ecommerce-recommender/
├── app.py # Streamlit frontend
├── main.py # FastAPI backend
├── recommend.py # Recommendation logic
├── llm.py # LLM explanation (mock or OpenAI API)
├── database.py # Database creation
├── populate_data.py # Sample data population
├── ecommerce.db # SQLite database (generated)
├── .gitignore
└── README.md