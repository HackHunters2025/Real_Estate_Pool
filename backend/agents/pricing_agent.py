# backend/agents/pricing_agent.py

from fastapi import APIRouter
import time

from services.pricing_service import recommend_price
from services.forecasting_service import simple_forecast
from services.esg_rules_service import check_esg_compliance
from services.graph_store import save_event, get_events_by_agent

router = APIRouter()


# ---------- SIMPLE PRICING ENDPOINT (keep as is for basic use) ----------
@router.post("/pricing/recommend")
def pricing(payload: dict):
    current_rent = payload.get("current_rent")
    demand_score = payload.get("demand_score", 0.5)

    recommended = recommend_price(current_rent, demand_score)

    return {
        "agent": "pricing_agent",
        "recommended_rent": recommended
    }


# ---------- HELPER FUNCTIONS FOR AGENTIC LOGIC ----------

def compute_confidence_and_risk(demand_score: float, esg_status: str):
    """
    Simple heuristic:
    - Higher demand => higher confidence
    - ESG FAIL => lower confidence, higher risk
    """
    base_conf = 0.5 + (demand_score - 0.5) * 0.6  # weight demand
    base_conf = max(0.1, min(base_conf, 0.95))

    if esg_status == "FAIL":
        base_conf -= 0.15

    base_conf = max(0.05, min(base_conf, 0.99))

    if base_conf >= 0.75:
        risk = "low"
    elif base_conf >= 0.45:
        risk = "medium"
    else:
        risk = "high"

    return round(base_conf, 2), risk


def compute_learning_adjustment():
    """
    Looks at past decisions in memory.
    If too many ESG FAILs, system becomes more conservative.
    """
    events = get_events_by_agent("pricing_agent_chain")
    if not events:
        return 1.0, "No prior decisions, neutral policy."

    last = events[-10:]  # last 10 decisions
    fail_count = 0
    total = 0

    for e in last:
        payload = e.get("payload", {})
        esg = payload.get("esg_check_result", {})
        if esg.get("status") == "FAIL":
            fail_count += 1
        total += 1

    if total == 0:
        return 1.0, "No usable ESG records."

    fail_ratio = fail_count / total

    # If more than 40% of recent decisions failed ESG -> reduce aggressiveness
    if fail_ratio > 0.4:
        return 0.97, f"High ESG fail ratio ({fail_ratio:.2f}), applying -3% safety adjustment."
    elif fail_ratio > 0.2:
        return 0.985, f"Moderate ESG fail ratio ({fail_ratio:.2f}), applying -1.5% safety adjustment."
    else:
        return 1.0, f"ESG fail ratio acceptable ({fail_ratio:.2f}), no adjustment."


# ---------- AGENTIC PRICING ENDPOINT (CHAIN + FEEDBACK + LEARNING) ----------

@router.post("/pricing/agentic_recommend")
def pricing_agentic(payload: dict):
    """
    Agentic Workflow:
    1. Recommend new price based on demand (pricing_agent).
    2. Forecast revenue for next 6 months (forecasting_agent).
    3. Check ESG compliance at that scenario (esg_compliance_agent).
    4. AUTO-CORRECT price if ESG FAIL (feedback loop).
    5. Apply learning adjustment based on past ESG failures (self-learning).
    6. Save full decision trail into memory.
    """

    start_time = time.time()

    current_rent = payload.get("current_rent")
    demand_score = payload.get("demand_score", 0.5)
    property_name = payload.get("property", "Property_A")
    energy_usage = payload.get("energy_usage", 1150)
    historical_rents = payload.get("historical_rents", [current_rent] * 6)

    # 1) Base price suggestion
    base_price = recommend_price(current_rent, demand_score)

    # 2) Forecast using base price
    forecast_result = simple_forecast(historical_rents, base_price)

    # 3) ESG check
    esg_result = check_esg_compliance(energy_usage, property_name)
    esg_status = esg_result.get("status", "UNKNOWN")

    # 4) Feedback loop: auto-adjust if ESG FAIL
    esg_adjusted_price = base_price
    esg_adjustment_applied = False
    if esg_status == "FAIL":
        esg_adjusted_price = round(base_price * 0.97, 2)  # reduce 3%
        esg_adjustment_applied = True

    # 5) Self-learning based on past memory
    learning_factor, learning_note = compute_learning_adjustment()
    final_price = round(esg_adjusted_price * learning_factor, 2)

    # 6) Confidence + risk
    confidence, risk_level = compute_confidence_and_risk(demand_score, esg_status)

    result = {
        "agent_chain": [
            "pricing_agent",
            "forecasting_agent",
            "esg_compliance_agent"
        ],
        "current_rent": current_rent,
        "base_suggested_rent": base_price,
        "esg_adjusted_rent": esg_adjusted_price,
        "final_recommended_rent": final_price,
        "confidence": confidence,
        "risk_level": risk_level,
        "esg_status": esg_status,
        "esg_adjustment_applied": esg_adjustment_applied,
        "learning_note": learning_note,
        "forecast_next_6_months": forecast_result,
        "esg_check_result": esg_result
    }

    duration = time.time() - start_time

    # Save to memory
    save_event(
        agent_name="pricing_agent_chain",
        event_type="pricing_decision",
        payload=result,
        success=True,
        chain=result["agent_chain"],
        duration=duration
    )

    return {
        "execution_ms": round(duration * 1000, 2),
        **result
    }
