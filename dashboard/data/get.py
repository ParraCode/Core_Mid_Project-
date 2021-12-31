
# Aqui vamos a escribir funciones donde recoger los datos que queremos. 

import requests
from config.api import url

def get_all_country():
    return requests.get(url+"/country").json()

