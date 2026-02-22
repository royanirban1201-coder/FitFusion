from fastapi import APIRouter

router = APIRouter(
    prefix="/crud",
    tags=["CRUD"]
)


@router.get("/health")
def crud_health():
    return {"message": "CRUD routes working"}