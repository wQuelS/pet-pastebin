from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from typing import Any

from api_service.core.config import settings

engine = create_async_engine(
    settings.db.DATABASE_URI,
    echo=settings.echo,
    future=settings.future,
    pool_size=settings.pool_size,
    max_overflow=settings.max_overflow,
)

async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=settings.expire_on_commit
)

Base: Any = declarative_base()
