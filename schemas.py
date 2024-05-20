import datetime
from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str


class User(UserCreate):
    id: int
    created_at: datetime.datetime

    class Config:
        orm_mode = True
