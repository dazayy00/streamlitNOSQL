import streamlit as st
import pandas as pd

st.title("Visor de Películas")

sidebar = st.sidebar
sidebar.image("perfil.png", width=150)
sidebar.write("**nombre:** Johan David Baltazar Trinidad")
sidebar.write("**matricula:** s21020562")

@st.cache_data
def load_data(nrows=None):
    """Carga el dataset de películas y devuelve un DataFrame con el número de registros solicitados."""
    try:
        data = pd.read_csv("movies.csv", nrows=nrows, encoding="ISO-8859-1")
        if nrows:
            return data.head(nrows)
        return data
    except FileNotFoundError:
        st.error("El archivo 'movies.csv' no se encontró. Verifica la ruta.")
        return pd.DataFrame()
    except UnicodeDecodeError:
        st.error("Error de decodificación. Verifica la codificación del archivo CSV.")
        return pd.DataFrame()


num_movies = st.number_input("Número de películas a mostrar:", min_value=1, value=500)

st.write(f"Cargando {num_movies} registros del dataset de películas...")
movies_data = load_data(num_movies)
movies_data_all = load_data()

if not movies_data.empty:
    st.write(f"___")
else:
    st.write("No se pudieron cargar datos. Verifica el archivo 'movies.csv'.")

agree = sidebar.checkbox("Mostrar Todo")

name = sidebar.text_input("Nombre de la pelicula:")
name_button = sidebar.button("Buscar")

if agree:
    st.write("Cargando todos los registros...")
    movies_data = load_data(None)
    st.write(f"Se cargaron {len(movies_data)} registros en total.")
else:
    movies_data = load_data(num_movies)
    st.write(f"Se cargaron {len(movies_data)} registros.")

if not movies_data.empty:
    st.dataframe(movies_data)
else:
    st.write("No se pudieron cargar datos. Verifica el archivo 'movies.csv'.")


if name_button:
    if name:
        filtered_data = movies_data[
            movies_data["name"].str.contains(name, case=False, na=False)
        ]
        st.write(f"Mostrando nombres entre **{name}** y {name}")
        st.dataframe(filtered_data)
    else:
        st.warning("Por favor, ingresa otro nombre.")

if not movies_data.empty:
    unique_directors = sorted(movies_data["director"].dropna().unique())
    selected_director = sidebar.selectbox("Selecciona un director:", unique_directors)

    if sidebar.button("Filtrar por Director"):
        filtered_data = movies_data[movies_data["director"] == selected_director]
        st.write(f"Películas dirigidas por: **{selected_director}**")
        st.dataframe(filtered_data)
else:
    st.write("No se pudieron cargar los datos. Verifica el archivo 'movies.csv'.")


st.write("Fin del visor de películas.")