import pandas as pd
import streamlit as st
import datetime

titanic_link = 'titanic.csv'
titanic_data = pd.read_csv(titanic_link)

st.title('titanic app')
sidebar = st.sidebar

today = datetime.date.today()
today_date = st.date_input('input date', today)
st.success('current date: `%s`' % (today_date))

agree = sidebar.checkbox("show dataset overview ?")
if agree:
    st.dataframe(titanic_data)

selected_town      =    sidebar.radio("select      embark        town",
titanic_data['embark_town'].unique())
st.write("selected embark town:", selected_town)
