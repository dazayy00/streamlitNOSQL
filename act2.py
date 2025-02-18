import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import datetime

# Cargar datos
TITANIC_LINK = 'titanic.csv'
UBER_DATA_URL = 'uber_dataset.csv'
titanic_data = pd.read_csv(TITANIC_LINK)

def load_uber_data(nrows):
    data = pd.read_csv(UBER_DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data['date/time'] = pd.to_datetime(data['date/time'])
    return data

# Configuración de la app
st.title('Aplicaciones de Datos')
sidebar = st.sidebar

# Información del usuario
sidebar.image("perfil.png", width=150)
sidebar.write("**Nombre:** Johan David Baltazar Trinidad")
sidebar.write("**Matrícula:** s21020562")

# Configurar pestañas
tabs = st.tabs(["Titanic", "Mapa de San Francisco", "Uber NYC"])

with tabs[0]:
    st.header('Titanic Dataset')
    if st.checkbox("Mostrar DataFrame del Titanic"):
        st.dataframe(titanic_data)
    
    st.subheader("Descripción de Datos")
    fig, ax = plt.subplots()
    ax.hist(titanic_data.fare)
    st.pyplot(fig)
    st.write("Histograma de tarifas del Titanic")
    
    fig2, ax2 = plt.subplots()
    ax2.barh(titanic_data['class'], titanic_data['fare'])
    ax2.set_ylabel("Clase")
    ax2.set_xlabel("Tarifa")
    ax2.set_title("Tarifas pagadas por clase en el Titanic")
    st.pyplot(fig2)
    
    fig3, ax3 = plt.subplots()
    ax3.scatter(titanic_data.age, titanic_data.fare)
    ax3.set_xlabel("Edad")
    ax3.set_ylabel("Tarifa")
    st.pyplot(fig3)
    st.write("Gráfica de dispersión de edad vs tarifa")
    
    # Filtros del Titanic
    today = datetime.date.today()
    today_date = st.date_input('Seleccionar fecha', today)
    st.success(f'Fecha seleccionada: `{today_date}`')
    
    selected_town = st.radio("Seleccionar ciudad de embarque", titanic_data['embark_town'].unique())
    st.write("Ciudad de embarque seleccionada:", selected_town)
    
    optionals = st.expander("Configuraciones opcionales", True)
    fare_min = optionals.slider("Tarifa mínima", float(titanic_data['fare'].min()), float(titanic_data['fare'].max()))
    fare_max = optionals.slider("Tarifa máxima", float(titanic_data['fare'].min()), float(titanic_data['fare'].max()))
    subset_fare = titanic_data[(titanic_data['fare'] <= fare_max) & (fare_min <= titanic_data['fare'])]
    st.dataframe(subset_fare)

with tabs[1]:
    st.header("Mapa de San Francisco")
    map_data = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon']
    )
    st.map(map_data)

with tabs[2]:
    st.header("Uber Pickups en NYC")
    data_load_state = st.text('Cargando datos de Uber...')
    data = load_uber_data(1000)
    data_load_state.text("¡Carga completada!")
    
    hour_to_filter = st.slider('Seleccionar hora', 0, 23, 17)
    filtered_data = data[data['date/time'].dt.hour == hour_to_filter]
    st.subheader(f'Mapa de recogidas de Uber a las {hour_to_filter}:00')
    st.map(filtered_data)
