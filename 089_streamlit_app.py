import streamlit as st
import pandas as pd

# reading the database
data = pd.read_csv("tips.csv")

# Bar chart with day against tip
st.bar_chart(data.groupby('day')['tip'].mean())

# Title for the chart
st.title("Bar Chart")

# Setting the X and Y labels
st.xlabel('Day')
st.ylabel('Tip')
st.pyplot()
