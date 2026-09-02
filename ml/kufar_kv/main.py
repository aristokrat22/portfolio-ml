from catboost import CatBoostRegressor
from data_prep import load_data, clean_price_pre_meter, convert_bool_to_int, clean_nan
from feature_eng import features, cat_features, parse_address
from train import save_model


#---------------------------------------------------------------
path = "../data/kufar_ads.csv"
df = load_data(path)
df = clean_price_pre_meter(df)
df = convert_bool_to_int(df)
df = clean_nan(df)


#-------------------------------------------------------------------
df[["street", "house_number"]] = df["address"].apply(parse_address)
features = ["rooms", "year_built", "has_balcony", "is_first_floor", "is_last_floor",
            "area_total", "area_living", "area_kitchen", "bathroom_type", "balcony_type", "condition","street"]
cat_features = ["bathroom_type", "balcony_type", "condition", "street"]
df = clean_nan(df)


#--------------------------------------------------------------------------
X = df[features]
y = df["price_per_meter_usd"]


#-------------------------------------------------------------------------------
log_params = {
    "iterations": 900,
    "depth": 5,
    "learning_rate": 0.02,
}
unlog_params = {
    "random_state": 42,
    "verbose": False,
}

model_params = log_params | unlog_params
model = CatBoostRegressor(**model_params, cat_features=cat_features)
model.fit(X, y)


save_model(model, path="catboost_kufar_kv.pkl")