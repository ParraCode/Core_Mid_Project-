import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pydeck as pdk

from utils.process_data import *
from data.get_data_covid import *

def variant ():

  st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

  st.markdown("""
  <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3498DB;">
    <a class="navbar-brand" href="https://www.linkedin.com/in/miguelangelparrarodriguez/" target="_blank">Miguel A. Parra</a>
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

  with st.container():
      col1, col2 = st.columns(2)

      col1.header('1. Escoja un Contienente:',None)

      cotinent_selected = col1.selectbox('Selecciona tu continente',get_list_continent())

      col2.header('2. Escoja un pais:',None)

          # Lista de paises, y elijo un pais 
      list_countrys = get_list_countrys_of_continent(cotinent_selected)
      country_selected = col2.selectbox('Selecciona un pais', list_countrys)

  # ---------------------------------------------------------------------------------------------------------------------------------------
  #VARIANTES
  with st.container():

    db_variant = get_variant_db()

    variant_list = variant_TR (db_variant)

    variants_selected = st.selectbox('Selecciona las variantes', variant_list)

    data_select_variant = variants_map(get_variant_db(),variants_selected)
    # print(data_select_variant)
        # Mapa 
    #st.map(data_select_variant)

    # ---------------------------------------------------------------------------------------------------------------------------------------
 
    # st.pydeck_chart(pdk.Deck(
    #     map_style='mapbox://styles/mapbox/light-v9',
    #     initial_view_state=pdk.ViewState(
    #         latitude=37.76,
    #         longitude=-122.4,
    #         zoom=11,
    #         pitch=50,
    #     ),
    #     layers=[
    #         pdk.Layer(
    #             'HexagonLayer',
    #             data=data_select_variant,
    #             get_position='[lon lat]',
    #             radius=2000,
    #             elevation_scale=9,
    #             elevation_range=[0, 1000],
    #             pickable=True,
    #             extruded=True,
    #         ),
    #         pdk.Layer(
    #             'ScatterplotLayer',
    #             data=data_select_variant,
    #             get_position='[lon, lat]',
    #             get_color='[200, 30, 0, 160]',
    #             get_radius=2000,
    #         ),
    #     ],
    # ))