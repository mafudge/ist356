import streamlit as st
import streamlit_folium as sf
import folium
import pandas as pd
import geopandas as gpd


# Here's a more straigtforward example with unemployment data:
CENTER_US = (39.8333333,-98.585522)
u_df = pd.read_csv('https://raw.githubusercontent.com/wrobstory/vincent/master/examples/data/US_Unemployment_Oct2012.csv')
state_geojson = './6-viz/data/us-states.geojson'
geo = gpd.read_file(state_geojson)
combined = pd.merge(geo, u_df, left_on='id', right_on='State')
map = folium.Map(location=CENTER_US, zoom_start=4)
st.write('## US Unemployment Choropleth - 2012')
out_map = combined.explore(m=map, column='Unemployment', cmap='YlGn', legend=True)
sf.folium_static(out_map)
