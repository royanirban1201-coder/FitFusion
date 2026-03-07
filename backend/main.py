from fastapi import FastAPI

from backend.routes.ai.calorie import router as ai_router
from backend.routes.crud.placeholder import router as crud_router

app = FastAPI()

app.include_router(ai_router)
app.include_router(crud_router)


@app.get("/")
def home():
    return {"message": "FitFusion Backend Running 🚀"}