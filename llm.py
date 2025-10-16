import random

def generate_explanation(user_id, product_name):
    # Mock explanations
    templates = [
        f"Because user {user_id} interacted with similar products, {product_name} is recommended.",
        f"{product_name} matches the user's past interests.",
        f"Users like you often buy {product_name}.",
        f"{product_name} is a popular choice in categories you like."
    ]
    return random.choice(templates)
