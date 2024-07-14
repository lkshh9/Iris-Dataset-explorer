import streamlit as st
import pandas as pd

st.write("Lokesh Kumawat Data Engineer")

# Load iris dataset from CSV
df = pd.read_csv('iris.csv')

# Create sidebar
st.sidebar.header('Filter Data')
min_value = st.sidebar.slider('Minimum Value', 0, 10, 0)
max_value = st.sidebar.slider('Maximum Value', 0, 10, 10)

# Filter data based on user input
filtered_df = df[(df['sepal length (cm)'] >= min_value) & (df['sepal length (cm)'] <= max_value)]

# Display filtered data
st.write(filtered_df)
