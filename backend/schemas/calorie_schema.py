from pydantic import BaseModel

class CalorieRequest(BaseModel):
    age: int
    height: float
    weight: float
    activity_level: str


class CalorieResponse(BaseModel):
    calories: float