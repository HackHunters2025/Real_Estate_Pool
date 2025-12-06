"""
Forecasting Agent
Handles financial forecasting using run_forecasting service.
Supports GET and POST requests.
"""

from fastapi import APIRouter, Query
from services.forecasting_service import run_forecasting

router = APIRouter()


@router.get("/forecast")
def forecast_get(
    property_id: str = Query("property_A"),
    current_rent: float = Query(None),
    months_ahead: int = Query(6),
    inflation_rate: float = Query(0.04)
):
    """
    GET financial forecast.
    Example:
    /forecast?property_id=property_A&current_rent=30000&months_ahead=6&inflation_rate=0.05
    """
    try:
        result = run_forecasting(
            property_id=property_id,
            current_rent=current_rent,
            months_ahead=months_ahead,
            inflation_rate=inflation_rate
        )

        return {
            "status": "success",
            "agent": "forecasting_agent",
            "property_id": property_id,
            "parameters": {
                "current_rent": current_rent,
                "months_ahead": months_ahead,
                "inflation_rate": inflation_rate
            },
            "forecast_result": result
        }
    except Exception as e:
        return {
            "status": "error",
            "property_id": property_id,
            "message": str(e)
        }


@router.post("/forecast")
def forecast_post(payload: dict):
    """
    POST financial forecast.
    Expected JSON:
    {
        "property_id": "property_A",
        "current_rent": 28000,
        "months_ahead": 6,
        "inflation_rate": 0.04
    }
    """
    try:
        property_id = payload.get("property_id", "property_A")
        current_rent = payload.get("current_rent")
        months_ahead = payload.get("months_ahead", 6)
        inflation_rate = payload.get("inflation_rate", 0.04)

        result = run_forecasting(
            property_id=property_id,
            current_rent=current_rent,
            months_ahead=months_ahead,
            inflation_rate=inflation_rate
        )

        return {
            "status": "success",
            "agent": "forecasting_agent",
            "property_id": property_id,
            "parameters": {
                "current_rent": current_rent,
                "months_ahead": months_ahead,
                "inflation_rate": inflation_rate
            },
            "forecast_result": result
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }


# Standalone Manual Test
if __name__ == "__main__":
    example = forecast_get("property_A", 30000, 6, 0.04)
    print(example)
