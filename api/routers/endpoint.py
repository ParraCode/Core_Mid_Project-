# Aqui defino los endopoints que van a ser todos los recursos de datos que voy a necesitar para hacer los graficos 
# que los pasare previamente por get_data.py para ahi hacer las request que pueda utilizar streamlit

# Consejo de Alvaro: puedo dividir los endopints en varios archvivos. Por ejmplo puedo usar este archivo solo 
# para los datos de data_core/ y otro para los endpoints que vaya a crear a partir de data_extra/, por ejemplo.  

from fastapi import APIRouter
from ..conect_database.conect_mongo import covid
from bson import json_util
from json import loads

router = APIRouter()

# Numero 1: Recoge una lista con todos los distintos paises de mi coleccion
@router.get("/country")
def get_list_country ():
    results = list(covid.find({}, {"country":1}).distinct("country"))
    return loads(json_util.dumps(results))


# Numero 2: Dado un pais, devuelve los casos confirmados y la decha de dichos casos
# Esta bien para hacer un grafico de lineas
@router.get("/country/{country}")
def get_country_data(country: str):
    results = list(covid.find({"country":country}, {'confirmed':1, 'recovered':1}))
    return loads(json_util.dumps(results.to_frame()))

