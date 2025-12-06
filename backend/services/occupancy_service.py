import os
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

BASE_PATH = "backend/data/properties/"

def run_occupancy_forecast(property_id="property_A", months_ahead=3):
    """
    Forecast future occupancy using linear regression
    """

    csv_path = os.path.join(BASE_PATH, property_id, "occupancy_history.csv")

    if not os.path.exists(csv_path):
        # fallback default if no CSV found
        history = [92, 90, 94, 91, 93, 95]
    else:
        df = pd.read_csv(csv_path)
        if "occupancy_rate" not in df.columns:
            raise ValueError("CSV must contain occupancy_rate column")
        history = df["occupancy_rate"].tolist()

    X = np.arange(len(history)).reshape(-1, 1)
    y = history

    model = LinearRegression()
    model.fit(X, y)

    future_X = np.arange(len(history), len(history) + months_ahead).reshape(-1, 1)
    future = model.predict(future_X)

    future = [round(float(v), 2) for v in future]

    trend = "up" if future[-1] > history[-1] else "down"

    return {
        "months": [f"Month-{i+1}" for i in range(len(history) + months_ahead)],
        "occupancy_rate": history + future,
        "trend": trend,
        "current_occupancy": history[-1],
        "predicted_future_rate": future
    }
