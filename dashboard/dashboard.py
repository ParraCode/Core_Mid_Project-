
# Consejo de Alvaro: para hacer el streamlit multipagina aqui solo hago referencia a las llamadas del los app = de los 
# diferentes Strealits y luego los juntos aqui para crear ese dashboard multipagina. 
# Tendria que crear un directorio que contuviese todas las paginas y que este al mismo nivel que este archivo 

# streamlit run dashboard/dashboard.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from utils.process_data import covid_cases_graph, fecha_int_transf

from data.get_data import get_list_country_of_countrys, get_one_europe_cuntry, get_data_confirmed_perd_day


st.title('Coviboard Core Core')

# Lista de paises, y elijo un pais 
list_countrys = get_list_country_of_countrys()

country_selected = st.sidebar.selectbox('Select your Contienent:', list_countrys)

# Dado el pais anterior obtengo los datos de confirmados para ese pais 
data_confirmed = get_data_confirmed_perd_day(country_selected)

#  Proceso el json y lo hago dataframe 
df_country = fecha_int_transf(data_confirmed)

# Meto el dataframe y ploteo 
st.line_chart(data=df_country, width=0, height=0, use_container_width=True)


print(list_countrys, type(list_countrys))
print(country_selected, type(country_selected))
print(data_confirmed, type(data_confirmed))
print(df_country, type(df_country))