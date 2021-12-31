from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
username = os.getenv("MONGO_USER")
password = os.getenv("MONGO_PASSWORD")
URL = f"mongodb+srv://{username}:{password}@parracode.p3gyj.mongodb.net"
db = MongoClient(URL).get_database("parracode_mid_project")
covid = db['covid']