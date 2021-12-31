
# Consejo de Alvaro: para hacer el streamlit multipagina aqui solo hago referencia a las llamadas del los app = de los 
# diferentes Strealits y luego los juntos aqui para crear ese dashboard multipagina. 
# Tendria que crear un directorio que contuviese todas las paginas y que este al mismo nivel que este archivo 

import streamlit as st
from data.get_data import get_all_country , get_country_data

def fecha_int_transf (core_df):
    import pandas as pd
    core_df = pd.DataFrame(core_df, columns = ['_id','recovered','confirmed'])
    core_df = core_df.drop(['_id'], axis=1)
    #core_df['date'] = core_df['date'].apply(lambda x: list(x.values())[0][0:10])
    #core_df['date'] = pd.to_datetime(core_df['date'])
    #core_df['_id'] = core_df.index
    return core_df

st.title('Coviboard Core Core')

all_country =  get_all_country()
chosen_country = st.selectbox('Escoge el pais', all_country)


data_country = get_country_data(chosen_country)

st.line_chart(data=fecha_int_transf(data_country), 
width=0, height=0, use_container_width=True)