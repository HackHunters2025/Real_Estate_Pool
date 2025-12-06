# backend/agents/occupancy_agent.py
"""
Occupancy Forecasting Agent
Calls occupancy_service.py and returns occupancy prediction,
trend direction, and future occupancy rate.
"""

from fastapi import APIRouter, Query
from services.occupancy_service import run_occupancy_forecast

router = APIRouter()

# ------------------------------------------------------------
# GET Endpoint
# ------------------------------------------------------------
@router.get("/occupancy")
def occupancy_get(property_id: str = Query("property_A"), months_ahead: int = Query(3)):
    """
    GET occupancy forecast.
    Example:
    /occupancy?property_id=property_A&months_ahead=3
    """
    try:
        result = run_occupancy_forecast(property_id, months_ahead)

        return {
            "status": "success",
            "agent": "occupancy_agent",
            "property_id": property_id,
            "months_requested": months_ahead,
            "forecast_months": result.get("months"),
            "occupancy_rate": result.get("occupancy_rate"),
            "trend": result.get("trend"),
            "current_occupancy": result.get("current_occupancy"),
            "predicted_future_rate": result.get("predicted_future_rate")
        }

    except Exception as e:
        return {
            "status": "error",
            "property_id": property_id,
            "message": str(e)
        }


# ------------------------------------------------------------
# POST Endpoint
# ------------------------------------------------------------
@router.post("/occupancy")
def occupancy_post(payload: dict):
    """
    POST occupancy forecast.
    Expected JSON Body:
    {
        "property_id": "property_A",
        "months_ahead": 3
    }
    """
    try:
        property_id = payload.get("property_id", "property_A")
        months_ahead = payload.get("months_ahead", 3)

        result = run_occupancy_forecast(property_id, months_ahead)

        return {
            "status": "success",
            "agent": "occupancy_agent",
            "property_id": property_id,
            "months_requested": months_ahead,
            "forecast_months": result.get("months"),
            "occupancy_rate": result.get("occupancy_rate"),
            "trend": result.get("trend"),
            "current_occupancy": result.get("current_occupancy"),
            "predicted_future_rate": result.get("predicted_future_rate")
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }


# ------------------------------------------------------------
# Standalone Test
# ------------------------------------------------------------
if __name__ == "__main__":
    print(occupancy_get("property_A", 3))
