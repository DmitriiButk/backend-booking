from pydantic import BaseModel, EmailStr, Field, StringConstraints, ConfigDict, field_serializer
from typing import List, Annotated, Optional
from datetime import datetime


class ReserveCreate(BaseModel):
    from_time: datetime = Field(..., alias='from', description='Начало резерва')
    to: datetime = Field(..., description='Конец резерва')
    name: Annotated[str, StringConstraints(min_length=1)] = Field(..., description='Имя гостя')
    phone: Annotated[Optional[str], StringConstraints(pattern=r"^7\d{10}$")] = Field(
        None, description='Телефон гостя в формате 7987654321')
    email: Optional[EmailStr] = Field(None, description='Почта гостя')
    count: Optional[int] = Field(None, description='Количество человек')
    text: Optional[str] = Field(None, description='Комментарий к резерву')
    source: Optional[str] = Field(None, description='Источник бронирования (домен)')
    item_ids: Optional[List[int]] = Field(None, description='ID бронируемого стола или столов')
    waitlist: Annotated[bool, Field(default=False, description='Заявка попадет в Лист ожидания')]
    deposit: Annotated[bool, Field(default=True, description='Учитывать депозит при бронировании')]

    model_config = ConfigDict(populate_by_name=True)

    @field_serializer('from_time')
    def serialize_from_time(self, value: datetime) -> str:
        return value.strftime('%Y-%m-%d %H:%M:%S')

    @field_serializer('to')
    def serialize_to(self, value: datetime) -> str:
        return value.strftime('%Y-%m-%d %H:%M:%S')
