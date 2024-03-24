from sqlalchemy import exc

from api_service.core.database import db_helper


async def get_async_session():
    async with db_helper.session_factory() as session:
        try:
            yield session
        except exc.SQLAlchemyError as error:
            await session.rollback()
            raise error
        finally:
            await session.close()
