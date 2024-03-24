from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from api_service.core.config import settings


class DatabaseHelper:
    def __init__(self, url: str, echo: bool, **kwargs) -> None:
        self.engine = create_async_engine(url=url, echo=echo, **kwargs)

        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )


db_helper = DatabaseHelper(
    url=settings.db.DATABASE_URI,
    echo=settings.echo,
    future=settings.future,
    pool_size=settings.pool_size,
    max_overflow=settings.max_overflow
)
