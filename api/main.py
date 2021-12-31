from fastapi import FastAPI
from .routers import main

# To run in shell:
 # uvicorn api.main:app --reload

app = FastAPI()

app.include_router(main.router)

@app.get("/")
def root():
    return {"Hello":"world"}

