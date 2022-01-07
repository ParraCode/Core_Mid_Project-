
import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from st_aggrid.shared import JsCode
from st_aggrid.shared import GridUpdateMode
import plotly_express as px



from utils.process_data import *
from data.get_data_covid import *

def eda ():

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

  with st.container():

    col1, col2 = st.columns(2)

    col1.header('1. Escoja un Contienente:',None)

    cotinent_selected = col1.selectbox('Selecciona tu continente',get_list_continent())

    col2.header('2. Escoja un pais:',None)

        # Lista de paises, y elijo un pais 
    list_countrys = get_list_countrys_of_continent(cotinent_selected)
    country_selected = col2.selectbox('Selecciona un pais', list_countrys)


    data = get_all_data_base_TR(country_selected)

    if country_selected is not None:
        df = alldb(data)
        pr = ProfileReport(df, explorative=True)

        st.header('**Input DataFrame**')

        shows = alldb(data)
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
        st.write('Puedes descargar este archivo en formato .csv')
        st.download_button(label='Download CSV',data = df.to_csv(), mime='text/csv')
        
        
        #st.write(df)
        st.write('---')
        st.header('**Pandas Profiling Report**')
        report = st_profile_report(pr)
