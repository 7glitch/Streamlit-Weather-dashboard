import streamlit as st
import random
import pandas as pd
import numpy as np
import requests
import json
st.write("Aathif's Weather Dashboard")
st.title("ST Weather Dashboard")
st.progress(100)
locations = {
    'China':(31.23, 121.47),
    'UAE':(25.20, 55.27 ),
    'Sri Lanka':(6.92, 79.86),
    'Qatar':(25.28, 51.53),
    'Saudi Arabia':(24.71, 46.67),
    'UK':(51.50,-0.12)
}
countries = list(locations.keys())
dropdown = st.sidebar.selectbox("Select your location:", options=list(locations.keys()))
country_code = {
    'China':'cn',
    'UAE':'ae',
    'Qatar':'qa',
    'Sri Lanka':'lk',
    'UK':'gb',
    'Saudi Arabia':'sa'
   
}
latitude, longitude = locations[dropdown]
API_URL = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=sunrise,sunset,daylight_duration,temperature_2m_max,temperature_2m_min,uv_index_max&hourly=temperature_2m,precipitation_probability,wind_speed_10m,rain,showers,relative_humidity_2m&current=temperature_2m,is_day,rain,precipitation&timezone=auto")
Value = json.loads(API_URL.text)
st.image(f'https://flagcdn.com/w160/{country_code[dropdown]}.png')
capital_url = requests.get(f'https://restcountries.com/v3.1/alpha/{country_code[dropdown]}?fields=capital')
capital = json.loads(capital_url.text)
st.subheader(f"City: {capital['capital'][0]}")
st.write('Timezone:', Value['timezone_abbreviation'])

st.sidebar.subheader("Weather")
st.sidebar.progress(1.0)
st.sidebar.write('Temperature:', Value['current']['temperature_2m'])
st.sidebar.write("Latitude", latitude)
st.sidebar.write("Longitude", longitude)
st.sidebar.write('Rain', Value['current']['rain'])
st.sidebar.write("Elevation", Value['elevation'])
st.sidebar.write("Home")
st.sidebar.write("About")

st.subheader("Weather Info")
chart_type = [
    'Bar Graph',
    'Line Graph',
    'Area Chart'
]
dropdown2 = st.selectbox("Select your prefered type of chart:", chart_type)
if dropdown2 == 'Bar Graph':
    st.bar_chart(data= [Value['daily']['sunrise'], Value['daily']['sunset']], width=1000, height=400, x_label='DURATION', y_label='DATE')
elif dropdown2 == 'Line Graph':
    st.line_chart(data= [Value['daily']['sunrise'], Value['daily']['sunset']], width=1000, height=400, x_label='DURATION', y_label='DATE')
elif dropdown2 == 'Area Chart':
    st.area_chart(data= [Value['daily']['sunrise'], Value['daily']['sunset']], width=1000, height=400, x_label='DURATION', y_label='DATE')



st.write("Duration of Daylight", Value['daily']['daylight_duration']) #Daylight duration info
st.write("Sunrise:", Value['daily']['sunrise'])   #sunrise and sunset times
st.write('Sunset:', Value['daily']['sunset'])
st.write('**Temperature for today:**', Value['daily']['temperature_2m_max'])
st.write(Value['hourly']['precipitation_probability'])
st.line_chart(data= Value['hourly']['precipitation_probability'], width=1000, height=400, color=["#fd0"], x_label='N/A', y_label='%')
st.write("Today's rainfall:", Value['hourly']['rain'])
st.link_button("<<< Click For More Info >>>", 'https://r.mtdv.me/articles/current-weather-info')
button = st.button("Show")
show = True
if button and show:
    show = True
    st.line_chart(data=Value['hourly']['rain'][0:100], color=['#ff00'], width=1000, height=400)
else:
    show = False

    

st.progress(1.0)
