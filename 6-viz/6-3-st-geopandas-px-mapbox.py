import random
import geopandas as gpd
import pandas as pd
import streamlit as st
import plotly.express as px
import streamlit_folium as sf
import folium

st.title('Streamlit Geopandas Examples')
st.caption('This is a simple example of how to use Streamlit to create visualizations with Geopandas')

# Load the GeoPandas data
st.write("## Saint Lucia Choropleth")
gdf = gpd.read_file("./6-viz/data/stlucia.geojson")
gdf['Amount'] = gdf.apply(lambda row: random.randint(50,275), axis=1)
st.write(gdf)

sf.folium_static(gdf.explore(gdf['Amount']))

wards_df = gpd.read_file("https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/city-of-syracuse/wards.geojson")
wards_df['amount'] = wards_df.apply(lambda row: random.randint(1,50), axis=1)

st.write('## City of Syracuse Wards - Choropleth')
st.write(wards_df)
sf.folium_static(wards_df.explore(wards_df['amount']))

stlucia_df = pd.read_csv("https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/st-lucia/parishes.csv")
stlucia_df['Amount'] = stlucia_df.apply(lambda row: random.randint(50,500), axis=1)


classesdf = pd.read_csv("https://raw.githubusercontent.com/mafudge/datasets/master/delimited/class-schedule.csv")
gdf = gpd.GeoDataFrame(classesdf, geometry=gpd.points_from_xy(classesdf['Lon'], classesdf['Lat']))
st.write(gdf)
schine = (43.03986, -76.13375)
m = folium.Map(location=schine, zoom_start=17)
mout = gdf.explore(popup="Course",lat="Lat", lon="Lon", m=m, marker_type="marker")
sf.folium_static(mout)


st.write("# Mapbox - Plotly Express")
st.write('## Saint Lucia Parishes - Scatter')
fig = px.scatter_mapbox(stlucia_df,  lat="Lat", lon="Lng", zoom=10, color = 'Parish', hover_name = 'Parish', size = 'Amount',  mapbox_style="open-street-map")
st.plotly_chart(fig)

st.write('## Saint Lucia Parishes - Density')
fig = px.density_mapbox(stlucia_df, lat='Lat', lon='Lng', z='Amount', radius=10, center=dict(lat=13.9, lon=-60.97), zoom=10, mapbox_style="open-street-map")
st.plotly_chart(fig)
