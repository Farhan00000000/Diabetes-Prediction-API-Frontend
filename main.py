from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Load model and scaler
model = joblib.load("diabetes_model.pkl")
scaler = joblib.load("scaler.pkl")

class InputData(BaseModel):
    Pregnancies: int
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/predict")
async def predict(data: InputData):
    arr = np.array([[data.Pregnancies, data.Glucose, data.BloodPressure,
                     data.SkinThickness, data.Insulin, data.BMI,
                     data.DiabetesPedigreeFunction, data.Age]])
    arr_scaled = scaler.transform(arr)
    pred = model.predict(arr_scaled)[0]
    prob = model.predict_proba(arr_scaled)[0].max()
    return {
        "prediction": int(pred),
        "result": "Diabetic" if pred == 1 else "Not Diabetic",
        "confidence": round(float(prob), 2)
    }

