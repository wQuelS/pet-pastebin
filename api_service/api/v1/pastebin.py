from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert

from api_service.models.paste import Paste
from api_service.serializers.paste_schemas import PasteCreate, PasteView
from api_service.utils.dependencies.get_db import get_async_session


router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello, world! This is pastebin root router!"}


# TODO: reimplement proper get() logic
@router.get("/pastebins/{paste_id}", response_model=PasteView)
async def get_pastebin_details(
    paste_id: str, session: AsyncSession = Depends(get_async_session)
):
    query = select(Paste).where(Paste.id == int(paste_id))
    response = await session.execute(query)
    result = response.scalar()
    return result


# TODO: reimplement proper post() logic
@router.post("/pastebins", response_model=PasteView)
async def create_pastebin(
    item: PasteCreate, session: AsyncSession = Depends(get_async_session)
):
    query = insert(Paste).returning(Paste)
    paste_data = item.model_dump(by_alias=True)
    response = await session.execute(query, paste_data)
    await session.commit()
    result = response.scalar()

    return result
