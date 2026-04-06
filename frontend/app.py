import streamlit as st
import requests

# Page setup
st.set_page_config(page_title="Price Tracker AI", page_icon="💰", layout="wide")

# Title
st.title("💰 Price Tracker AI")
st.write("Track prices and predict future trends 📊")

# Input
url = st.text_input("🔗 Enter Product URL")

# Buttons
col1, col2 = st.columns(2)

with col1:
    check = st.button("Check Price")

with col2:
    predict = st.button("Predict Price")

# Backend URL
BACKEND_URL = "http://127.0.0.1:5000"

# Check Price
if check:
    if url == "":
        st.warning("Please enter URL")
    else:
        try:
            res = requests.post(f"{BACKEND_URL}/get-price", json={"url": url})
            data = res.json()
            st.success(f"Current Price: ₹{data['price']}")
        except:
            st.error("Backend not running")

# Predict Price
if predict:
    if url == "":
        st.warning("Please enter URL")
    else:
        try:
            res = requests.post(f"{BACKEND_URL}/predict", json={"url": url})
            data = res.json()
            st.success(f"Predicted Price: ₹{data['predicted_price']}")
        except:
            st.error("Prediction failed")

# Sample graph
st.subheader("📊 Price Trend")
import pandas as pd

df = pd.DataFrame({
    "Day": [1,2,3,4,5],
    "Price": [1000, 950, 970, 930, 910]
})

st.line_chart(df.set_index("Day"))