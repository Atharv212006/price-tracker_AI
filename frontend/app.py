import streamlit as st
import requests

st.set_page_config(page_title="Price Tracker", page_icon="◈", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700&family=DM+Mono:wght@400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'Syne', sans-serif;
}

/* Page background */
.stApp {
    background-color: #0d0d0f;
    background-image:
        linear-gradient(rgba(255,255,255,0.025) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,0.025) 1px, transparent 1px);
    background-size: 48px 48px;
}

/* Hide Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 48px 32px 64px; max-width: 600px; }

/* Eyebrow tag */
.eyebrow {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: #c9a84c;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 12px;
}
.eyebrow::before {
    content: '';
    display: inline-block;
    width: 24px;
    height: 1px;
    background: #c9a84c;
}

/* Heading */
h1 {
    font-size: 42px !important;
    font-weight: 700 !important;
    color: #f0ede6 !important;
    letter-spacing: -0.02em !important;
    line-height: 1.1 !important;
    margin-bottom: 8px !important;
}

.subtitle {
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    color: #555;
    margin-bottom: 40px;
}

/* Form card */
.form-card {
    background: #131316;
    border: 1px solid #1e1e22;
    padding: 32px;
    position: relative;
    margin-top: 8px;
}
.form-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, #c9a84c, transparent);
}

/* Labels */
.stTextInput label, .stNumberInput label {
    font-family: 'DM Mono', monospace !important;
    font-size: 10px !important;
    letter-spacing: 0.15em !important;
    text-transform: uppercase !important;
    color: #666 !important;
}

/* Inputs */
.stTextInput input, .stNumberInput input {
    background: #0d0d0f !important;
    border: 1px solid #222 !important;
    border-radius: 0 !important;
    color: #e8e6e0 !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 13px !important;
    padding: 12px 16px !important;
}
.stTextInput input:focus, .stNumberInput input:focus {
    border-color: #c9a84c !important;
    box-shadow: none !important;
}

/* Buttons */
.stButton button {
    border-radius: 0 !important;
    font-family: 'Syne', sans-serif !important;
    font-size: 13px !important;
    font-weight: 600 !important;
    letter-spacing: 0.05em !important;
    padding: 13px 20px !important;
    width: 100% !important;
    transition: all 0.15s !important;
}

/* Primary button (col2 - Track) */
[data-testid="column"]:nth-child(2) .stButton button {
    background: #c9a84c !important;
    color: #0d0d0f !important;
    border: none !important;
}
[data-testid="column"]:nth-child(2) .stButton button:hover {
    background: #d4b660 !important;
}

/* Secondary button (col1 - Check) */
[data-testid="column"]:nth-child(1) .stButton button {
    background: transparent !important;
    border: 1px solid #2a2a2e !important;
    color: #999 !important;
}
[data-testid="column"]:nth-child(1) .stButton button:hover {
    border-color: #555 !important;
    color: #e8e6e0 !important;
}

/* Alerts */
.stSuccess, .stWarning, .stError {
    border-radius: 0 !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 12px !important;
}

/* Number input spinner */
.stNumberInput [data-testid="stNumberInputStepDown"],
.stNumberInput [data-testid="stNumberInputStepUp"] {
    background: #1a1a1e !important;
    border-color: #222 !important;
    color: #c9a84c !important;
}
</style>

<div class="eyebrow">Real-time tracking</div>
""", unsafe_allow_html=True)

st.markdown("<h1>Price<br>Tracker</h1>", unsafe_allow_html=True)
st.markdown('<p class="subtitle">monitor any product. alert on drop.</p>', unsafe_allow_html=True)

st.markdown('<div class="form-card">', unsafe_allow_html=True)

url = st.text_input("Product URL", placeholder="https://amazon.in/product/...")
target_price = st.number_input("Target Price (₹)", min_value=0.0, format="%.2f")

col1, col2 = st.columns(2)

BACKEND_URL = "http://127.0.0.1:5000"

with col1:
    if st.button("Check Price"):
        if not url:
            st.warning("Enter a product URL")
        else:
            try:
                res = requests.post(f"{BACKEND_URL}/get-price", json={"url": url})
                data = res.json()
                st.success(f"Current price: ₹{data['price']}")
            except:
                st.error("Backend not reachable")

with col2:
    if st.button("Track Product"):
        if not url or target_price == 0:
            st.warning("Enter URL and target price")
        else:
            try:
                res = requests.post(
                    f"{BACKEND_URL}/track",
                    json={"url": url, "target_price": target_price}
                )
                st.success("Tracking active — you'll be notified on drop")
            except:
                st.error("Failed to start tracking")

st.markdown('</div>', unsafe_allow_html=True)