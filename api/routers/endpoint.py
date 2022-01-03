# Aqui defino los endopoints que van a ser todos los recursos de datos que voy a necesitar para hacer los graficos 
# que los pasare previamente por get_data.py para ahi hacer las request que pueda utilizar streamlit

# Consejo de Alvaro: puedo dividir los endopints en varios archvivos. Por ejmplo puedo usar este archivo solo 
# para los datos de data_core/ y otro para los endpoints que vaya a crear a partir de data_extra/, por ejemplo.  

from fastapi import APIRouter
from ..conect_database.conect_mongo import covid
from bson import json_util
from json import loads

router = APIRouter()


# No se usa
@router.get("/continent")
def get_list_continent ():
    results = list(covid.find({}, {"continent":1, "_id":0}).distinct("continent"))
    return loads(json_util.dumps(results))

# No se
@router.get("/continent/{continent}")
def get_list_countrys_of_continent (continent: str):
    results = list(covid.find({"continent":continent}, {"country":1, "_id":0}).distinct("country"))
    return loads(json_util.dumps(results))


@router.get("/continent/{continent}/{country}/confirmedDay")
def get_data_confirmed_perd_day (continent: str,country: str):
    results = list(covid.find({"continent":continent, "country":country},{"totalConfirmed":1,"totalDeaths":1, "date":1, "_id":0}))
    return loads(json_util.dumps(results))

@router.get("/continent/{continent}/{country}/DataWeek")
def get_data_confirmed_perd_week (continent: str,country: str):
    results = list(covid.find({"continent":continent, "country":country},{"confirmed":1,"deaths":1, "Year-Week":1, "date":1,"_id":0}))
    return loads(json_util.dumps(results))