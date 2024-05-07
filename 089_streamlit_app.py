import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# reading the database
data = pd.read_csv("tips.csv")

# Bar chart with day against tip
fig, ax = plt.subplots()
ax.bar(data['day'], data['tip'])
ax.set_title("Bar Chart")
ax.set_xlabel('Day')
ax.set_ylabel('Tip')

# Show plot in Streamlit app
st.pyplot(fig)
