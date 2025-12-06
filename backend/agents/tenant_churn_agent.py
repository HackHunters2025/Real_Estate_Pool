# backend/agents/tenant_churn_agent.py
"""
Tenant Churn Prediction Agent
Supports:
- GET: Using property_id (CSV-based churn)
- POST: Using property_id or custom tenant attributes (no CSV required)
"""

from fastapi import APIRouter, Query
from services.churn_service import run_churn_prediction

router = APIRouter()


# ------------------------------------------------------------
# GET: Churn for property using dataset
# ------------------------------------------------------------
@router.get("/churn")
def churn_get(property_id: str = Query("property_A")):
    """
    GET churn prediction using stored tenant dataset (CSV).
    Example:
    /churn?property_id=property_A
    """
    try:
        result = run_churn_prediction(property_id)

        return {
            "status": "success",
            "agent": "tenant_churn_agent",
            "mode": result.get("mode"),
            "property_id": property_id,
            "churn_score": result.get("churn_score"),
            "risk_level": result.get("risk_level"),
            "top_factors": result.get("top_factors"),
            "tenant_count": result.get("tenant_count")
        }

    except Exception as e:
        return {
            "status": "error",
            "property_id": property_id,
            "message": str(e)
        }


# ------------------------------------------------------------
# POST: Accept JSON Input for custom prediction or property
# ------------------------------------------------------------
@router.post("/churn")
def churn_post(payload: dict):
    """
    Supports:
    1️⃣ Batch CSV-like JSON
    {
      "csv": [
        { "late_payments": 2, "complaints": 1, "months_stayed": 12, "rent_increase": 6 }
      ]
    }

    2️⃣ Single manual tenant:
    {
      "late_payments": 3,
      "complaints": 2,
      "months_stayed": 9,
      "rent_increase": 7
    }
    """
    try:
        # Batch CSV JSON mode
        if "csv" in payload:
            return run_churn_prediction(json_csv_data=payload["csv"])

        # Manual tenant mode
        if all(k in payload for k in ["late_payments", "complaints", "months_stayed", "rent_increase"]):
            return run_churn_prediction(manual_input=payload)

        return {"status": "error", "message": "Invalid input. Provide 'csv' array or manual tenant attributes."}

    except Exception as e:
        return {"status": "error", "message": str(e)}

# Standalone test
if __name__ == "__main__":
    print(churn_post({"late_payments": 2, "complaints": 1, "months_stayed": 10, "rent_increase": 5}))
