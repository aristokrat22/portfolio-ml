import numpy as np
from sklearn.metrics import mean_squared_error, r2_score 


def calculate_metrics(y_true, y_pred):
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    mean_target = np.mean(y_true)
    nrmse = rmse / mean_target * 100 
    r2 = r2_score(y_true, y_pred)

    return {
        'rmse': rmse,
        'nrmse': nrmse,
        'r2': r2,  
    }


def evaluate_results(results):
    per_pair = [calculate_metrics(y_true, y_pred) for y_true, y_pred in results]

    summary = {}
    for name in per_pair[0]:
        values = [m[name] for m in per_pair]
        summary[name] = {
            'mean': np.mean(values),
            'std': np.std(values),
        }

    return per_pair, summary