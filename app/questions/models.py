from pydantic import BaseModel, Field
from datetime import datetime


class BaseQuestion(BaseModel):
    question_id: int = Field(alias="id")
    answer: str
    question: str
    created_at: datetime

    class Config:
        orm_mode = True
        allow_populate_by_alias = True
