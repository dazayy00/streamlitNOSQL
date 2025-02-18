import pandas as pd
import streamlit as st
import datetime

titanic_link = 'titanic.csv'
titanic_data = pd.read_csv(titanic_link)

st.title('titanic app')
sidebar = st.sidebar

sidebar.image("perfil.png", width=150)
sidebar.write("**nombre:** Johan David Baltazar Trinidad")
sidebar.write("**matricula:** s21020562")

today = datetime.date.today()
today_date = st.date_input('input date', today)
st.success('current date: `%s`' % (today_date))

agree = sidebar.checkbox("show dataset overview ?")
if agree:
    st.dataframe(titanic_data)

selected_town      =    sidebar.radio("select      embark        town",
titanic_data['embark_town'].unique())
st.write("selected embark town:", selected_town)

optionals = st.expander("Optional Configurations", True)
fare_min = optionals.slider(
        "Minimun Fare",
        min_value=float(titanic_data['fare'].min()),
        max_value=float(titanic_data['fare'].max())
        )
fare_max = optionals.slider(
        "Maximun Fare",
        min_value=float(titanic_data['fare'].min()),
        max_value=float(titanic_data['fare'].max())
        )
subset_fare = titanic_data[(titanic_data['fare'] <= fare_max) &
                           (fare_min <=titanic_data['fare'])]
