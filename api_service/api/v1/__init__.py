from fastapi import APIRouter

from api_service.api.v1.pastebin import router as pastebin_router

v1_router = APIRouter(prefix="/v1")

v1_router.include_router(pastebin_router, tags=["Pastebin"])
