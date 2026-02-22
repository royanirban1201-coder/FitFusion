import pandas as pd


def prepare_calorie_features(food_logs):
    """
    Converts raw MongoDB food logs into ML-ready features.
    """

    if not food_logs:
        return None

    df = pd.DataFrame(food_logs)

    # Calculate variance safely
    variance = df["calories"].var()

    if pd.isna(variance):
        variance = 0

    features = {
        "avg_calories": float(df["calories"].mean()),
        "max_calories": float(df["calories"].max()),
        "min_calories": float(df["calories"].min()),
        "variance": float(variance)
    }

    return features