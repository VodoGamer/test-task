from datetime import datetime

import aiohttp
from pydantic import BaseModel


class Question(BaseModel):
    id: int
    question: str
    answer: str
    created_at: datetime


async def get_random_questions(count: int) -> list[Question]:
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://jservice.io/api/random?count={count}") as resp:
            questions_response = await resp.json()
    return [Question(**question_response) for question_response in questions_response]
