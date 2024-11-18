import folium
import streamlit as st
import pandas as pd

import streamlit_folium as sf


st.title('Streamlit Folium Example')
JMA = (43.0362, -76.1363)
HINDS = (43.0382, -76.1333)
m1 = folium.Map(location=JMA, zoom_start=16)
folium.Marker(JMA, popup="JMA Wireless Dome", tooltip="JMA", icon=folium.Icon(color="red")
).add_to(m1)
folium.Marker(HINDS, popup="iSchool", tooltip="Hinds Hall", icon=folium.Icon(color="blue")
).add_to(m1)

st.write('### Folium Map And Data')
st_data = sf.st_folium(m1, width=725)
st.write(st_data)

m2 = folium.Map(location=JMA, zoom_start=16)
folium.Marker(JMA, popup="JMA Wireless Dome", tooltip="JMA", icon=folium.Icon(color="red")
).add_to(m2)
folium.Marker(HINDS, popup="iSchool", tooltip="Hinds Hall", icon=folium.Icon(color="blue")
).add_to(m2)

st.write('### Folium Map Only')
sf.folium_static(m2, width=725)



