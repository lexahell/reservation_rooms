from typing import Optional
from pydantic import BaseModel, Field, validator

class MeetingRoom(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=100)
    description: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "name": "Переговорная комната #1",
                "description": "Просторная комната на 40 человек. "
                "Есть флипчарт, проектор, кофемашина.",
            }
        }

class MeetingRoomCreate(MeetingRoom):
    name: str = Field(..., min_length=2, max_length=100)

    @validator("name")
    def name_is_numeric(cls, value: str):
        if value.isnumeric():
            raise ValueError("Имя не может быть числом")
        return value

class MeetingRoomDB(MeetingRoomCreate):
    id: int
    class Config:
        orm_mode = True


class MeetingRoomUpdate(MeetingRoom):
    @validator("name")
    def name_cannot_be_null(cls, value):
        if value is None:
            raise ValueError("Имя переговорки не может быть пустым")
        return value
