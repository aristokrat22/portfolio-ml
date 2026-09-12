import pickle
from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


app = FastAPI()

MODEL_PATH_CARS = Path(__file__).parent / "catboost_kufar_auto.pkl"
MODEL_PATH_HOUSES = Path(__file__).parent / "catboost_kufar_kv.pkl"

with open(MODEL_PATH_CARS, "rb") as f1:
    model_cars = pickle.load(f1)

with open(MODEL_PATH_HOUSES, "rb") as f2:
    model_houses = pickle.load(f2)


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


class CarInput(BaseModel):
    regdate: int      # Год выпуска
    mileage: float    # Пробег (км)
    engine: str       # Тип топлива / двигатель
    capacity: float   # Объем двигателя (л)
    gearbox: str      # Коробка передач
    body_type: str    # Тип кузова
    drive: str        # Привод
    brand: str        # Марка
    model: str        # Модель


@app.post("/api/models/predict-price-car")
def predict_price_car(data: CarInput):
    # Расчет фичи износа wear
    age = 2026 - data.regdate
    wear = round(data.mileage / (age + 1), 1)

    # Строгий порядок фичей согласно features в feature_eng.py:
    # ["regdate", "mileage", "engine", "capacity", "gearbox", "body_type", "drive", "brand", "model", "wear"]
    features_order = [
        data.regdate,
        data.mileage,
        data.engine,
        data.capacity,
        data.gearbox,
        data.body_type,
        data.drive,
        data.brand,
        data.model,
        wear,
    ]

    prediction = model_cars.predict([features_order])[0]
    predicted_price = max(0, round(float(prediction), 2))

    return {
        "predicted_price": predicted_price
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)