from fastapi import APIRouter, Depends, HTTPException
from app.database import activity_collection
from app.utils.auth import verify_token
from datetime import datetime, timedelta
from pydantic import BaseModel
from bson import ObjectId


router = APIRouter(prefix="/activity", tags=["Activity"])


# -----------------------------
# Activity Model
# -----------------------------
class ActivityCreate(BaseModel):
    activity_type: str   # gym, run, sports, walk
    duration_minutes: int
    calories_burned: int


# -----------------------------
# 1️⃣ Add Activity
# -----------------------------
@router.post("/add-activity")
async def add_activity(activity: ActivityCreate, email: str = Depends(verify_token)):

    activity_dict = activity.dict()
    activity_dict["user_email"] = email
    activity_dict["created_at"] = datetime.utcnow()

    await activity_collection.insert_one(activity_dict)

    return {"message": "Activity logged successfully"}


# -----------------------------
# 2️⃣ Get My Activities
# -----------------------------
@router.get("/my-activities")
async def get_my_activities(email: str = Depends(verify_token)):

    activities = await activity_collection.find(
        {"user_email": email}
    ).to_list(length=None)

    for activity in activities:
        activity["_id"] = str(activity["_id"])

    return {"activities": activities}


# -----------------------------
# 3️⃣ Daily Calories Burned
# -----------------------------
@router.get("/daily-summary")
async def daily_summary(email: str = Depends(verify_token)):

    today = datetime.utcnow()
    start_of_day = datetime(today.year, today.month, today.day)

    pipeline = [
        {
            "$match": {
                "user_email": email,
                "created_at": {"$gte": start_of_day}
            }
        },
        {
            "$group": {
                "_id": None,
                "total_calories_burned": {"$sum": "$calories_burned"}
            }
        }
    ]

    result = await activity_collection.aggregate(pipeline).to_list(length=1)

    if not result:
        return {"total_calories_burned_today": 0}

    return {"total_calories_burned_today": result[0]["total_calories_burned"]}


# -----------------------------
# 4️⃣ Weekly Activity Comparison
# -----------------------------
@router.get("/weekly-summary")
async def weekly_summary(email: str = Depends(verify_token)):

    today = datetime.utcnow()
    start_of_week = today - timedelta(days=7)

    pipeline = [
        {
            "$match": {
                "user_email": email,
                "created_at": {"$gte": start_of_week}
            }
        },
        {
            "$group": {
                "_id": {
                    "$dayOfWeek": "$created_at"
                },
                "total_calories": {"$sum": "$calories_burned"}
            }
        },
        {
            "$sort": {"_id": 1}
        }
    ]

    results = await activity_collection.aggregate(pipeline).to_list(length=None)

    return {"weekly_activity": results}