# backend/agents/portfolio_agent.py
"""
This agent handles portfolio optimization:
e.g. how to allocate capital between properties to maximize returns
under a given risk level.

It calls run_portfolio_optimization from portfolio_service.py.
"""

from fastapi import APIRouter, Query
from services.portfolio_service import run_portfolio_optimization

router = APIRouter()


@router.get("/portfolio")
def portfolio_get(
    risk_level: str = Query("medium", description="Risk level: low / medium / high")
):
    """
    SIMPLE GET endpoint for testing.
    In reality, portfolio optimization usually needs a POST with a list of properties.
    Here we just call the service with a dummy payload.
    """
    try:
        # Example: service will internally use default example properties
        result = run_portfolio_optimization(
            properties=None,  # service can handle None as 'use default'
            risk_level=risk_level,
        )

        return {
            "status": "success",
            "agent": "portfolio_agent",
            "risk_level": risk_level,
            "optimization": result,
        }
    except Exception as e:
        return {
            "status": "error",
            "agent": "portfolio_agent",
            "message": str(e),
        }


@router.post("/portfolio")
def portfolio_post(payload: dict):
    """
    POST portfolio optimization.

    Expected JSON payload (example):

    {
      "properties": [
        {
          "id": "property_A",
          "current_value": 1000000,
          "noi": 60000,
          "risk_score": 0.3
        },
        {
          "id": "property_B",
          "current_value": 800000,
          "noi": 45000,
          "risk_score": 0.5
        }
      ],
      "risk_level": "medium"
    }
    """
    try:
        properties = payload.get("properties", [])
        risk_level = payload.get("risk_level", "medium")

        result = run_portfolio_optimization(
            properties=properties,
            risk_level=risk_level,
        )

        return {
            "status": "success",
            "agent": "portfolio_agent",
            "risk_level": risk_level,
            "properties_count": len(properties),
            "optimization": result,
        }
    except Exception as e:
        return {
            "status": "error",
            "agent": "portfolio_agent",
            "message": str(e),
        }


# ------------------------------------------------------------
# Standalone test (python portfolio_agent.py)
# ------------------------------------------------------------
if __name__ == "__main__":
    # Minimal sample properties for local testing
    sample_payload = {
        "properties": [
            {"id": "property_A", "current_value": 1000000, "noi": 60000, "risk_score": 0.3},
            {"id": "property_B", "current_value": 800000, "noi": 45000, "risk_score": 0.5},
        ],
        "risk_level": "medium",
    }
    test = portfolio_post(sample_payload)
    print(test)
