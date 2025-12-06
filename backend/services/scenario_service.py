# backend/services/scenario_service.py

"""
This service performs scenario simulations.
It applies percentage changes to rent, occupancy, expenses,
and computes a mock financial impact score.
"""

def run_scenario(
    property_id: str,
    rent_change_pct: float,
    occupancy_change_pct: float,
    expense_change_pct: float,
    months_ahead: int,
) -> dict:
    """
    TEMP MOCK IMPLEMENTATION.
    Replace this with a real model during final integration.
    """

    # Mock financial impact formula
    # (positive rent change increases impact, negative occupancy or higher expenses reduces it)
    impact_score = (
        rent_change_pct * 0.6
        + occupancy_change_pct * 0.3
        - expense_change_pct * 0.5
    )

    # Mock monthly projections
    monthly_projection = [
        {
            "month": i + 1,
            "mock_noi_change": impact_score * (i + 1) * 100
        }
        for i in range(months_ahead)
    ]

    return {
        "property_id": property_id,
        "inputs": {
            "rent_change_pct": rent_change_pct,
            "occupancy_change_pct": occupancy_change_pct,
            "expense_change_pct": expense_change_pct,
            "months_ahead": months_ahead
        },
        "impact_score": impact_score,
        "projection": monthly_projection,
        "note": "Mock scenario simulation. Replace with real financial engine."
    }
