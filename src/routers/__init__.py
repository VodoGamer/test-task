from typing import Iterable

from fastapi import APIRouter

from . import quiz

routers: Iterable[APIRouter] = (quiz.router,)
