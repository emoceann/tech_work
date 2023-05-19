from fastapi import APIRouter, Depends
from app.questions.services import QuestionsService


router = APIRouter(prefix="/questions")


@router.post("/", response_model=str | None)
async def get_number_questions(count: int, service: QuestionsService = Depends(QuestionsService)):
    return await service.get_questions(count)
