# Cargo la base de datos de mongo via url de atlas
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
username = os.getenv("MONGO_USER")
password = os.getenv("MONGO_PASSWORD")

URL = f"mongodb+srv://{username}:{password}@parracode.p3gyj.mongodb.net"
db = MongoClient(URL).get_database("Covid19")

# saco la coleccion covid de mongo 
covid = db['CovidDB']

variant = db['VariantsDB']