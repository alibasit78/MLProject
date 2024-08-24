import joblib
import numpy as np
from fastapi import FastAPI  # pylint: disable=missing-module-docstring

model = joblib.load("app/model.joblib")

class_names = ["setosa", "versicolor", "virginica"]

app = FastAPI()


@app.get("/")
def home():  # pylint: disable=missing-function-docstring
    return {"message": "We are at home"}


@app.post("/predict")
def predict(data: dict):
    """
    Predicts the class of a given set of features
    Args:
        data (dict): A dictionary containing the features to predict
        e.g., {"features": [0.1, 0.34, -0.12, 0.98]}
    Returns:
        dict: A dictionary containing the predicted class
    """
    features = np.array(data["features"]).reshape(1, -1)
    prediction = model.predict(features)[0]
    class_name = class_names[prediction]
    print("class name: ", class_name, "features: ", features)
    return {"predicted_class": class_name}
