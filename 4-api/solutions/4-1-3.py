import requests
import streamlit as st


st.title("Streamlit Weather")
location = st.text_input("Enter a location")
if location:
    apikey = "ea044c96950db6cc0fab7ae1"
    headers = { "X-Api-Key": apikey }
    geourl = "https://cent.ischool-iot.net/api/google/geocode"
    params = { "location": location }
    response = requests.get(geourl, params=params, headers=headers)
    response.raise_for_status()
    geodata = response.json()
    
    lat, lon = geodata['results'][0]['geometry']['location']["lat"], geodata['results'][0]['geometry']['location']["lng"]
    weatherurl = "https://cent.ischool-iot.net/api/weather/current"
    params = { "lat": lat, "lon": lon, "units": "imperial" }
    response = requests.get(weatherurl, params=params, headers=headers)
    response.raise_for_status()
    weatherdata = response.json()
    coltemp, colhumid = st.columns(2)
    coltemp.metric("Temperature", f"{weatherdata['current']['temperature_2m']}{weatherdata['current_units']['temperature_2m']}")
    colhumid.metric("Humidity", f"{weatherdata['current']['relative_humidity_2m']}{weatherdata['current_units']['relative_humidity_2m']}")


