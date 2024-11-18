import pandas as pd
import streamlit as st
import folium
import streamlit_folium as sf


days  = {
    'Sunday': 'red',
    'Monday': 'orange',
    'Tuesday': 'beige',
    'Wednesday': 'green',
    'Thursday': 'blue',
    'Friday': 'purple',
    'Saturday': 'gray'
}

st.title('Streamlit Park magic')

map = folium.Map(location=[43.0481, -76.1474], zoom_start=15)
df = pd.read_csv('./6-viz/data/final_cuse_parking_violations.csv')
df_dropped = df.dropna()
status = df_dropped['status'].unique()

status = st.selectbox('Select ticket status: ', status)

df_filtered = df_dropped[df_dropped['status'] == status]

df_sample = df_filtered.sample(50)

for i, row in df_sample.iterrows():
    lat, lon = row['coords'].strip("(").strip(")").split(',') 
    lat = float(lat.replace("'", ""))
    lon = float(lon.replace("'", ""))
    color = days[row['dayofweek']]
    folium.Marker((lat, lon), popup=row['location'], tooltip=row['location'], icon=folium.Icon(color=color)).add_to(map)


sf.folium_static(map)
