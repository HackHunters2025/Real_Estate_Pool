# occupancy_service.py
"""
Service logic for occupancy trend analysis and forecasting.
Used by occupancy_agent.py.
"""

import os
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# ------------------------------------------------------------
# Load occupancy data for a property
# ------------------------------------------------------------
def load_occupancy_data(property_id):
    base_path = f"backend/data/properties/{property_id}/occupancy.csv"

    if not os.path.exists(base_path):
        raise FileNotFoundError(f"occupancy.csv not found for {property_id}")

    df = pd.read_csv(base_path)

    if not {"month", "occupancy_rate"}.issubset(df.columns):
        raise ValueError("occupancy.csv must contain: month, occupancy_rate")

    return df

# ------------------------------------------------------------
# Simple linear regression occupancy forecast
# ------------------------------------------------------------
def forecast_occupancy(values, months_ahead=3):
    values = np.array(values)

    if len(values) < 2:
        return [values[-1] for _ in range(months_ahead)]

    X = np.arange(len(values)).reshape(-1, 1)
    y = values

    model = LinearRegression()
    model.fit(X, y)

    future_X = np.arange(len(values), len(values) + months_ahead).reshape(-1, 1)
    future_vals = model.predict(future_X)

    return np.clip(future_vals, 0, 1).tolist()

# ------------------------------------------------------------
# Main run_occupancy_forecast function (standalone)
# ------------------------------------------------------------
def run_occupancy_forecast(property_id="property_A"):
    df = load_occupancy_data(property_id)

    months = df["month"].tolist()
    occupancy_rate = df["occupancy_rate"].tolist()

    future_pred = forecast_occupancy(occupancy_rate, 3)
    future_months = [f"Future-{i+1}" for i in range(3)]
    trend = "up" if future_pred[-1] > occupancy_rate[-1] else "down"

    return {
        "months": months + future_months,
        "occupancy_rate": occupancy_rate + future_pred,
        "trend": trend,
        "current_occupancy": round(float(occupancy_rate[-1]), 2),
        "predicted_future_rate": [round(float(v), 2) for v in future_pred]
    }

# ------------------------------------------------------------
# OccupancyService class for integration
# ------------------------------------------------------------
class OccupancyService:
    def __init__(self, property_id):
        self.property_id = property_id
        self.data = load_occupancy_data(property_id)
        self.occupancy_rate = self.data["occupancy_rate"].tolist()

    def forecast_occupancy(self, months=3):
        return forecast_occupancy(self.occupancy_rate, months)

# ------------------------------------------------------------
# Standalone test
# ------------------------------------------------------------
if __name__ == "__main__":
    print(run_occupancy_forecast("property_A"))
