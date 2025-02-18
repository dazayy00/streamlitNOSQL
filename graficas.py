import pandas as pd
import streamlit as st 
import matplotlib.pyplot as plt

titanic_link = 'titanic.csv'
titanic_data = pd.read_csv(titanic_link)

st.title('titanic app')
sidebar = st.sidebar

sidebar.image("perfil.png", width=150)
sidebar.write("**nombre:** Johan David Baltazar Trinidad")
sidebar.write("**matricula:** s21020562")

show_data = sidebar.checkbox("¿Mostrar DataFrame?")
if show_data:
    st.dataframe(titanic_data)

st.header("Data Description")


fig, ax = plt.subplots()
ax.hist(titanic_data.fare)
st.header("histograma del titanic")
st.pyplot(fig)

fig2, ax2 = plt.subplots()
y_pos = titanic_data['class']
x_pos = titanic_data['fare']

ax2.barh (y_pos, x_pos)
ax2.set_ylabel("Class")
ax2.set_xlabel("Fare")
ax2.set_title('¿cuanto pagaron las clases del titanic')

st.header("grafica de barras del titanic")
st.pyplot(fig2)

fig3, ax3 = plt.subplots()
ax3.scatter(titanic_data.age, titanic_data.fare)
ax3.set_xlabel("Edad")
ax3.set_ylabel("Tarifa")
st.header("Grafica de Dispersión del Titanic")
st.pyplot(fig3)