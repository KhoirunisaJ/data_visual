import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# reading the database
data = pd.read_csv("tips.csv")

st.title("My Dashboard")
# Title for the chart
st.title("Bar Chart")

# Bagian visualisasi data
st.header("Selamat Datang")
st.subheader("Jumlah Tips per hari")

# Bar chart with day against tip
sns.scatterplot(x='day', y='tip', data=data, hue='sex')
# Bar chart with day against tip
st.bar_chart(data.groupby('day')['tip'].mean())

# Setting the X and Y labels
st.pyplot()
