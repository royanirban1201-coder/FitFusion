from fastapi import APIRouter, Depends
from app.database import food_collection, user_collection
from app.utils.auth import verify_token
from datetime import datetime

router = APIRouter(prefix="/analytics", tags=["Campus Analytics"])


# 1️⃣ Average Calories Per Hostel
@router.get("/average-calories-per-hostel")
async def average_calories_per_hostel(current_user: str = Depends(verify_token)):

    pipeline = [
        {
            "$lookup": {
                "from": "users",
                "localField": "email",
                "foreignField": "email",
                "as": "user_data"
            }
        },
        {"$unwind": "$user_data"},
        {
            "$group": {
                "_id": "$user_data.hostel",
                "average_calories": {"$avg": "$calories"}
            }
        }
    ]

    results = await food_collection.aggregate(pipeline).to_list(length=None)

    return {"average_calories_per_hostel": results}


# 2️⃣ Average Mood Per Department
@router.get("/average-mood-per-department")
async def average_mood_per_department(current_user: str = Depends(verify_token)):

    pipeline = [
        {
            "$group": {
                "_id": "$department",
                "average_mood": {"$avg": "$mood"}
            }
        }
    ]

    results = await user_collection.aggregate(pipeline).to_list(length=None)

    return {"average_mood_per_department": results}


# 3️⃣ Activity Participation By Academic Year
@router.get("/activity-participation-by-year")
async def activity_participation_by_year(current_user: str = Depends(verify_token)):

    pipeline = [
        {
            "$group": {
                "_id": "$academic_year",
                "total_participants": {"$sum": 1}
            }
        }
    ]

    results = await user_collection.aggregate(pipeline).to_list(length=None)

    return {"activity_participation_by_year": results}


# 4️⃣ Environmental Effect On Outdoor Workouts
@router.get("/environmental-effect-outdoor-workouts")
async def environmental_effect_outdoor_workouts(current_user: str = Depends(verify_token)):

    pipeline = [
        {
            "$match": {
                "workout_type": "outdoor"
            }
        },
        {
            "$group": {
                "_id": "$weather_condition",
                "average_duration": {"$avg": "$duration_minutes"}
            }
        }
    ]

    results = await food_collection.aggregate(pipeline).to_list(length=None)

    return {"environmental_effect_on_outdoor_workouts": results}