
# Consejo de Alvaro: para hacer el streamlit multipagina aqui solo hago referencia a las llamadas del los app = de los 
# diferentes Strealits y luego los juntos aqui para crear ese dashboard multipagina. 
# Tendria que crear un directorio que contuviese todas las paginas y que este al mismo nivel que este archivo 

# streamlit run dashboard/dashboard.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from st_aggrid.shared import JsCode
from st_aggrid.shared import GridUpdateMode
import plotly_express as px

from utils.process_data import *

from data.get_data_covid import *

st.set_page_config(page_title="Covid compare", layout="wide") 

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
#st.set_page_config(page_title="Compare Shows", layout="wide") 

    # Division en columnas 

col1, col2= st.columns(2)

    # ---------------------------------------------------------------------------------------------------------------------------------------

    # Titulo

col1.title('Core Code')

    # ---------------------------------------------------------------------------------------------------------------------------------------

    # Side Bar 
st.sidebar.header('1. Escoja un Contienente:',None)

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


    # Mapa 
country_loc = country_location_coord(country_location())
st.map(country_loc)

# ---------------------------------------------------------------------------------------------------------------------------------------

st.title("Covid DB shows analysis")

shows = pd.read_csv("../data/CovidDB.csv")

# add this
gb = GridOptionsBuilder.from_dataframe(shows)

gb.configure_pagination()
gb.configure_side_bar()
gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc="sum", editable=True)
gb.configure_selection(selection_mode="multiple", use_checkbox=True)

gridOptions = gb.build()

data = AgGrid(shows, 
              gridOptions=gridOptions, 
              enable_enterprise_modules=True, 
              allow_unsafe_jscode=True, 
              update_mode=GridUpdateMode.SELECTION_CHANGED)
st.download_button(label='Dowload CSV',data = shows.to_csv(), mime='text/csv')