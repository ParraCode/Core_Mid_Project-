
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

def covid():

  # ---------------------------------------------------------------------------------------------------------------------------------------
  # Configuracion de pagina 

  #st.set_page_config(page_title="Covid compare", layout="wide")

  # ---------------------------------------------------------------------------------------------------------------------------------------
  # Barra de menu 

  st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

  st.markdown("""
  <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #8ed3ac;">
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
  # Expander variables 

  with st.container():
      with st.expander("Guia variables"):
        st.write("""
            - icu_patients: Número de pacientes con COVID-19 en unidades de cuidados 
            intensivos (UCI) en un día determinado

            - hosp_patients: Número de pacientes con COVID-19 en el hospital en un día determinado

            - total_tests: Pruebas totales para COVID-19

            - positive_rate: La proporción de pruebas de COVID-19 que son positivas, expresada como un 
            promedio móvil de 7 días (esto es lo contrario de las pruebas por caso)

            - tests_per_case: Pruebas realizadas por cada nuevo caso confirmado de COVID-19, dado como un 
            promedio móvil de 7 días (esto es lo contrario de Positive_rate)

            - new_vaccinations: Nuevas dosis de vacuna COVID-19 administradas 
            (solo calculadas para días consecutivos)

            - people_vaccinated_per_hundred: Número total de personas que recibieron al menos una dosis 
            de vacuna por cada 100 personas en la población total

            - people_fully_vaccinated_per_hundred: Número total de personas que recibieron todas las dosis prescritas por el 
            protocolo de vacunación por cada 100 personas en la población total

            - population: poblacion total del pais
        """)


  # ---------------------------------------------------------------------------------------------------------------------------------------
  # Graficos 
  with st.container():
      col1, col2 = st.columns(2)

      ## Grafico 1 
      col1.header('Grafico 1')
      # Lista de variables
      var_list1 = lista_variables(get_oneline())
      # Selector de variable
      var_grafico1 = col1.selectbox('Selecciona la variable para el Grafico 1', var_list1)

      c2 = get_data_one_country(country_selected2,var_grafico1)
      c1 = get_data_one_country(country_selected1,var_grafico1)

      #data
      data_country1 = country_one_var_df(c1,var_grafico1,start_date,end_date)
      data_country2 = country_one_var_df(c2,var_grafico1,start_date,end_date)

      df_merge_country_1_2 = merge_country_data(data_country1,data_country2)

      # Meto el dataframe y ploteo 
      grafico_1 = col1.area_chart(data=df_merge_country_1_2, width=0, height=0, use_container_width=True)


      ## Grafico 2
      col2.header('Grafico 2')
      # Lista de variables
      var_list2 = lista_variables(get_oneline())
      var_list2.remove(var_grafico1)
      # Selector de variable
      var_grafico2 = col2.selectbox('Selecciona la variable para el Grafico 2', var_list2) # cambiar var_list2

      c3 = get_data_one_country(country_selected2,var_grafico2) # cambiar c3 # cambiar var_grafico2
      c4 = get_data_one_country(country_selected1,var_grafico2) # cambiar c4 # cambiar var_grafico2

      #data
      data_country3 = country_one_var_df(c3,var_grafico2,start_date,end_date)
      data_country4 = country_one_var_df(c4,var_grafico2,start_date,end_date)

      df_merge_country34 = merge_country_data(data_country3,data_country4)

      # Meto el dataframe y ploteo 
      grafico_2 = col2.area_chart(data=df_merge_country34, width=0, height=0, use_container_width=True)


      ## Grafico 3
      col1.header('Grafico 3')
      # Lista de variables
      var_list3 = lista_variables(get_oneline())
      var_list3.remove(var_grafico1)
      var_list3.remove(var_grafico2)
      # Selector de variable
      var_grafico3 = col1.selectbox('Selecciona la variable para el Grafico 3', var_list3) # cambiar var_list2

      c5 = get_data_one_country(country_selected2,var_grafico3) # cambiar c3 # cambiar var_grafico2
      c6 = get_data_one_country(country_selected1,var_grafico3) # cambiar c4 # cambiar var_grafico2

      #data
      data_country5 = country_one_var_df(c5,var_grafico3,start_date,end_date)
      data_country6 = country_one_var_df(c6,var_grafico3,start_date,end_date)

      df_merge_country56 = merge_country_data(data_country5,data_country6)

      # Meto el dataframe y ploteo 
      grafico_3 = col1.area_chart(data=df_merge_country56, width=0, height=0, use_container_width=True)


      ## Grafico 4
      col2.header('Grafico 4')
      # Lista de variables
      var_list4 = lista_variables(get_oneline())
      var_list4.remove(var_grafico1)
      var_list4.remove(var_grafico2)
      var_list4.remove(var_grafico3)
      # Selector de variable
      var_grafico4 = col2.selectbox('Selecciona la variable para el Grafico 4', var_list4) # cambiar var_list2

      c7 = get_data_one_country(country_selected2,var_grafico4) # cambiar c3 # cambiar var_grafico2
      c8 = get_data_one_country(country_selected1,var_grafico4) # cambiar c4 # cambiar var_grafico2

      #data
      data_country7 = country_one_var_df(c7,var_grafico4,start_date,end_date)
      data_country8 = country_one_var_df(c8,var_grafico4,start_date,end_date)

      df_merge_country78 = merge_country_data(data_country7,data_country8)

      # Meto el dataframe y ploteo 
      grafico_4 = col2.area_chart(data=df_merge_country78, width=0, height=0, use_container_width=True)