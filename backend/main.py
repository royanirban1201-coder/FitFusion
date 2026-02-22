
from fastapi import FastAPI
from database.mongo import db

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FitFusion Backend Running 🚀"}

@app.get("/test-db")
def test_db():
    collections = db.list_collection_names()
    return {"collections": collections}