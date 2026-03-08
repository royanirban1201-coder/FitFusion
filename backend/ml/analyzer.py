from backend.ml.preprocessing import prepare_calorie_features


def calorie_analysis(age, height, weight, activity):

    bmr = 10 * weight + 6.25 * height - 5 * age + 5

    if activity == "low":
        multiplier = 1.2
    elif activity == "moderate":
        multiplier = 1.55
    else:
        multiplier = 1.9

    calories = bmr * multiplier

    return calories