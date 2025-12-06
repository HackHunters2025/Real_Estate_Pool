"""
Scenario Simulation Service
Predicts the financial impact of Rent, Occupancy, and Expense changes.
Generates monthly projections and confidence scoring.
"""

import numpy as np


def run_scenario(
    property_id: str,
    rent_change_pct: float,
    occupancy_change_pct: float,
    expense_change_pct: float,
    months_ahead: int,
) -> dict:

    # -----------------------------------------------------------------
    # BASE VALUES (To be dynamically loaded later; placeholders for now)
    # -----------------------------------------------------------------
    base_rent = 200000          # Monthly rent revenue
    base_occupancy = 0.85       # 85% of units filled
    base_expenses = 120000      # Monthly operating expenses

    # -----------------------------------------------------------------
    # Convert percent → multiplier
    # -----------------------------------------------------------------
    rent_multiplier = 1 + rent_change_pct / 100
    occupancy_multiplier = 1 + occupancy_change_pct / 100
    expense_multiplier = 1 + expense_change_pct / 100

    # -----------------------------------------------------------------
    # Confidence score (risk-based)
    # High adjustments = low certainty
    # -----------------------------------------------------------------
    total_change_factor = abs(rent_change_pct) + abs(occupancy_change_pct) + abs(expense_change_pct)
    confidence_score = round(max(0.15, 1.0 - total_change_factor / 100), 2)

    # -----------------------------------------------------------------
    # Sensitivity Impact Weighting
    # -----------------------------------------------------------------
    sensitivity = {
        "rent_sensitivity": abs(rent_change_pct) * 0.6,
        "occupancy_sensitivity": abs(occupancy_change_pct) * 0.4,
        "expense_sensitivity": abs(expense_change_pct) * 0.8
    }
    sensitivity_rank = sorted(sensitivity, key=lambda k: sensitivity[k], reverse=True)

    # -----------------------------------------------------------------
    # Projections (compound each month)
    # -----------------------------------------------------------------
    projection = []
    current_rent = base_rent
    current_occupancy = base_occupancy
    current_expenses = base_expenses

    for month in range(1, months_ahead + 1):
        current_rent *= rent_multiplier
        current_occupancy = min(max(current_occupancy * occupancy_multiplier, 0), 1)
        current_expenses *= expense_multiplier

        revenue = current_rent * current_occupancy
        noi = revenue - current_expenses

        projection.append({
            "month": month,
            "occupancy_rate": float(round(current_occupancy, 3)),
            "projected_revenue": float(round(revenue, 2)),
            "projected_expenses": float(round(current_expenses, 2)),
            "projected_NOI": float(round(noi, 2)),
        })

    final_noi = projection[-1]["projected_NOI"]
    impact_classification = "positive" if final_noi > 0 else "negative"

    # -----------------------------------------------------------------
    # Output JSON Response
    # -----------------------------------------------------------------
    return {
        "property_id": property_id,
        "inputs_used": {
            "rent_change_pct": rent_change_pct,
            "occupancy_change_pct": occupancy_change_pct,
            "expense_change_pct": expense_change_pct,
            "months_ahead": months_ahead
        },
        "confidence_score": confidence_score,
        "impact_classification": impact_classification,
        "sensitivity_rank": sensitivity_rank,
        "final_month_NOI": final_noi,
        "projection_monthly": projection
    }
