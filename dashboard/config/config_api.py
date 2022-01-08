# Cargo la url de la API desde el archivo .env

from dotenv import load_dotenv
import os

load_dotenv()
url = os.getenv("url")
