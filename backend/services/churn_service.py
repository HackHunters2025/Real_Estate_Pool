# services/churn_service.py

import os
import pandas as pd

def load_tenant_data(property_id):
    base_path = f"backend/data/properties/{property_id}/tenant_data.csv"

    if not os.path.exists(base_path):
        return pd.DataFrame({
            "tenant_id": [1, 2, 3],
            "late_payments": [1, 4, 0],
            "complaints": [0, 5, 1],
            "months_stayed": [18, 6, 25],
            "rent_increase": [5, 8, 2]
        })

    return pd.read_csv(base_path)


def calculate_churn_score(row):
    score = 0
    if row["late_payments"] >= 3:
        score += 0.35
    elif row["late_payments"] == 2:
        score += 0.20
    elif row["late_payments"] == 1:
        score += 0.10

    if row["complaints"] >= 4:
        score += 0.30
    elif row["complaints"] >= 2:
        score += 0.20
    elif row["complaints"] == 1:
        score += 0.10

    if row["months_stayed"] < 6:
        score += 0.25
    elif row["months_stayed"] < 12:
        score += 0.15

    if row["rent_increase"] >= 8:
        score += 0.25
    elif row["rent_increase"] >= 5:
        score += 0.15

    return min(score, 1.0)


def risk_level(score):
    if score >= 0.75:
        return "High"
    elif score >= 0.40:
        return "Medium"
    else:
        return "Low"


def run_churn_prediction(property_id="property_A"):
    df = load_tenant_data(property_id)
    df["churn_score"] = df.apply(calculate_churn_score, axis=1)
    avg_score = df["churn_score"].mean()
    risk = risk_level(avg_score)

    factors = []
    if df["late_payments"].mean() >= 2:
        factors.append("Frequent Late Payments")
    if df["complaints"].mean() >= 3:
        factors.append("High Complaint Frequency")
    if df["months_stayed"].mean() < 12:
        factors.append("Short Occupancy Period")
    if df["rent_increase"].mean() >= 6:
        factors.append("High Rent Increase")
    if not factors:
        factors.append("Stable Tenant Behavior")

    return {
        "churn_score": round(float(avg_score), 2),
        "risk_level": risk,
        "top_factors": factors,
        "tenant_count": len(df)
    }


class ChurnService:
    def __init__(self, property_id):
        self.property_id = property_id
        self.data = load_tenant_data(property_id)

    def predict_churn(self):
        self.data["churn_score"] = self.data.apply(calculate_churn_score, axis=1)
        return self.data["churn_score"].tolist()

    def run(self):
        return run_churn_prediction(self.property_id)


if __name__ == "__main__":
    print(run_churn_prediction("property_A"))
