import streamlit as st
import pandas as pd

# reading the database
data = pd.read_csv("tips.csv")

st.title("My Dashboard")

# Bagian visualisasi data
st.header("Selamat Datang")
st.h1("selamat melihat dashboardku")
st.h1("ini adalah dashboard tips. Semoga membantu")

# Bar chart with day against tip
st.bar_chart(data.groupby('day')['tip'].mean())

# Title for the chart
st.title("Bar Chart")

# Setting the X and Y labels
st.xlabel('Day')
st.ylabel('Tip')
st.pyplot()

# Scatter plot using seaborn
sns.scatterplot(x='day', y='tip', data=data, hue='sex')

# Title for the plot
plt.title("Scatter Plot")

# Show plot in Streamlit app
st.pyplot()
