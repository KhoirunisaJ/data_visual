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
# Title for the chart
st.subheader("Bar Chart")
st.subheader("Jumlah Tips per hari")

st.subheader("Scatter Plot")
st.subheader("Jumlah Tips per hari")
fig, ax = plt.subplots()
sns.scatterplot(x='day', y='tip', data=data, hue='sex', ax=ax)

# Bar chart with day against tip
st.bar_chart(data.groupby('day')['tip'].mean())

# Show plot in Streamlit app
st.pyplot(fig)
