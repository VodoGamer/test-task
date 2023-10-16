from datetime import datetime

from sqlalchemy import select

from src.client import async_session
from src.services.db.models import QuestionModel


async def get_question_by_id(id: int) -> QuestionModel | None:
    async with async_session() as session:
        response = await session.execute(select(QuestionModel).where(QuestionModel.id == id))
    return response.scalar_one_or_none()


async def get_last_question() -> QuestionModel | None:
    async with async_session() as session:
        response = await session.execute(
            select(QuestionModel).order_by(QuestionModel.added_at.desc()).limit(1)
        )
    return response.scalar_one_or_none()


async def add_question(id: int, question: str, answer: str, created_at: datetime) -> None:
    new_question = QuestionModel(**locals())
    async with async_session() as session:
        session.add(new_question)
        await session.commit()
