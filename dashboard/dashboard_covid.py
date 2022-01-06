
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

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3498DB;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/miguelangelparrarodriguez/" target="_blank">Miguel A. Parra</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://www.linkedin.com/in/miguelangelparrarodriguez/" target="_blank">LinkeIn</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://github.com/ParraCode" target="_blank">GitHub</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------------------------------------------------------------------------
# Titulo

with st.container():
    st.markdown("<h1 style='text-align:center'><b>Covid Dashboard Information</b></h1>", unsafe_allow_html=True)
    st.write('---')
# ---------------------------------------------------------------------------------------------------------------------------------------
#Filters

with st.container():
    col1, col2, col3 = st.columns(3)
    ## Filter continent
    col1.header('1. Escoja un Contienente:',None)
    cotinent_selected = col1.selectbox('Selecciona tu continente',get_list_continent())

    ## Filter country
    col2.header('2. Escoja dos paises:',None)
      # Lista de paises 1, y elijo un pais 
    list_countrys1 = get_list_countrys_of_continent(cotinent_selected)
    country_selected1 = col2.selectbox('Selecciona tu primer pais', list_countrys1)
      # Lista de paises 2, y elijo un pais 
    list_countrys2 = get_list_countrys_of_continent(cotinent_selected)
    list_countrys2.remove(country_selected1)
    country_selected2 = col2.selectbox('Selecciona tu segundo pais', list_countrys2)

    ## Filter time
    col3.header('3. Escoja un periodo:',None)
    start_date = col3.date_input('Start date', datetime.date(2020, 1, 23), min_value=datetime.date(2020, 1, 23), max_value=datetime.date(2021, 12, 30))
    end_date = col3.date_input('End date', datetime.date(2021, 12, 31), min_value=datetime.date(2020, 1, 24), max_value=datetime.date(2021, 12, 31))

    st.write('---')
# ---------------------------------------------------------------------------------------------------------------------------------------
# Graficos 
with st.container():
    col1, col2, col3 = st.columns(3)

    ## Grafico 1 
    col1.header('Grafico 1')
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
    grafico_1 = col1.area_chart(data=df_merge_country_1_2, width=0, height=0, use_container_width=True)