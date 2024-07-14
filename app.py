import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from st_aggrid import AgGrid, GridOptionsBuilder

st.write("Lokesh Kumawat Data Engineer")

st.write("This is a beginner level project to get started with streamlit for deploying Data Engineering tasks")

st.write("Here, i've used the famous iris dataset to create a data exploration tool.")

# Load iris dataset from CSV
df = pd.read_csv('iris.csv')

# Create sidebar
st.sidebar.header('Filter Data')
min_value = st.sidebar.slider('Minimum Sepal Length (cm)', 0, 10, 0)
max_value = st.sidebar.slider('Maximum Sepal Length (cm)', 0, 10, 10)

species_mapping = {0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'}
species = st.sidebar.multiselect('Select Species', sorted(df['target'].map(species_mapping).unique()))

# Filter data based on user input
filtered_df = df[(df['sepal length (cm)'] >= min_value) & (df['sepal length (cm)'] <= max_value)]
if species:
    species_filter = [key for key, value in species_mapping.items() if value in species]
    filtered_df = filtered_df[filtered_df['target'].isin(species_filter)]

# Display filtered data
st.write(filtered_df)

# Scatter plot
st.write("Scatter Plot of Sepal Length vs Sepal Width")
fig = px.scatter(filtered_df, x='sepal length (cm)', y='sepal width (cm)', color='target', labels={'target': 'Species'})
st.plotly_chart(fig)

# Summary statistics
if st.sidebar.checkbox('Show Summary Statistics'):
    st.write("Summary Statistics")
    st.write(filtered_df.describe())

# Sepal length distribution
if st.sidebar.checkbox('Show Sepal Length Distribution'):
    st.write("Sepal Length Distribution")
    fig, ax = plt.subplots()
    filtered_df['sepal length (cm)'].hist(bins=20, ax=ax)
    ax.set_title('Sepal Length Distribution')
    ax.set_xlabel('Sepal Length (cm)')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)

# Interactive data table
st.write("Interactive Data Table")
gb = GridOptionsBuilder.from_dataframe(filtered_df)
gb.configure_pagination(paginationAutoPageSize=True)
gb.configure_side_bar()
gb.configure_selection('multiple', use_checkbox=True)
gridOptions = gb.build()

AgGrid(filtered_df, gridOptions=gridOptions, enable_enterprise_modules=True)

# Correlation heatmap
if st.sidebar.checkbox('Show Correlation Heatmap'):
    st.write("Correlation Heatmap")
    fig, ax = plt.subplots()
    # Check for NaN values before creating heatmap
    if not filtered_df.empty and not filtered_df.isnull().values.any():
        corr = filtered_df.corr()
        sns.heatmap(corr, annot=True, ax=ax, cmap='coolwarm')
        st.pyplot(fig)
    else:
        st.write("Dataset contains NaN values. Handle missing data before displaying heatmap.")

# Pair plot
if st.sidebar.checkbox('Show Pair Plot'):
    st.write("Pair Plot")
    fig = px.scatter_matrix(filtered_df, dimensions=['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'], color='target', labels={'target': 'Species'})
    st.plotly_chart(fig)
