"""
Scenario Simulation Agent
---
Predicts the impact of changes in:
- rent
- occupancy
- expenses

Outputs: updated NOI, profit curve, risk impact, sensitivity factors.

Part of Decentralized Multi-Agent Pipeline:
pricing → churn → forecast → scenario simulation → portfolio optimization
"""

from fastapi import APIRouter, Query
from services.scenario_service import run_scenario
from services.graph_store import save_event

router = APIRouter()


# ------------------------------------------------------------
# GET Endpoint (Quick Test)
# ------------------------------------------------------------
@router.get("/scenario")
def scenario_get(
    property_id: str = Query("property_A"),
    rent_change_pct: float = Query(0.0),
    occupancy_change_pct: float = Query(0.0),
    expense_change_pct: float = Query(0.0),
    months_ahead: int = Query(6),
):
    try:
        result = run_scenario(
            property_id=property_id,
            rent_change_pct=rent_change_pct,
            occupancy_change_pct=occupancy_change_pct,
            expense_change_pct=expense_change_pct,
            months_ahead=months_ahead,
        )

        payload = {
            "status": "success",
            "agent": "scenario_agent",
            "agent_chain": [
                "forecasting_agent",
                "pricing_agent",
                "scenario_agent"
            ],
            "property_id": property_id,
            "input_scenario": {
                "rent_change_pct": rent_change_pct,
                "occupancy_change_pct": occupancy_change_pct,
                "expense_change_pct": expense_change_pct,
                "months_ahead": months_ahead,
            },
            "scenario_result": result,
        }

        save_event("scenario_agent", "scenario_simulation", payload)
        return payload

    except Exception as e:
        return {"status": "error", "agent": "scenario_agent", "message": str(e)}


# ------------------------------------------------------------
# POST Endpoint (Real Payload)
# ------------------------------------------------------------
@router.post("/scenario")
def scenario_post(payload: dict):
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

        response = {
            "status": "success",
            "agent": "scenario_agent",
            "property_id": property_id,
            "agent_chain": [
                "forecasting_agent",
                "portfolio_agent",
                "scenario_agent"
            ],
            "input_scenario": {
                "rent_change_pct": rent_change_pct,
                "occupancy_change_pct": occupancy_change_pct,
                "expense_change_pct": expense_change_pct,
                "months_ahead": months_ahead,
            },
            "scenario_result": result,
        }

        save_event("scenario_agent", "scenario_simulation", response)
        return response

    except Exception as e:
        return {"status": "error", "agent": "scenario_agent", "message": str(e)}


# ------------------------------------------------------------
# Local Debug
# ------------------------------------------------------------
if __name__ == "__main__":
    test = scenario_get(
        property_id="property_A",
        rent_change_pct=5,
        occupancy_change_pct=-2,
        expense_change_pct=1,
        months_ahead=6,
    )
    print(test)
