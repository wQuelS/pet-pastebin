from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

from api_service.utils.enumerations import DestroyTimeEnum


class PasteCreate(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    title: str | None
    text: str = Field(alias="text_block")
    destruction_time: DestroyTimeEnum | None = None


class PasteView(PasteCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    views: int
