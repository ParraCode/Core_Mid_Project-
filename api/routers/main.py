from fastapi import APIRouter
from ..database.mongo import covid
from bson import json_util
from json import loads

router = APIRouter()


@router.get("/country/{country}")
def get_country(country: str):
    results = list(covid.find({"country":country}))
    return loads(json_util.dumps(results))