
from fastapi import APIRouter
from bson import json_util
from json import loads

from conect_database.conect_mongo import covid

router = APIRouter()

# -------------------------------------------------------------------------------------------------------------------------------------------------------
# Endpoint

# dashboard covid
@router.get("/alldbmap/{var}")
def get_all_db_map (var: str):
    results = list(covid.find({}, {"country":1,"population":1,f"{var}":1,"_id":0}))
    return loads(json_util.dumps(results))

# dashboard covid
@router.get("/alldboneline")
def get_oneline ():
    results = list(covid.find({'confirmedDay':0,'country': 'Spain'}, {"Year":0,"Month":0,"Week":0,
                                                                      "Day":0,"population":0,"_id":0}).distinct("confirmedDay"))
    return loads(json_util.dumps(results))

# dashboard EDA
@router.get("/alldb/{country}")
def get_all_db_country (country: str):
    results = list(covid.find({"country":country}, {"Year":0,"Month":0,"Week":0,"Day":0,"_id":0}))
    return loads(json_util.dumps(results))

# dashboard covid
# dashboard EDA
@router.get("/continent")
def get_list_continent ():
    results = list(covid.find({}, {"continent":1, "_id":0}).distinct("continent"))
    return loads(json_util.dumps(results))

# dashboard covid
# dashboard EDA
@router.get("/continent/{continent}")
def get_list_countrys_of_continent (continent: str):
    results = list(covid.find({"continent":continent}, {"country":1, "_id":0}).distinct("country"))
    return loads(json_util.dumps(results))

# dashboard covid
@router.get("/continent/{country}/{var}")
def get_data_one_var (country: str, var: str):
    results = list(covid.find({"country":country},{f"{var}":1, "country":country,"date":1, "_id":0}))
    return loads(json_util.dumps(results))