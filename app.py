import streamlit as st
import requests
from datetime import datetime

st.title("Taxi Fare Predictor")

date = st.date_input("Date")
time = st.time_input("Time")
pickup = st.text_input("Pickup (lat,long)", "40.748817,-73.985428")
dropoff = st.text_input("Dropoff (lat,long)", "40.761432,-73.977622")
passengers = st.number_input("Passengers", 1, 10, 1)

pickup_lat, pickup_lon = map(float, pickup.split(','))
dropoff_lat, dropoff_lon = map(float, dropoff.split(','))
pickup_datetime = f"{date} {time}"

url = "https://taxifare-33741543340.europe-west1.run.app/predict"

if st.button("Predict"):
    params = {
        "pickup_datetime": pickup_datetime,
        "pickup_longitude": pickup_lon,
        "pickup_latitude": pickup_lat,
        "dropoff_longitude": dropoff_lon,
        "dropoff_latitude": dropoff_lat,
        "passenger_count": passengers
    }

    try:
        response = requests.get(url, params=params)
        fare = response.json().get("fare")
        st.success(f"Estimated Fare: ${fare:.2f}")
    except:
        st.error("Something went wrong. Please check your input or API.")
