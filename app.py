import streamlit as st
import pandas as pd
import joblib
# Load model and feature names

model = joblib.load("../models/final_model.pkl")
feature_names = joblib.load("../models/feature_names.pkl")

st.title("Delivery Time Prediction App")

st.write("provide order details below to predict delivery time.")

# User inputs

distance = st.number_input("Distance (km)",min_value=0.1,max_value=100.0,value=5.0)
prepare_time = st.number_input("Preparation Time (min)",min_value=1.0,max_value=120.0,value=15.0)
experience = st.number_input("Courier Experience (years)",min_value=0.0,max_value=20.0,value=2.0)

time_category = st.selectbox("Time of Day", ["Non-Peak", "Peak"])
weather = st.selectbox("Weather Condition", ["Normal", "Delay-Risk"])
traffic = st.selectbox("Traffic Level", ["Low", "Medium", "High"])
vehicle = st.selectbox("Vehicle Type", ["Bike", "Scooter", "Car"])

# Convert categorical values to model format
input_data = {
    "Distance_km": distance,
    "Preparation_Time_min": prepare_time,
    "Courier_Experience_yrs": experience,
    "Weather_category": 1 if weather == "Delay-Risk" else 0,
    "Traffic_Level": {"Low":1, "Medium":2, "High":3}[traffic],
    "Vehicle_Type_Scooter": 1 if vehicle == "Scooter" else 0,
    "Vehicle_Type_Car": 1 if vehicle == "Car" else 0
}
input_df = pd.DataFrame([input_data]) 

input_df = input_df.reindex(columns=feature_names, fill_value=0)
