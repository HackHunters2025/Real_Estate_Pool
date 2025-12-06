"""
Portfolio Optimization Agent
---
Goal:
Allocate capital across multiple properties to maximize ROI
based on user-selected risk level (low / medium / high).

This agent is designed for AGI-style agent orchestration:
pricing → churn → forecast → portfolio allocation.
"""

from fastapi import APIRouter, Query
from services.portfolio_service import run_portfolio_optimization
from services.graph_store import save_event

router = APIRouter()


# ------------------------------------------------------------
# GET Endpoint (Quick Testing & Demo Mode)
# ------------------------------------------------------------
@router.get("/portfolio")
def portfolio_get(
    risk_level: str = Query("medium", description="Risk level: low / medium / high")
):
    """
    GET portfolio optimization (Demo)
    Automatically loads sample properties internally.
    Good for showcasing the feature quickly.
    """

    try:
        result = run_portfolio_optimization(properties=None, risk_level=risk_level)

        # Save thinking for agent memory
        save_event(
            "portfolio_agent",
            "portfolio_recommendation",
            {"risk_level": risk_level, "result": result},
        )

        return {
            "status": "success",
            "agent": "portfolio_agent",
            "risk_level": risk_level,
            "optimization_decision": result,
            "agent_chain": ["forecasting_agent", "pricing_agent", "portfolio_agent"]
        }

    except Exception as e:
        return {
            "status": "error",
            "agent": "portfolio_agent",
            "message": str(e),
        }


# ------------------------------------------------------------
# POST Endpoint (Real Use)
# ------------------------------------------------------------
@router.post("/portfolio")
def portfolio_post(payload: dict):
    """
    POST portfolio optimization with full control.
    Supports AGI-style evaluation for many properties.

    Expected payload:
    {
      "properties": [
        { "id": "P-A", "current_value": 1000000, "noi": 60000, "risk_score": 0.3 },
        { "id": "P-B", "current_value": 800000,  "noi": 45000, "risk_score": 0.5 }
      ],
      "risk_level": "medium"
    }
    """

    try:
        properties = payload.get("properties", None)
        risk_level = payload.get("risk_level", "medium")

        result = run_portfolio_optimization(properties=properties, risk_level=risk_level)

        # Memory logging for training AGI decision models
        save_event(
            "portfolio_agent",
            "portfolio_recommendation",
            {"risk_level": risk_level, "properties": properties, "result": result},
        )

        return {
            "status": "success",
            "agent": "portfolio_agent",
            "risk_level": risk_level,
            "properties_count": len(properties) if properties else 0,
            "optimization_decision": result,
            "agent_chain": ["churn_agent", "forecasting_agent", "pricing_agent", "portfolio_agent"]
        }

    except Exception as e:
        return {
            "status": "error",
            "agent": "portfolio_agent",
            "message": str(e),
        }


# ------------------------------------------------------------
# Standalone Debug
# ------------------------------------------------------------
if __name__ == "__main__":
    sample_payload = {
        "properties": [
            {"id": "Property_A", "current_value": 1200000, "noi": 68000, "risk_score": 0.25},
            {"id": "Property_B", "current_value": 750000,  "noi": 43000, "risk_score": 0.55},
        ],
        "risk_level": "medium",
    }
    test = portfolio_post(sample_payload)
    print(test)
