import pickle
from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn



app = FastAPI()

MODEL_PATH_CARS = Path(__file__).parent / "model-examscore.pkl"
MODEL_PATH_HOUSES = Path(__file__).parent / "catboost_kufar_kv.pkl"

with open(MODEL_PATH_CARS, "rb") as f1:
    model_cars = pickle.load(f1)

with open(MODEL_PATH_HOUSES, "rb") as f2:
    model_houses = pickle.load(f2)

import pandas as pd
from pydantic import BaseModel


class HouseInput(BaseModel):
    rooms: int
    year_built: int
    has_balcony: int
    is_first_floor: int
    is_last_floor: int
    area_total: float
    area_living: float
    area_kitchen: float
    bathroom_type: str
    balcony_type: str
    condition: str
    street: str


@app.post("/api/models/predict-price-house")
def predict_price_houses(data: HouseInput):
    # Порядок строго как в ноутбуке обучения
    features_order = [
        data.rooms,
        data.year_built,
        data.has_balcony,
        data.is_first_floor,
        data.is_last_floor,
        data.area_total,
        data.area_living,
        data.area_kitchen,
        data.bathroom_type,
        data.balcony_type,
        data.condition,
        data.street,
    ]

    # Модель предсказывает цену за 1 кв.м
    pred_per_meter = float(model_houses.predict([features_order])[0])
    total_price = round(pred_per_meter * data.area_total, 2)

    return {
        "price_per_meter": round(pred_per_meter, 2),
        "predicted_price": total_price,
    }


class ExamInput(BaseModel):
    study_hours: float
    class_attendance: float
    sleep_hours: float
    sleep_quality: str
    study_method: str
    facility_rating: str


@app.post("/api/models/predict-price-car")
def predict_exam_score(data: ExamInput):
    features_order = [
        data.study_hours,
        data.class_attendance,
        data.sleep_hours,
        data.sleep_quality,
        data.study_method,
        data.facility_rating,
    ]
    prediction = model_cars.predict([features_order])
    return {"predicted_score": float(prediction[0])}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)