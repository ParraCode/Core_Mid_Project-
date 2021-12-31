
# Aqui vamos a escribir funciones donde recoger los datos que queremos. las llamadas que hace streamlit a la api en forma de 
# funciones para recoger datos y luego jugar con ellos en los graficos 

import requests
from config.config_api import url 

# Endpoint Numero 1
def get_all_country():
    return requests.get(url+"/country").json()

# Endpoint Numero 2
def get_country_data(country):
    return requests.get(url+"/country/{country}").json()

