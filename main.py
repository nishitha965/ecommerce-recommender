from fastapi import FastAPI
from recommend import recommend_products
from llm import generate_explanation

app = FastAPI()

# Root endpoint
@app.get("/")
def root():
    return {"message": "E-commerce Recommender API is running"}

# Recommendation endpoint
@app.get("/recommend/{user_id}")
def recommend(user_id: int):
    try:
        recs = recommend_products(user_id)
        if not recs:
            return {"message": f"No recommendations found for user {user_id}"}

        results = []
        for rec in recs:
            explanation = generate_explanation(user_id, rec[1])
            results.append({
                "id": rec[0],
                "name": rec[1],
                "category": rec[2],
                "price": rec[3],
                "explanation": explanation
            })
        return results

    except Exception as e:
        return {"error": "Internal server error", "details": str(e)}
