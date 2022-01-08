
from fastapi import APIRouter
from ..conect_database.conect_mongo import covid, variant
from bson import json_util
from json import loads

router = APIRouter()

# -------------------------------------------------------------------------------------------------------------------------------------------------------
# COVID
 
@router.get("/alldb")
def get_all_db ():
    results = list(covid.find({}, {"date":1,"continent":1,"country":1,"totalConfirmed":1,"totalDeaths":1,"deathsDay":1,"confirmedDay":1,"icuPatients":1,
                                   "hospPatients":1,"totalTest":1,"positiveRate":1,"testPerCase":1,"newVaccinations":1,
                                   "vaccinatedPerHundred":1,"fullyVaccinatedPerHundred":1,"_id":0}))
    return loads(json_util.dumps(results))

@router.get("/alldbmap/{var}")
def get_all_db_map (var: str):
    results = list(covid.find({}, {"country":1,"population":1,f"{var}":1,"_id":0}))
    return loads(json_util.dumps(results))

@router.get("/alldboneline")
def get_oneline ():
    results = list(covid.find({'country': 'Spain'}, {"population":0,"_id":0}))
    return loads(json_util.dumps(results))

@router.get("/alldb/{country}")
def get_all_db_country (country: str):
    results = list(covid.find({"country":country}, {"date":1,"continent":1,"country":1,"totalConfirmed":1,"totalDeaths":1,"deathsDay":1,"confirmedDay":1,"icuPatients":1,
                                   "hospPatients":1,"totalTest":1,"positiveRate":1,"testPerCase":1,"newVaccinations":1,
                                   "vaccinatedPerHundred":1,"fullyVaccinatedPerHundred":1,"icuPatients":1,"_id":0}))
    return loads(json_util.dumps(results))

@router.get("/continent")
def get_list_continent ():
    results = list(covid.find({}, {"continent":1, "_id":0}).distinct("continent"))
    return loads(json_util.dumps(results))

@router.get("/country/location")
def country_location ():
    results = list(covid.find({"continent":"Europe"},{"longitude":1,"latitude":1, "country":1,"_id":0}))
    return loads(json_util.dumps(results))

@router.get("/continent/{continent}")
def get_list_countrys_of_continent (continent: str):
    results = list(covid.find({"continent":continent}, {"country":1, "_id":0}).distinct("country"))
    return loads(json_util.dumps(results))

@router.get("/continent/{country}/{var}")
def get_data_one_var (country: str, var: str):
    results = list(covid.find({"country":country},{f"{var}":1, "country":country,"date":1, "_id":0}))
    return loads(json_util.dumps(results))

# -------------------------------------------------------------------------------------------------------------------------------------------------------
# VARIANT

@router.get("/variant/{variants}")
def get_variant_data_location (variants: str):
    results = list(variant.find({"variant":variants}, {"date":1, "country":1, "variant":1, "latitude":1,
                                                      "longitude":1,"continentExp":1,"_id":0}))
    return loads(json_util.dumps(results))

@router.get("/variant")
def get_variants_db ():
    results = list(variant.find({}, {"country":1, "variant":1, "longitude":1,"latitude":1,
                                    "_id":0}))
    return loads(json_util.dumps(results))