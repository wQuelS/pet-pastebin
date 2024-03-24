from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy import Text, Enum, String, Integer, text

from .base import Base
from api_service.utils.enumerations import DestroyTimeEnum


class Paste(Base):
    title: Mapped[str] = mapped_column(String(65), nullable=True)
    text_block: Mapped[str] = mapped_column(Text, nullable=True)
    destruction_time: Mapped[DestroyTimeEnum] = mapped_column(
        ENUM(DestroyTimeEnum, name="destructs_enum"), nullable=False, server_default=DestroyTimeEnum.DEFAULT.value
    )
    views: Mapped[int] = mapped_column(Integer, nullable=False, server_default=text("0"))
