from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routers
from backend.routes.ai.calorie import router as ai_router

app = FastAPI(title="FitFusion API")

# CORS configuration
origins = [
    "http://localhost:3000",   # React frontend
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root route
@app.get("/")
def read_root():
    return {"message": "FitFusion backend running"}
@app.get("/health")
def health_check():
    return {"status": "backend running"}
@app.get("/test")
def test_api():
    return {"message": "API working correctly"}

# Include routers
app.include_router(ai_router, prefix="/ai", tags=["AI"])