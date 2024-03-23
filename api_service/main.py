from fastapi import FastAPI

from api_service.api.v1 import v1_router

app = FastAPI()
app.include_router(v1_router)
