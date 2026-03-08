from app.utils.auth import verify_token
from fastapi import Depends, APIRouter, HTTPException
from datetime import datetime
from app.models.food_model import FoodCreate, FoodUpdate
from app.database import food_collection
from bson import ObjectId

router = APIRouter()


# Add Food Log
@router.post("/add-food")
async def add_food(food: FoodCreate, email: str = Depends(verify_token)):
    food_dict = food.dict()
    food_dict["user_email"] = email
    food_dict["created_at"] = datetime.utcnow()

    await food_collection.insert_one(food_dict)

    return {"message": "Food added successfully"}


# Get User Food Logs
@router.get("/user-food")
async def get_user_food(email: str = Depends(verify_token)):
    foods_cursor = food_collection.find({"user_email": email})
    foods = await foods_cursor.to_list(length=None)

    for food in foods:
        food["_id"] = str(food["_id"])

    return foods


# Update Food Log
@router.put("/update-food/{food_id}")
async def update_food(food_id: str, updated_data: FoodUpdate, email: str = Depends(verify_token)):
    result = await food_collection.update_one(
        {"_id": ObjectId(food_id), "user_email": email},
        {"$set": updated_data.dict(exclude_unset=True)}
    )

    if result.modified_count == 1:
        return {"message": "Food updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Food not found")


# Delete Food Log
@router.delete("/delete-food/{food_id}")
async def delete_food(food_id: str, email: str = Depends(verify_token)):
    result = await food_collection.delete_one(
        {"_id": ObjectId(food_id), "user_email": email}
    )

    if result.deleted_count == 1:
        return {"message": "Food deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Food not found")