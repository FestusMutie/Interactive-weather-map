import streamlit as st
import leafmap.foliumap as leafmap
import requests
from geopy.geocoders import Nominatim

# Function to get latitude and longitude from city name
def get_coordinates(city):
    geolocator = Nominatim(user_agent="weather_app")
    location = geolocator.geocode(city)
    if location:
        return location.latitude, location.longitude
    return None, None

# Function to fetch weather data from Open-Meteo
def get_weather_data(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

# Streamlit UI
st.title("🌍 Interactive Weather Map")
st.write("Enter a city or coordinates to view real-time temperature data.")

# User input for city or coordinates
col1, col2 = st.columns(2)

with col1:
    city = st.text_input("Enter city name (e.g., Nairobi, Berlin, New York):")

with col2:
    lat = st.text_input("Or enter latitude:")
    lon = st.text_input("Or enter longitude:")

# Convert city name to coordinates if provided
if city:
    lat, lon = get_coordinates(city)

# Convert lat/lon to float if provided
if lat and lon:
    try:
        lat, lon = float(lat), float(lon)
    except ValueError:
        st.error("Invalid latitude or longitude. Please enter numeric values.")
        lat, lon = None, None

if lat and lon:
    # Fetch weather data
    weather_data = get_weather_data(lat, lon)

    if weather_data:
        temp = weather_data["hourly"]["temperature_2m"][0]  # Get latest temperature
        st.write(f"**Current Temperature at {lat}, {lon}:** {temp}°C")

        # Create the map
        m = leafmap.Map(center=[lat, lon], zoom=6)
        m.add_marker([lat, lon], popup=f"🌡 {temp}°C")
        m.to_streamlit(height=500)
    else:
        st.error("Failed to retrieve weather data.")
