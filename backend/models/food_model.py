from pydantic import BaseModel
from typing import Optional


class FoodCreate(BaseModel):
    food_name: str
    calories: int
    protein: float
    carbs: float
    fats: float


class FoodUpdate(BaseModel):
    food_name: Optional[str] = None
    calories: Optional[int] = None
    protein: Optional[float] = None
    carbs: Optional[float] = None
    fats: Optional[float] = None