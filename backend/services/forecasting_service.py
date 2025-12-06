# forecasting_service.py
"""
Service layer for forecasting revenue, expenses, and NOI.
This file contains the ML logic used by forecasting_agent.py.
"""

import os
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# ------------------------------------------------------------
# Load rent & expense data for a given property
# ------------------------------------------------------------
def load_property_data(property_id):
    base_path = f"backend/data/properties/{property_id}/rent_expenses.csv"

    if not os.path.exists(base_path):
        raise FileNotFoundError(f"rent_expenses.csv not found for {property_id}")

    df = pd.read_csv(base_path)

    if not {"month", "revenue", "expenses"}.issubset(df.columns):
        raise ValueError("CSV must contain: month, revenue, expenses")

    return df

# ------------------------------------------------------------
# Perform a simple linear regression forecast
# ------------------------------------------------------------
def forecast_series(values, months_ahead=6):
    values = np.array(values)
    X = np.arange(len(values)).reshape(-1, 1)
    y = values

    model = LinearRegression()
    model.fit(X, y)

    future_X = np.arange(len(values), len(values) + months_ahead).reshape(-1, 1)
    future_vals = model.predict(future_X)

    return np.maximum(future_vals, 0).tolist()

# ------------------------------------------------------------
# Main run_forecasting function (standalone)
# ------------------------------------------------------------
def run_forecasting(property_id="property_A"):
    df = load_property_data(property_id)

    months = df["month"].tolist()
    revenue = df["revenue"].tolist()
    expenses = df["expenses"].tolist()
    noi = (df["revenue"] - df["expenses"]).tolist()

    future_revenue = forecast_series(revenue, 6)
    future_expenses = forecast_series(expenses, 6)
    future_noi = forecast_series(noi, 6)

    future_months = [f"Future-{i+1}" for i in range(6)]
    trend = "up" if future_noi[-1] > noi[-1] else "down"

    return {
        "forecast_months": months + future_months,
        "predicted_revenue": revenue + future_revenue,
        "predicted_expenses": expenses + future_expenses,
        "predicted_noi": noi + future_noi,
        "trend": trend
    }

# ------------------------------------------------------------
# ForecastingService class for integration
# ------------------------------------------------------------
class ForecastingService:
    def __init__(self, property_id):
        self.property_id = property_id
        self.data = load_property_data(property_id)
        self.months = self.data["month"].tolist()
        self.revenue = self.data["revenue"].tolist()
        self.expenses = self.data["expenses"].tolist()
        self.noi = (self.data["revenue"] - self.data["expenses"]).tolist()

    def forecast_revenue(self, months=6):
        return forecast_series(self.revenue, months)

    def forecast_expenses(self, months=6):
        return forecast_series(self.expenses, months)

    def forecast_noi(self, months=6):
        return forecast_series(self.noi, months)

# ------------------------------------------------------------
# Standalone test
# ------------------------------------------------------------
if __name__ == "__main__":
    print(run_forecasting("property_A"))
