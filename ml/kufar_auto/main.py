from catboost import CatBoostRegressor
from data_prep import load_data, prepare_data
from feature_eng import features, cat_features, add_feature_wear
from train import save_model


#---------------------------------------------------------------
path = "../data/kufar_auto_v2.csv"

df = load_data(path)
df = prepare_data(df)
df = add_feature_wear(df)


#-------------------------------------------------------------------
X = df[features]
y = df["price_usd"]


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


save_model(model, path="catboost_kufar_auto.pkl")