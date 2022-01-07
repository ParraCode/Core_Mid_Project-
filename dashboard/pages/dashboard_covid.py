
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
import folium
from streamlit_folium import folium_static
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode
import datetime

# ---------------------------------------------------------------------------------------------------------------------------------------
# Funciones

from utils.process_data import *
from utils.process_map import *
from data.get_data_covid import *

def covid():

  # ---------------------------------------------------------------------------------------------------------------------------------------
  # Barra de menu 

  st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

  st.markdown("""
  <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #8ed3ac;">
    <a class="navbar-brand" href="https://www.linkedin.com/in/miguelangelparrarodriguez/" target="_blank">miguelangelparra.tech</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
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

  # ---------------------------------------------------------------------------------------------------------------------------------------
  # Mapa
  with st.container():

      ## Grafico 1 
      st.markdown("<h3 style='text-align:center'><b>Mapa Coropletico</b></h3>", unsafe_allow_html=True)

      # Lista de variables
      var_map_list = lista_variables(get_oneline())
      # Selector de variable
      var_map = st.selectbox('Selecciona la variable para el Mapa Coropletico', var_map_list)
      #Setting up the world countries data URL
      url = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data'
      country_shapes = f'{url}/world-countries.json'

      #llamada a funcion api que me todas las variables y el nombre del pais
      request_data_map = get_all_data_base_map(var_map)
      #funcion que dada esos datos me deje un dataset con nombre pais y el agregado de esa variable en una sola linea por un unico pais. 
      df_covid_map = country_one_var_df_map(request_data_map, var_map)

      #Creating a base map
      m = folium.Map()

      folium.Choropleth(
      #The GeoJSON data to represent the world country
      geo_data=country_shapes,
      name='choropleth COVID-19',
      data=df_covid_map,
      #The column aceppting list with 2 value; The country name and  the numerical value
      columns=['country', var_map],
      key_on='feature.properties.name',
      fill_color='YlOrRd',
      fill_opacity=0.7,
      line_opacity=1,
      nan_fill_color='white'
      ).add_to(m)

      # call to render Folium map in Streamlit
      folium_static(m,width=1120,height=450)

      data_table = get_all_data_base()
      shows = alldb(data_table)

      gb = GridOptionsBuilder.from_dataframe(shows)
      gb.configure_pagination()
      gb.configure_side_bar()
      gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc="sum", editable=True)
      gb.configure_selection(selection_mode="multiple", use_checkbox=True)
      gridOptions = gb.build()
      data_table = AgGrid(shows, gridOptions=gridOptions, 
                    enable_enterprise_modules=True, 
                    allow_unsafe_jscode=True, 
                    update_mode=GridUpdateMode.SELECTION_CHANGED)

