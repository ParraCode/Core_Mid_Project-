
# Consejo de Alvaro: para hacer el streamlit multipagina aqui solo hago referencia a las llamadas del los app = de los 
# diferentes Strealits y luego los juntos aqui para crear ese dashboard multipagina. 
# Tendria que crear un directorio que contuviese todas las paginas y que este al mismo nivel que este archivo 

import streamlit as st
from dashboard.data.get_data import get_all_country, get_country_data

st.title('Coviboard Core Core')

all_country =  get_all_country()
chosen_country = st.selectbox('Escoge los paieses', all_country)

#st.line_chart(data=None, width=0, height=0, use_container_width=True)

#get_country_data(chosen_country)