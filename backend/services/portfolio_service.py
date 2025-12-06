# backend/services/portfolio_service.py

"""
This service performs portfolio optimization across properties.
Properties with lower risk_score receive higher allocation weight.
"""

from typing import List, Dict, Optional


def run_portfolio_optimization(
    properties: Optional[List[Dict]] = None,
    risk_level: str = "medium",
) -> dict:
    """
    TEMP MOCK IMPLEMENTATION.
    Real version could use portfolio theory (Sharpe ratio, mean-variance, Monte Carlo, etc.)
    """

    # Default properties if none provided
    if not properties:
        properties = [
            {"id": "property_A", "current_value": 1000000, "noi": 60000, "risk_score": 0.3},
            {"id": "property_B", "current_value": 800000, "noi": 45000, "risk_score": 0.5},
            {"id": "property_C", "current_value": 650000, "noi": 38000, "risk_score": 0.4},
        ]

    # Avoid division by zero
    eps = 0.0001

    # Compute inverse-risk weights
    total_inverse_risk = sum(1.0 / max(p.get("risk_score", eps), eps) for p in properties)

    allocation = []
    for p in properties:
        inv_risk = 1.0 / max(p.get("risk_score", eps), eps)
        weight = inv_risk / total_inverse_risk

        allocation.append({
            "id": p["id"],
            "suggested_weight": weight,
            "current_value": p.get("current_value"),
            "risk_score": p.get("risk_score"),
        })

    return {
        "risk_level": risk_level,
        "properties_count": len(properties),
        "allocation": allocation,
        "note": "Mock portfolio optimization. Replace with real model."
    }
