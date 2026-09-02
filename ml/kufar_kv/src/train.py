from sklearn.model_selection import KFold, train_test_split
from evaluate import evaluate_results
import mlflow
import pickle
from pathlib import Path


def train_model(
    model,
    X,
    y,
    mode='holdout',
    n_rows=None,
    test_size=0.2,
    n_splits=5,
    random_state=42
):
    if n_rows is not None:
        X = X.sample(n=n_rows, random_state=random_state)
        y = y.loc[X.index]
        actual_n_rows = n_rows
    else:
        actual_n_rows = len(X)

    
    if mode == 'holdout':
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state
        )
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        return [(y_test, y_pred)], actual_n_rows

    elif mode == 'cv':
        kf = KFold(n_splits=n_splits, shuffle=True, random_state=random_state)
        results = []
        for train_idx, val_idx in kf.split(X):
            X_train, X_val = X.iloc[train_idx], X.iloc[val_idx]
            y_train, y_val = y.iloc[train_idx], y.iloc[val_idx]
            model.fit(X_train, y_train)
            y_pred = model.predict(X_val)
            results.append((y_val, y_pred))
        return results, actual_n_rows

    else:
        raise ValueError(f"Неизвестный mode: {mode!r}. Используй 'holdout' или 'cv'.")


def save_model(model, path="model.pkl"):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "wb") as f:
        pickle.dump(model, f)
    print(f"Модель сохранена: {path.resolve()}")


def log_experiment(
    results,
    model,
    model_params,
    mode,
    features,
    path,
    n_rows,
):
    
    mlflow.log_param("data-name", path)
    mlflow.log_param("data-rows", n_rows)
    mlflow.log_params(model_params)
    mlflow.log_param("mode", mode)
    mlflow.log_param("features", features)


    _, summary = evaluate_results(results)
    print("Доступные метрики:", list(summary.keys()))
    rmse = summary['rmse']['mean']
    nrmse = summary['nrmse']['mean']
    r2 = summary['r2']['mean']  # Вытаскиваем средний R2
    
    mlflow.log_metric("rmse", rmse)
    mlflow.log_metric("nrmse", nrmse)
    mlflow.log_metric("r2", r2) # Логируем в MLflow

    print(f"RMSE:  {rmse:.2f}")
    print(f"NRMSE: {nrmse:.2f}%")
    print(f"R2:    {r2:.4f}")
    print(model.get_params().items())

