from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

from backend.ml.analyzer import calorie_analysis

router = APIRouter(
    prefix="/ai",
    tags=["AI"]
)


class CalorieData(BaseModel):
    calories: int


class CalorieRequest(BaseModel):
    data: List[CalorieData]


@router.post("/calorie-analysis")
def ai_calorie_analysis(request: CalorieRequest):
    formatted_data = [item.dict() for item in request.data]
    result = calorie_analysis(formatted_data)
    return result