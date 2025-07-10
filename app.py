import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

# Location mapping
location_map = {"Islamabad": 0, "Lahore": 1, "Karachi": 2}

# Page configuration
st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="centered",
    initial_sidebar_state="auto",
)

# Header section
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🏡 House Price Prediction App</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: grey;'>Enter your house details to get an estimated price instantly</h4><br>", unsafe_allow_html=True)

# Optional top image
st.image("https://images.unsplash.com/photo-1570129477492-45c003edd2be", use_column_width=True)

# Form section
st.markdown("### 📝 Enter House Details")

col1, col2 = st.columns(2)
with col1:
    area = st.number_input("📏 Area (in sq ft)", min_value=300, step=100)
with col2:
    location = st.selectbox("📍 Location", list(location_map.keys()))

col3, col4 = st.columns(2)
with col3:
    bedrooms = st.number_input("🛏️ Bedrooms", step=1, min_value=1)
with col4:
    bathrooms = st.number_input("🛁 Bathrooms", step=1, min_value=1)

# Spacer
st.markdown("<br>", unsafe_allow_html=True)

# Styled button using container and theme
with st.container():
    predict = st.button("💰 Predict Price")

# Prediction logic
if predict:
    loc_code = location_map[location]
    input_data = np.array([[area, bedrooms, bathrooms, loc_code]])
    predicted_price = model.predict(input_data)[0]

    st.markdown(f"<h2 style='color:#2196F3;'>💸 Estimated House Price: Rs. {int(predicted_price):,}</h2>", unsafe_allow_html=True)
else:
    st.markdown("✅ Fill in the details above and click Predict Price.")

# Footer
st.markdown("""
    <hr>
    <p style='text-align: center; color: grey;'>An House Price Pridiction App</p>
""", unsafe_allow_html=True)
