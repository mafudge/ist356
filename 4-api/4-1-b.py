import requests
import dotenv
import os

from weather import geocode, weather

dotenv.load_dotenv(".env")
CENT_API_KEY = os.getenv("CENT_API_KEY")

import streamlit as st

st.title("Weather App")
location = st.text_input("Enter a location (city, state, or country):")
if location:
    lat, lon = geocode(location)
    if lat is None or lon is None:
        st.error("Location not found.")
    else:
        temp = weather(lat, lon)
        st.metric(label="Temperature", value=f"{temp}°F", delta=None)