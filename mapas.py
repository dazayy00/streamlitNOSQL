import pandas as pd
import numpy as np
import streamlit as st

st.title('Maps app')
sidebar = st.sidebar

sidebar.image("perfil.png", width=150)
sidebar.write("**nombre:** Johan David Baltazar Trinidad")
sidebar.write("**matricula:** s21020562")

map_data = pd.DataFrame(
 np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
 columns=['lat', 'lon'])

st.title("San Francisco Map")
st.header("using streamlit and mapbox")

st.map(map_data)