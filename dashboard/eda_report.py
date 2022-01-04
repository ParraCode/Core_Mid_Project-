
import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
from fpdf import FPDF
import base64
from tempfile import NamedTemporaryFile
from selenium import webdriver

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


st.sidebar.header('1. Escoja un Contienente:',None)

cotinent_selected = st.sidebar.selectbox('Selecciona tu continente',get_list_continent())

st.sidebar.header('2. Escoja un pais:',None)

    # Lista de paises, y elijo un pais 
list_countrys = get_list_countrys_of_continent(cotinent_selected)
country_selected = st.sidebar.selectbox('Selecciona un pais', list_countrys)


data = get_all_data_base_TR(country_selected)

if country_selected is not None:
#Pandas Profiling Report
    df = alldb(data)
    pr = ProfileReport(df, explorative=True)

    st.header('**Input DataFrame**')
    
    st.write('Puedes descargar este archivo en formato .csv')
    st.download_button(label='Dowload CSV',data = df.to_csv(), mime='text/csv')
    st.write(df)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    report = st_profile_report(pr)
        

