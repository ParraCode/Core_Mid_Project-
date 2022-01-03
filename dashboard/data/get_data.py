
# Aqui vamos a escribir funciones donde recoger los datos que queremos. las llamadas que hace streamlit a la api en forma de 
# funciones para recoger datos y luego jugar con ellos en los graficos 

import requests
from config.config_api import url 

# Endpoint Numero 1
def get_list_country_of_countrys():
    base_url = url+f"/continent/Europe"
    res = requests.get(base_url).json()
    return res


def get_one_europe_cuntry(country):
    base_url = url+f"/continent/Europe/{country}"
    res = requests.get(base_url).json()
    return res


# Endpoint Numero 2
def get_data_confirmed_perd_day(country):
    base_url = url+f"/continent/Europe/{country}/confirmedDay"
    res = requests.get(base_url).json()
    return res
