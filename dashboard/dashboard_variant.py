import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pydeck as pdk

from utils.process_data import *
from data.get_data_covid import *

st.set_page_config(page_title="CovidDB Download", layout="wide") 


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


st.sidebar.header('1. Escoja un Contienente:',None)

cotinent_selected = st.sidebar.selectbox('Selecciona tu continente',get_list_continent())

st.sidebar.header('2. Escoja un pais:',None)

    # Lista de paises, y elijo un pais 
list_countrys = get_list_countrys_of_continent(cotinent_selected)
country_selected = st.sidebar.selectbox('Selecciona un pais', list_countrys)


data = get_all_data_base_TR(country_selected)

st.title("Analysis of Covid-19's variants")

# ---------------------------------------------------------------------------------------------------------------------------------------
#VARIANTES

data_variant = get_variant_db()

variant_list = variant_TR (data_variant)


variants_selected = st.multiselect('Selecciona las variantes', variant_list, default='Delta')

    # Mapa 
country_loc = country_location_coord(country_location())
st.map(country_loc)

# ---------------------------------------------------------------------------------------------------------------------------------------
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.pydeck_chart(pdk.Deck(
     map_style='mapbox://styles/mapbox/light-v9',
     initial_view_state=pdk.ViewState(
         latitude=37.76,
         longitude=-122.4,
         zoom=11,
         pitch=50,
     ),
     layers=[
         pdk.Layer(
            'HexagonLayer',
            data=df,
            get_position='[lon, lat]',
            radius=200,
            elevation_scale=5,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
         ),
         pdk.Layer(
             'ScatterplotLayer',
             data=df,
             get_position='[lon, lat]',
             get_color='[200, 30, 0, 160]',
             get_radius=200,
         ),
     ],
 ))
