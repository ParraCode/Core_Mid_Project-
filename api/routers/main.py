from fastapi import APIRouter
from ..database.mongo import covid
from bson import json_util
from json import loads

router = APIRouter()


@router.get("/country")
def get_all_country():
    results = list(covid.find({}, {"country":1}).distinct("country"))
    return loads(json_util.dumps(results))


# devuelve todas las fechas para el pais que indiquemos
@router.get("/country/{country}")
def get_country(country: str):
    results = list(covid.find({"country":country}.distinct(), {"date":1,"_id":0}))
    return loads(json_util.dumps(results))