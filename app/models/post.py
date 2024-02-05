from models.base import BaseModel
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import TEXT
from sqlmodel import Field


class Post(BaseModel, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)
    title: str = Field(sa_column_kwargs={"unique": True, "index": True})
    slug: str = Field(sa_column_kwargs={"unique": True, "index": True})
    content: str = Field(sa_column=Column(TEXT, nullable=False, default=""))
