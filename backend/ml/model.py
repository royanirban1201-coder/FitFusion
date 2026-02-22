import joblib
import os


MODEL_PATH = os.path.join("ml", "saved_models", "weight_model.pkl")


def load_model():
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)
    return None


def predict_weight_change(model, features):
    prediction = model.predict([list(features.values())])
    return prediction[0]