import pandas as pd

features = [
    "regdate",
    "mileage",
    "engine",
    "capacity",
    "gearbox",
    "body_type",
    "drive",
    "brand",
    "model",
    "wear"
]

cat_features = ["engine", "gearbox", "body_type", "drive", "brand", "model"]

#, "model", "generation"

def add_feature_wear(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    age = 2026 - df["regdate"]
    df["wear"] = (df["mileage"] / (age + 1)).round(1)
    return df