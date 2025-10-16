import streamlit as st
import requests

# --- Page setup ---
st.set_page_config(page_title="E-commerce Recommender", layout="wide")
st.title("🛒 E-commerce Product Recommender")
st.write("Enter your User ID to get personalized product recommendations.")

# --- User input ---
user_id = st.number_input("User ID", min_value=1, step=1)

# --- Button to fetch recommendations ---
if st.button("Get Recommendations"):
    with st.spinner("Fetching recommendations..."):
        try:
            # Call backend API
            response = requests.get(f"http://127.0.0.1:8000/recommend/{user_id}")
            response.raise_for_status()  # Raise error for bad status
            data = response.json()

            # --- Handle backend messages ---
            if "message" in data:
                st.warning(data["message"])
            elif "error" in data:
                st.error(data["error"])
            else:
                # --- Display recommendations ---
                for item in data:
                    with st.container():
                        st.subheader(f"🛍️ {item['name']}")
                        st.write(f"**Category:** {item['category']}  |  **Price:** ${item['price']}")
                        with st.expander("💡 Why this product is recommended?"):
                            st.write(item['explanation'])
                        st.markdown("---")  # Divider between products

        except requests.exceptions.RequestException as e:
            st.error(f"Request failed: {e}")
        except ValueError:
            st.error("Response was not valid JSON. Check backend!")
