import pandas as pd
import numpy as np
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent

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