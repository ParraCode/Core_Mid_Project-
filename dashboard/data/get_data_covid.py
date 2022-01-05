
# Aqui vamos a escribir funciones donde recoger los datos que queremos. las llamadas que hace streamlit a la api en forma de 
# funciones para recoger datos y luego jugar con ellos en los graficos 

import requests
from config.config_api import url 

def get_all_data_base():
    base_url = url+"/alldb"
    res = requests.get(base_url).json()
    return res

def get_all_data_base_TR(country):
    base_url = url+f"/alldb/{country}"
    res = requests.get(base_url).json()
    return res

def get_variant_db():
    base_url = url+"/variant"
    res = requests.get(base_url).json()
    return res

def get_variant_db_filtred(variants):
    base_url = url+f"/variant/{variants}"
    res = requests.get(base_url).json()
    return res


def get_list_continent():
    base_url = url+"/continent"
    res = requests.get(base_url).json()
    return res

def country_location():
    base_url = url+"/country/location"
    res = requests.get(base_url).json()
    return res

# Endpoint Numero 1
def get_list_countrys_of_continent(continent):
    base_url = url+f"/continent/{continent}"
    res = requests.get(base_url).json()
    return res

# Endpoint Numero 2
def get_data_confirmed_perd_day(contienent,country):
    base_url = url+f"/continent/{contienent}/{country}/confirmedDay"
    res = requests.get(base_url).json()
    return res

def get_data_confirmed_perd_week(contienent,country):
    base_url = url+f"/continent/{contienent}/{country}/DataWeek"
    res = requests.get(base_url).json()
    return res

def get_oneline():
    base_url = url+"/alldboneline"
    res = requests.get(base_url).json()
    return res

def get_data_one_country(country,var):
    base_url = url+f"/continent/{country}/{var}"
    res = requests.get(base_url).json()
    return res