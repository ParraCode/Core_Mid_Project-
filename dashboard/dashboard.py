
# Consejo de Alvaro: para hacer el streamlit multipagina aqui solo hago referencia a las llamadas del los app = de los 
# diferentes Strealits y luego los juntos aqui para crear ese dashboard multipagina. 
# Tendria que crear un directorio que contuviese todas las paginas y que este al mismo nivel que este archivo 

# streamlit run dashboard/dashboard.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from utils.process_data import *

from data.get_data import *

# ---------------------------------------------------------------------------------------------------------------------------------------
st.set_page_config(page_title="Compare Shows", layout="wide") 

# Division en columnas 

col1, col2= st.columns(2)

# ---------------------------------------------------------------------------------------------------------------------------------------

# Titulo

col1.title('Core Code')

# ---------------------------------------------------------------------------------------------------------------------------------------

# Side Bar 
st.sidebar.header('1. Escoja un Contienente:',None)

list_contients = get_list_continent()
cotinent_selected = st.sidebar.selectbox('Selecciona tu continente',get_list_continent())

st.sidebar.header('2. Escoja dos paises:',None)

# Lista de paises, y elijo un pais 
list_countrys1 = get_list_countrys_of_continent(cotinent_selected)
country_selected1 = st.sidebar.selectbox('Selecciona tu primer pais', list_countrys1)

# Lista de paises, y elijo un pais 
list_countrys2 = get_list_countrys_of_continent(cotinent_selected)
country_selected2 = st.sidebar.selectbox('Selecciona tu segundo pais', list_countrys2)

st.sidebar.header('3. Escoja un periodo:',None)


st.sidebar.date_input('Fecha inicial', value=None, min_value=None, max_value=None, key=None, help=None, on_change=None, args=None, kwargs=None)

st.sidebar.date_input('Fecha final', value=None, min_value=None, max_value=None, key=None, help=None, on_change=None, args=None, kwargs=None)


# ---------------------------------------------------------------------------------------------------------------------------------------


# Dado el pais anterior obtengo los datos de confirmados para ese pais 
data_confirmed = get_data_confirmed_perd_day(cotinent_selected,country_selected1)

#  Proceso el json y lo hago dataframe 
df_country = fechaDay_int_transf(data_confirmed)

# Meto el dataframe y ploteo 
col1.line_chart(data=df_country, width=0, height=0, use_container_width=True)


#st.metric('label', df_country.max(), delta=None, delta_color="normal")

