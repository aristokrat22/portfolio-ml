import pandas as pd
import numpy as np
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent

def load_data(filename):
    df = pd.read_csv(DATA_DIR / filename)
    return df


def correlation_ratio(categories, values):
    categories = np.array(categories)
    values = np.array(values)
    ss_total = np.sum((values - values.mean())**2)
    ss_between = sum(
        len(values[categories == cat]) * (values[categories == cat].mean() - values.mean())**2
        for cat in np.unique(categories)
    )
    return np.sqrt(ss_between / ss_total)


def clean_price_pre_meter(df, min_price=500, max_price=None):
    df_clean = df.copy()
    df_clean = df_clean[df_clean["price_per_meter_usd"] >= min_price]
    
    if max_price is not None:
        df_clean = df_clean[df_clean["price_per_meter_usd"] <= max_price]

    
    return df_clean


def convert_bool_to_int(df, bool_columns=None):
    df_result = df.copy()
    
    if bool_columns is None:
        bool_columns = df_result.select_dtypes(include="bool").columns.tolist()
    
    for col in bool_columns:
        df_result[col] = df_result[col].astype(int)
    
    print(f"Сконвертировано колонок: {bool_columns}")
    
    return df_result


def clean_nan(df, num_strategy=None, cat_fill_value="не_указано", add_missing_flag=True):
    """
    Разом чистит NaN по всем колонкам:
    - числовые -> импутация (median/mean) + опциональный флаг пропуска
    - категориальные (object/str) -> заполняются cat_fill_value
    """
    df_result = df.copy()
    
    num_cols = df_result.select_dtypes(include=["float64", "int64"]).columns.tolist()
    cat_cols = df_result.select_dtypes(include=["object"]).columns.tolist()

    for col in num_cols:
        n_missing = df_result[col].isna().sum()
        if n_missing == 0:
            continue
        
        if add_missing_flag:
            df_result[f"{col}_missing"] = df_result[col].isna().astype(int)
        
        if num_strategy == "median":
            fill_val = df_result[col].median()
        elif num_strategy == "mean":
            fill_val = df_result[col].mean()
        else:
            fill_val = 0
        
        df_result[col] = df_result[col].fillna(fill_val)
        print(f"[num] {col}: заполнено {n_missing} пропусков значением {fill_val:.2f}")
    
    for col in cat_cols:
        n_missing = df_result[col].isna().sum()
        if n_missing == 0:
            continue
        
        df_result[col] = df_result[col].fillna(cat_fill_value)
        print(f"[cat] {col}: заполнено {n_missing} пропусков значением '{cat_fill_value}'")
    
    return df_result

