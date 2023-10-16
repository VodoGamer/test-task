from fastapi import APIRouter
from pydantic import BaseModel

from src.services.db.questions import add_question, get_last_question, get_question_by_id
from src.services.questions import Question, get_random_questions

router = APIRouter()


class QuizParameters(BaseModel):
    questions_num: int


@router.post("/")
async def random_questions(parameters: QuizParameters) -> Question | None:
    questions: list[Question] = await get_random_questions(parameters.questions_num)
    last_question = await get_last_question()
    if last_question:
        last_question = Question(**last_question.__dict__)

    for question in questions:
        await add_unique_question(question)

    return last_question


async def add_unique_question(question: Question) -> None:
    if await get_question_by_id(question.id):
        new_question: Question = (await get_random_questions(1))[0]
        await add_unique_question(new_question)
    await add_question(question.id, question.question, question.answer, question.created_at)
