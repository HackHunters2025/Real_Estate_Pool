# backend/agents/vendor_cost_agent.py
from fastapi import APIRouter
from services.vendor_service import detect_vendor_anomaly

router = APIRouter()

@router.post("/vendor/analyze")
def vendor_analyze(payload: dict):
    history = payload.get("history")
    new_invoice = payload.get("invoice_amount")

    result = detect_vendor_anomaly(history, new_invoice)
    return {"agent": "vendor_cost_agent", "overspend_detected": result}
