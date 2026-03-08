from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends
from app.utils.auth import create_access_token
from fastapi import APIRouter, HTTPException
from app.models.user_model import UserCreate, UserLogin
from app.database import user_collection
from passlib.context import CryptContext

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Function to hash password
def hash_password(password: str):
    return pwd_context.hash(password)


# Function to verify password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


# Register User
@router.post("/register")
async def register_user(user: UserCreate):

    existing_user = await user_collection.find_one({"email": user.email})

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = hash_password(user.password)

    user_dict = user.dict()
    user_dict["password"] = hashed_password

    await user_collection.insert_one(user_dict)

    return {"message": "User registered successfully"}


# Login User
@router.post("/login")
async def login_user(form_data: OAuth2PasswordRequestForm = Depends()):

    existing_user = await user_collection.find_one({"email": form_data.username})

    if not existing_user:
        raise HTTPException(status_code=400, detail="User not found")

    if not pwd_context.verify(form_data.password, existing_user["password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": form_data.username})

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }