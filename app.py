import streamlit as st
import pandas as pd
import plotly.express as px

# Leer los datos desde la raíz (ya tienes vehicles_us.csv ahí)
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header('Aplicación de Análisis de Vehículos 🚗')

# Botón para el histograma
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botón para el gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión entre precio y kilometraje')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
