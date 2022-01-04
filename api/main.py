
# Desde este archivo creo la api que sustenta al resto del pryecto. 
# Este el archivo que voy a llamar desde consola y que pone a funcionar el resto de directorios de api/

from fastapi import FastAPI
from .routers import endpoints

# To run in shell:
# uvicorn api.main:app --reload

app = FastAPI()

# Defino los router a mis archivo/s endopoint/s
app.include_router(endpoints.router)


# Mensaje para el root para saber en que consiste esta API
@app.get("/")
def root():
    return {"API":"Covid Data Core Code School"}

