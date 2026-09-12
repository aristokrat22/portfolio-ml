import pandas as pd
import numpy as np
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent

def load_data(filename):
    df = pd.read_csv(DATA_DIR / filename)
    return df


def filter_price_outliers(data: pd.DataFrame, budget_brands=None, old_year=2005, old_price_cap=50000, absolute_cap=100000) -> pd.DataFrame:
    """Убирает битые/неправдоподобные цены: совпадение с пробегом, старые бренды по космическим ценам, старые авто за неадекват, любые цены выше разумного потолка."""
    budget_brands = budget_brands or ["vaz", "ваз", "москвич", "газ", "запорожец", "иж", "лада", "lada"]
    brand_lower = data["brand"].astype(str).str.lower()

    bad = (
        (data["price_usd"] == data["mileage"]) |
        (brand_lower.isin(budget_brands) & (data["price_usd"] > 15000)) |
        ((data["regdate"] < old_year) & (data["price_usd"] > old_price_cap)) |
        (data["price_usd"] > absolute_cap)
    )

    print(f"Отсеяно по неправдоподобной цене: {bad.sum()} из {len(data)}")
    return data[~bad].reset_index(drop=True)


def prepare_data(
    df: pd.DataFrame,
    min_price: float = 500.0,
    is_train: bool = True
) -> pd.DataFrame:
    data = df.copy()

    if "price_usd" in data.columns:
        data["price_usd"] = data["price_usd"] / 100.0
        if is_train:
            data = data.dropna(subset=["price_usd"])
            data = data[data["price_usd"] >= min_price]
            data = filter_price_outliers(data)

    cat_columns = ["engine", "gearbox", "body_type", "drive", "condition"]
    for col in cat_columns:
        if col in data.columns:
            data[col] = data[col].fillna("Unknown").astype(str)

    # brand/model/generation теперь приходят готовыми из скрейпа,
    # но могут быть "error"/"closed" (сбой сбора / объявление уже снято)
    car_columns = ["brand", "model", "generation"]
    for col in car_columns:
        if col in data.columns:
            data[col] = data[col].fillna("unknown").replace(
                {"error": "unknown", "closed": "unknown"}
            ).astype(str)

    if "capacity" in data.columns:
        data["capacity"] = data["capacity"].fillna(0.0).astype(float)

    if "seats" in data.columns:
        data["seats"] = data["seats"].fillna(5.0).astype(int)

    if "regdate" in data.columns:
        data["regdate"] = data["regdate"].astype(int)

    if "mileage" in data.columns:
        bad_mileage = data["mileage"] > 900000
        print(f"Отсеяно по нереальному пробегу: {bad_mileage.sum()} из {len(data)}")
        data = data[~bad_mileage]

    return data.reset_index(drop=True)