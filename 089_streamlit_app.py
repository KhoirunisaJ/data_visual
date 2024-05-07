import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# reading the database
data = pd.read_csv("tips.csv")

st.title("My Dashboard")

# Bagian visualisasi data
st.header("Selamat Datang")

# Bar chart with day against tip
st.bar_chart(data.groupby('day')['tip'].mean())

# Title for the chart
st.title("Bar Chart")

# Setting the X and Y labels
st.xlabel('Day')
st.ylabel('Tip')
st.pyplot()
