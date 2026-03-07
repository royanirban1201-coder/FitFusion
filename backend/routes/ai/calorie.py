from fastapi import APIRouter
from backend.schemas.calorie_schema import CalorieRequest, CalorieResponse
from backend.ml.analyzer import calorie_analysis

router = APIRouter()

@router.post("/calorie", response_model=CalorieResponse)
def analyze_calories(data: CalorieRequest):

    result = calorie_analysis(
        age=data.age,
        height=data.height,
        weight=data.weight,
        activity=data.activity_level
    )

    return {"calories": result}