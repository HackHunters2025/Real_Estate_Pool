# backend/agents/scenario_agent.py
"""
This agent handles scenario simulation:
e.g. what happens to cash flow / NOI if rent, occupancy, or expenses change.

It calls run_scenario from scenario_service.py and returns formatted JSON.
"""

from fastapi import APIRouter, Query
from services.scenario_service import run_scenario

router = APIRouter()


@router.get("/scenario")
def scenario_get(
    property_id: str = Query("property_A"),
    rent_change_pct: float = Query(0.0, description="Rent change in % (e.g., 5 for +5%)"),
    occupancy_change_pct: float = Query(0.0, description="Occupancy change in %"),
    expense_change_pct: float = Query(0.0, description="Expense change in %"),
    months_ahead: int = Query(6, description="Months ahead for scenario")
):
    """
    GET scenario simulation results.
    Example:
    /scenario?property_id=property_A&rent_change_pct=5&months_ahead=6
    """
    try:
        result = run_scenario(
            property_id=property_id,
            rent_change_pct=rent_change_pct,
            occupancy_change_pct=occupancy_change_pct,
            expense_change_pct=expense_change_pct,
            months_ahead=months_ahead,
        )

        return {
            "status": "success",
            "agent": "scenario_agent",
            "property_id": property_id,
            "inputs": {
                "rent_change_pct": rent_change_pct,
                "occupancy_change_pct": occupancy_change_pct,
                "expense_change_pct": expense_change_pct,
                "months_ahead": months_ahead,
            },
            "scenario_result": result,
        }
    except Exception as e:
        return {
            "status": "error",
            "agent": "scenario_agent",
            "message": str(e),
        }


@router.post("/scenario")
def scenario_post(payload: dict):
    """
    POST scenario simulation.

    Expected JSON payload:
    {
        "property_id": "property_A",
        "rent_change_pct": 5.0,
        "occupancy_change_pct": -3.0,
        "expense_change_pct": 2.0,
        "months_ahead": 6
    }
    """
    try:
        property_id = payload.get("property_id", "property_A")
        rent_change_pct = float(payload.get("rent_change_pct", 0.0))
        occupancy_change_pct = float(payload.get("occupancy_change_pct", 0.0))
        expense_change_pct = float(payload.get("expense_change_pct", 0.0))
        months_ahead = int(payload.get("months_ahead", 6))

        result = run_scenario(
            property_id=property_id,
            rent_change_pct=rent_change_pct,
            occupancy_change_pct=occupancy_change_pct,
            expense_change_pct=expense_change_pct,
            months_ahead=months_ahead,
        )

        return {
            "status": "success",
            "agent": "scenario_agent",
            "property_id": property_id,
            "inputs": {
                "rent_change_pct": rent_change_pct,
                "occupancy_change_pct": occupancy_change_pct,
                "expense_change_pct": expense_change_pct,
                "months_ahead": months_ahead,
            },
            "scenario_result": result,
        }
    except Exception as e:
        return {
            "status": "error",
            "agent": "scenario_agent",
            "message": str(e),
        }


# ------------------------------------------------------------
# Standalone test (python scenario_agent.py)
# ------------------------------------------------------------
if __name__ == "__main__":
    # Simple in-file test (GET-style call)
    test = scenario_get(
        property_id="property_A",
        rent_change_pct=5.0,
        occupancy_change_pct=-2.0,
        expense_change_pct=1.5,
        months_ahead=6,
    )
    print(test)
