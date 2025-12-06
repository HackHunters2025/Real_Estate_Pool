"""
Portfolio Optimization Service
Allocates capital across properties based on risk, NOI performance,
and portfolio strategy (low / medium / high risk tolerance).
"""

from typing import List, Dict, Optional
import numpy as np


def _risk_adjustment_factor(risk_level: str) -> float:
    """
    Determines aggressiveness of investment scaling.
    """
    mapping = {
        "low": 0.4,      # Safer distribution, defensive
        "medium": 1.0,   # Balanced
        "high": 1.8      # Aggressive
    }
    return mapping.get(risk_level.lower(), 1.0)


def run_portfolio_optimization(
    properties: Optional[List[Dict]] = None,
    risk_level: str = "medium",
) -> dict:

    # -----------------------------------------------------
    # Default mock properties (in case frontend sends none)
    # -----------------------------------------------------
    if not properties:
        properties = [
            {"id": "property_A", "current_value": 1000000, "noi": 60000, "risk_score": 0.3},
            {"id": "property_B", "current_value": 800000, "noi": 45000, "risk_score": 0.5},
            {"id": "property_C", "current_value": 650000, "noi": 38000, "risk_score": 0.4},
        ]

    eps = 0.0001
    risk_factor = _risk_adjustment_factor(risk_level)

    # -----------------------------------------------------
    # Compute Expected Return (NOI / Value)
    # -----------------------------------------------------
    for p in properties:
        p["expected_return"] = round((p["noi"] / max(p["current_value"], eps)), 4)

    # -----------------------------------------------------
    # Compute allocation weight (Inverse risk × Adjusted for expected return)
    # -----------------------------------------------------
    raw_scores = []
    for p in properties:
        inv_risk = 1 / max(p.get("risk_score", eps), eps)
        score = inv_risk * (p["expected_return"] * 1.5) * risk_factor  # Higher return rewarded
        raw_scores.append(score)

    total_score = sum(raw_scores)

    # -----------------------------------------------------
    # Build Allocation Table
    # -----------------------------------------------------
    allocation = []
    for p, score in zip(properties, raw_scores):
        weight = score / max(total_score, eps)
        diversification_penalty = (1 / len(properties)) * 0.1  # encourage spreading capital

        final_weight = max(weight - diversification_penalty, 0)
        allocation.append({
            "id": p["id"],
            "risk_score": p["risk_score"],
            "expected_return": p["expected_return"],
            "suggested_weight": round(final_weight, 4),
            "investment_priority_score": round(score, 4),
        })

    # Sort highest allocation scored -> top recommended
    allocation_sorted = sorted(allocation, key=lambda x: x["investment_priority_score"], reverse=True)

    return {
        "strategy_risk_level": risk_level,
        "properties_evaluated": len(properties),
        "top_recommendation": allocation_sorted[0]["id"],
        "allocation_plan": allocation_sorted,
        "explanation": (
            "Weights are based on inverse risk and expected return. "
            "Diversification penalty applied to avoid over-allocation to one asset."
        )
    }
