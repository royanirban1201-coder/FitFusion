from ml.preprocessing import prepare_calorie_features


def calorie_analysis(food_logs):

    features = prepare_calorie_features(food_logs)

    if features is None:
        return {"message": "No data available"}

    avg = features["avg_calories"]

    if avg > 2500:
        status = "High intake"
    elif avg < 1800:
        status = "Low intake"
    else:
        status = "Balanced"

    return {
        "features": features,
        "status": status
    }