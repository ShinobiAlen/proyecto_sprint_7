import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Análisis de vehículos")

# cargar datos
df = pd.read_csv('vehicles_us.csv')

st.write("Vista previa del dataset")
st.dataframe(df.head())

# Histograma
if st.checkbox("Mostrar histograma del odómetro"):
    fig = px.histogram(df, x="odometer")
    st.plotly_chart(fig)

# Scatter plot
if st.checkbox("Relación precio vs odómetro"):
    fig = px.scatter(df, x="odometer", y="price")
    st.plotly_chart(fig)
