import streamlit as st
import pandas as pd

names_link = 'dataset.csv'
names_data = pd.read_csv(names_link)

st.title('Names Dataset')
sidebar = st.sidebar

sidebar.image("perfil.png", width=150)
sidebar.write("**nombre:** Johan David Baltazar Trinidad")
sidebar.write("**matricula:** s21020562")

st.dataframe(names_data)

sidebar = st.sidebar
sidebar.header('Filtros de búsqueda')

start_initial = sidebar.text_input('Inicial del nombre de inicio (A-Z)', 'A').upper()
end_initial = sidebar.text_input('Inicial del nombre de fin (A-Z)', 'B').upper()

gender = sidebar.selectbox('Género', ['Todos', 'M', 'F'])

index_number = sidebar.text_input('Número exacto del índice (por ejemplo, 2, 20, 203)', '')

filtered_data = names_data

if start_initial and end_initial:
    if start_initial.isalpha() and end_initial.isalpha():
        filtered_data = filtered_data[filtered_data['name'].str[0].between(start_initial, end_initial)]

if gender != 'Todos':
    filtered_data = filtered_data[filtered_data['sex'] == gender]

if index_number:
    index_list = [int(num) for num in index_number.split(',')]
    filtered_data = filtered_data[filtered_data['index'].isin(index_list)]

st.dataframe(filtered_data)
