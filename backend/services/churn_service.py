import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

# ------------------------------------------------------------
# Run churn prediction — JSON CSV Mode
# ------------------------------------------------------------
def run_churn_prediction(property_id=None, manual_input=None, json_csv_data=None):
    # CASE 1: JSON CSV Input
    if json_csv_data is not None:
        df = pd.DataFrame(json_csv_data)

        required = {"late_payments", "complaints", "months_stayed", "rent_increase"}
        if not required.issubset(df.columns):
            raise ValueError("CSV JSON must include: late_payments, complaints, months_stayed, rent_increase")

        # Auto-generate labels if missing
        if "churned" not in df.columns:
            df["churned"] = ((df["complaints"] > 2) & (df["months_stayed"] < 8)).astype(int)

        feature_cols = ["late_payments", "complaints", "months_stayed", "rent_increase"]
        X = df[feature_cols]
        y = df["churned"]

        model = LogisticRegression()
        model.fit(X, y)

        df["churn_score"] = model.predict_proba(X)[:, 1]
        df["churn_score"] = df["churn_score"].round(3)

        def map_risk(score):
            if score >= 0.70: return "HIGH"
            elif score >= 0.40: return "MEDIUM"
            return "LOW"

        df["risk_level"] = df["churn_score"].apply(map_risk)

        return {
            "mode": "json_csv_batch_prediction",
            "total_predicted": len(df),
            "results": df.to_dict(orient="records")
        }

    # CASE 2 – fallback manual single entry
    if manual_input:
        coef_map = {
            "late_payments": 0.35,
            "complaints": 0.45,
            "months_stayed": -0.30,
            "rent_increase": 0.25
        }

        score = (
            manual_input["late_payments"] * coef_map["late_payments"] +
            manual_input["complaints"] * coef_map["complaints"] +
            manual_input["months_stayed"] * coef_map["months_stayed"] +
            manual_input["rent_increase"] * coef_map["rent_increase"]
        )
        
        score = 1 / (1 + np.exp(-score))
        score = round(float(score), 3)

        risk = "HIGH" if score >= 0.70 else "MEDIUM" if score >= 0.40 else "LOW"

        return {
            "mode": "manual_single_tenant",
            "churn_score": score,
            "risk_level": risk
        }

    raise ValueError("Provide json_csv_data or manual_input")
