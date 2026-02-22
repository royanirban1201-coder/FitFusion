import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os


def train_model():
    # Fake dataset for now
    data = {
        "avg_calories": [1800, 2200, 2700, 2500],
        "variance": [100, 150, 200, 170],
        "weight_change": [-0.5, 0.1, 0.8, 0.6]
    }

    df = pd.DataFrame(data)

    X = df[["avg_calories", "variance"]]
    y = df["weight_change"]

    model = LinearRegression()
    model.fit(X, y)

    os.makedirs("ml/saved_models", exist_ok=True)
    joblib.dump(model, "ml/saved_models/weight_model.pkl")


if __name__ == "__main__":
    train_model()
    print("Model trained and saved.")