import httpx
from fastapi import Depends
from pydantic import parse_obj_as
from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert
from sqlalchemy.orm import load_only
from app.db.config import get_session

from app.questions.models import BaseQuestion
from app.questions.dao import Question


class QuestionsService:
    def __init__(self, db_session: AsyncSession = Depends(get_session)):
        self.db_session = db_session
        self.http_client = httpx.AsyncClient()

    async def request_questions(self, count: int) -> dict:
        response = await self.http_client.get(url=f"https://jservice.io/api/random?count={count}")
        return response.json()

    async def get_questions(self, count: int) -> str | None:
        while 1:
            data = await self.request_questions(count)
            if not await self.check_records_exist([i["id"] for i in data]):
                data = parse_obj_as(list[BaseQuestion], data)
                await self.create_record(data)
                return await self.select_last_record()

    async def select_last_record(self) -> str | None:
        stmt = select(Question.question).order_by(Question.id.desc())
        return await self.db_session.scalar(stmt.slice(1, 2))

    async def check_records_exist(self, data: list[int]) -> bool:
        stmt = select(Question).where(Question.question_id.in_(data))
        return await self.db_session.scalar(select(stmt.exists()))

    async def create_record(self, data: list[BaseQuestion]) -> None:
        data = [i.dict() for i in data]
        await self.db_session.execute(insert(Question).values(data))
        await self.db_session.commit()
