
# Consejo de Alvaro: para hacer el streamlit multipagina aqui solo hago referencia a las llamadas del los app = de los 
# diferentes Strealits y luego los juntos aqui para crear ese dashboard multipagina. 
# Tendria que crear un directorio que contuviese todas las paginas y que este al mismo nivel que este archivo 

# streamlit run dashboard/dashboard.py

# ---------------------------------------------------------------------------------------------------------------------------------------
# Librerias

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pydeck as pdk
import datetime

# ---------------------------------------------------------------------------------------------------------------------------------------
# Funciones

from utils.process_data import *
from data.get_data_covid import *

# ---------------------------------------------------------------------------------------------------------------------------------------
# Configuracion de pagina 

st.set_page_config(page_title="Covid compare", layout="wide")

# ---------------------------------------------------------------------------------------------------------------------------------------
# Barra de menu 

# ---------------------------------------------------------------------------------------------------------------------------------------
# Division en columnas 

col1, col2= st.columns(2)

# ---------------------------------------------------------------------------------------------------------------------------------------
# Titulo
st.sidebar.title('**Covid-19 Countr Comparations**')
st.markdown("<h1 style='text-align:center'><b>Covid Dashboard Information</b></h1>", unsafe_allow_html=True)


# ---------------------------------------------------------------------------------------------------------------------------------------
# SideBar 

st.sidebar.header('1. Escoja un Contienente:',None)

cotinent_selected = st.sidebar.selectbox('Selecciona tu continente',get_list_continent())

st.sidebar.header('2. Escoja dos paises:',None)

# Lista de paises 1, y elijo un pais 
list_countrys1 = get_list_countrys_of_continent(cotinent_selected)
country_selected1 = st.sidebar.selectbox('Selecciona tu primer pais', list_countrys1)

# Lista de paises 2, y elijo un pais 
list_countrys2 = get_list_countrys_of_continent(cotinent_selected)
list_countrys2.remove(country_selected1)

country_selected2 = st.sidebar.selectbox('Selecciona tu segundo pais', list_countrys2)

st.sidebar.header('3. Escoja un periodo:',None)


start_date = st.date_input('Start date', datetime.date(2020, 1, 23), min_value=datetime.date(2020, 1, 23), max_value=datetime.date(2021, 12, 30))
end_date = st.date_input('End date', datetime.date(2021, 12, 31), min_value=datetime.date(2020, 1, 24), max_value=datetime.date(2021, 12, 31))
# ---------------------------------------------------------------------------------------------------------------------------------------
# Graficos 

## Grafico 1 
# Lista de variables
var_list = lista_variables(get_oneline())
# Selector de variable
var_grafico1 = col1.selectbox('Selecciona la variable para el Grafico 1', var_list)

c2 = get_data_one_country(country_selected2,var_grafico1)
c1 = get_data_one_country(country_selected1,var_grafico1)

#data
data_country1 = country_one_var_df(c1,var_grafico1,start_date,end_date)
data_country2 = country_one_var_df(c2,var_grafico1,start_date,end_date)

df_merge_country_1_2 = merge_country_data(data_country1,data_country2)

# Meto el dataframe y ploteo 
grafico_1 = col1.line_chart(data=df_merge_country_1_2, width=0, height=0, use_container_width=True)