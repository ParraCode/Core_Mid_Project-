import requests
from config.config_api import url 

def get_variant_db():
    base_url = url+"/variant"
    res = requests.get(base_url).json()
    return res

def get_variant_db_filtred(variants):
    base_url = url+f"/variant/{variants}"
    res = requests.get(base_url).json()
    return res