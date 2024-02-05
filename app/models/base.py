from datetime import datetime

from sqlalchemy import Column, DateTime, func, text
from sqlmodel import Field, SQLModel


class BaseModel(SQLModel):
    created: datetime = Field(
        sa_column_kwargs={
            "server_default": text("CURRENT_TIMESTAMP"),
        }
    )
    updated: datetime | None = Field(sa_column=Column(DateTime(), onupdate=func.now()))
