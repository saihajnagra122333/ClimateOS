import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# App title
st.title("🌱 ClimateOS MVP v0.1")
st.write("AI-Driven Geoengineering + Carbon Sequestration Optimizer")

# Load cleaned data
@st.cache_data
def load_data():
    return pd.read_csv("../data/cleaned_soil_data.csv")

data = load_data()

# Show data table
st.subheader("Cleaned Soil Data")
st.dataframe(data)

# Create folium map
st.subheader("Carbon Sequestration Map")
m = folium.Map(location=[23, 78], zoom_start=4)

# Add markers from data
for _, row in data.iterrows():
    folium.Marker(
        location=[row['lat'], row['lon']],
        popup=f"Soil: {row['soil_type']} | Rainfall: {row['rainfall']} mm | Carbon: {row['carbon_stock']} tCO2",
        icon=folium.Icon(color="green", icon="leaf")
    ).add_to(m)

# Display map
st_folium(m, width=700, height=450)

# Simple CO2 reduction graph (dummy plot)
import matplotlib.pyplot as plt
st.subheader("Projected CO2 Reduction")
years = [2025, 2030, 2035, 2040]
reduction = [0, 50, 150, 300]  # dummy values

plt.figure(figsize=(6,4))
plt.plot(years, reduction, marker='o')
plt.xlabel("Year")
plt.ylabel("CO2 Reduction (tCO2)")
plt.title("Projected CO2 Reduction Over Time")
st.pyplot(plt)





