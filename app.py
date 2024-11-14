import streamlit as st
import pandas as pd
import joblib
import numpy as np
import requests
from streamlit_lottie import st_lottie

# Function to load Lottie URL
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Lottie animations
lottie_coding = load_lottieurl("https://lottie.host/342f0bbc-697d-4ce9-b5d9-b0b87ca8e90e/9JgE51wznk.json")
lottie_coding1 = load_lottieurl("https://lottie.host/b98b367e-b9bd-4178-9626-b72a9335e820/uwdMVdCEeT.json")
lottie_coding2 = load_lottieurl("https://lottie.host/fc3e7662-72bc-43ab-b508-c174ee7332e2/kXACUpNjwi.json")

# Load the trained model
model = joblib.load('walmart_sales_model.pkl')  # Your trained model (Ensure it's saved in the correct path)

# Header section with Lottie animations for engagement
st.title("AI-Powered Retail Shelf Management System")

# Add Lottie animation (Intro GIF or animation)
st_lottie(lottie_coding, speed=1, width=600, height=400, key="coding")

st.write("Enter the details for store sales prediction:")

# Input fields for user to enter values
store = st.number_input('Store', min_value=1, max_value=45, step=1)  # Assuming 45 stores
holiday_flag = st.number_input('Holiday Flag (0 or 1)', min_value=0, max_value=1, step=1)

# Slider for Temperature (°F)
temperature = st.slider('Temperature (°F)', min_value=-20, max_value=110, step=1, value=70)

# Slider for Fuel Price (USD)
fuel_price = st.slider('Fuel Price (USD)', min_value=0.5, max_value=5.0, step=0.01, value=2.5)

# Slider for Consumer Price Index (CPI)
cpi = st.slider('Consumer Price Index (CPI)', min_value=100.0, max_value=250.0, step=0.1, value=200.0)

# Slider for Unemployment Rate (%)
unemployment = st.slider('Unemployment Rate (%)', min_value=0.0, max_value=15.0, step=0.1, value=5.0)

# Date input for Year, Month, and Day
date_input = st.date_input("Select Date", min_value=pd.to_datetime("2010-01-01"), max_value=pd.to_datetime("2020-12-31"), value=pd.to_datetime("2020-01-01"))

# Extract the year, month, and day from the selected date
year = date_input.year
month = date_input.month
day = date_input.day

# Slider for Weekday (0=Sunday, 6=Saturday)
weekday = st.slider('Weekday (0=Sunday, 6=Saturday)', min_value=0, max_value=6, step=1, value=3)  # Default to Wednesday

# Prediction button with a fun Lottie animation on click
if st.button("Predict Weekly Sales"):


    # Prepare input data as a DataFrame
    input_data = pd.DataFrame({
        'Store': [store],
        'Holiday_Flag': [holiday_flag],
        'Temperature': [temperature],
        'Fuel_Price': [fuel_price],
        'CPI': [cpi],
        'Unemployment': [unemployment],
        'Year': [year],
        'Month': [month],
        'Day': [day],
        'Weekday': [weekday]
    })
    
    # Make prediction
    prediction = model.predict(input_data)
    
    # Use Streamlit columns to place Lottie animations on both sides
    col1, col2, col3 = st.columns([1, 4, 1])  # Create 3 columns: Left, Center, Right
    with col1:
        st_lottie(lottie_coding1, speed=1, width=100, height=100, key="left")
    with col2:
        # Display the prediction in a large, bold, and centered style using Markdown
        st.markdown(f"<h2 style='text-align: center; font-size: 40px; font-weight: bold;'>Predicted Weekly Sales: ${prediction[0]:,.2f}</h2>", unsafe_allow_html=True)
    with col3:
        st_lottie(lottie_coding1, speed=1, width=100, height=100, key="right")
    
    col1, col2, col3 = st.columns([1, 4, 1])  # Create 3 columns again for centering
    with col2:
        st_lottie(lottie_coding2, speed=1, width=400, height=400, key="final_animation")