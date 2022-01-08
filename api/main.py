
import os

from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
import sentry_sdk

from fastapi import FastAPI
from .routers import endpoints

# To run in shell:
# uvicorn api.main:app --reload

sentry_sdk.init(
    dsn=os.getenv('dns_sentry'),  # CHANGE HERE
    environment=os.getenv('ENV', 'dev'), # You should read it from environment variable
    )

app = FastAPI(
    title='My FastAPI App',
    description='Demo Sentry Integration',
    version='1.0.0',
)

try:
    app.add_middleware(SentryAsgiMiddleware)
except Exception:
    # pass silently if the Sentry integration failed
    pass

# Defino los router a mis archivo/s endopoint/s
app.include_router(endpoints.router)


# Mensaje para el root para saber en que consiste esta API
@app.get("/")
def root():
    return {"API":"Covid Data Core Code School"}

# Calling this endpoint to see if the setup works. If yes, an error message will show in Sentry dashboard
@app.get('/sentry')
async def sentry():
    raise Exception('Test sentry integration')