import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

from utils.process_data import *
from data.get_data_covid import *

st.sidebar.header('1. Escoja un Contienente:',None)

cotinent_selected = st.sidebar.selectbox('Selecciona tu continente',get_list_continent())

st.sidebar.header('2. Escoja un pais:',None)

    # Lista de paises, y elijo un pais 
list_countrys = get_list_countrys_of_continent(cotinent_selected)
country_selected = st.sidebar.selectbox('Selecciona un pais', list_countrys)

data = get_all_data_base_TR(country_selected)


if country_selected is not None:
    # Pandas Profiling Report
    df = alldb(data)
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr)
