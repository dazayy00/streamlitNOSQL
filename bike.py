import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("CitiBike")

sidebar = st.sidebar

sidebar.image("perfil.png", width=150)
sidebar.write("**nombre:** Johan David Baltazar Trinidad")
sidebar.write("**matricula:** s21020562")

@st.cache_data
def load_data(nrows=None):
    """Carga el dataset de CitiBike y devuelve un DataFrame con el número de registros solicitados."""
    try:
        data = pd.read_csv("citibike-tripdata.csv", nrows=nrows, encoding="ISO-8859-1")
        data['started_at'] = pd.to_datetime(data['started_at'], errors='coerce') 
        data['hour'] = data['started_at'].dt.hour 
        return data
    except (FileNotFoundError, UnicodeDecodeError) as e:
        st.error(f"Error al cargar datos: {e}")
        return pd.DataFrame()

show_all = sidebar.checkbox("Mostrar todos los registros")

if show_all:
    bikes_data = load_data(None) 
else:
    bikes_data = load_data(500)

bikes_data.reset_index(drop=False, inplace=True)

hour = sidebar.slider("Selecciona la hora del día (0-23):", 0, 23, 12)


filtered_data = bikes_data[bikes_data['hour'] == hour]

filtered_data = filtered_data.rename(columns={"start_lat": "lat", "start_lng": "lon"})

st.write(f"### Registros a las {hour}:00 horas")
st.write(f"Se están mostrando {'todos' if show_all else '500'} registros filtrados por hora.")
st.dataframe(bikes_data)


st.write("### 🚲 Número total de recorridos por hora")
hourly_counts = bikes_data['hour'].value_counts().sort_index()

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(hourly_counts.index, hourly_counts.values, color='#007bff')
ax.set_xlabel('Hora del día')
ax.set_ylabel('Número de recorridos')
ax.set_title('Número total de recorridos por hora del día')
ax.set_xticks(range(0, 24))
ax.grid(True, linestyle='--', alpha=0.7)

st.pyplot(fig)

st.write(f"### 🗺️ Mapa de recorridos a las {hour}:00 horas")
if not filtered_data.empty:
    st.map(filtered_data[['lat', 'lon']])
else:
    st.write(f"No hay recorridos iniciados a las {hour}:00 horas.")

st.write("Fin del visor de CitiBike.")