import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# reading the database
file_path = "tips.csv"
data = pd.read_csv(file_path, encoding='latin-1')

# Bar chart with day against tip
plt.bar(data['day'], data['tip'])
plt.title("Bar Chart")
# Setting the X and Y labels
plt.xlabel('Day')
plt.ylabel('Tip')
st.pyplot(fig)
