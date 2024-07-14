import streamlit as st
import pandas as pd

st.write("Lokesh Kumawat Data Engineer")
st.write("This is a beginner level project to get started with streamlit for deploying Data Engineering tasks")

st.write("Here, i've used the famous iris dataset to create a data exploration tool.")

st.write("i've load the iris dataset and create a sidebar that allows users to filter the data based on the sepal length.")



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
