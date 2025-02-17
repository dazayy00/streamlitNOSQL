import streamlit as st
st.title ("App side bar")

sidebar = st.sidebar
sidebar.title("esta es la barra lateral")

sidebar.write("aqui van los elementos de entrada")

st.header("informacion sobre el conjunto de datos")
st.header("descripcion de los datos")

st.write("""
         este es un simple ejemplo de una app para predecir 

         ¡esta app predice mis datos!

         """)   
