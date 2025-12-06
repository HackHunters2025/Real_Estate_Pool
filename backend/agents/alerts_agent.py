# backend/agents/alerts_agent.py

from fastapi import APIRouter
from services.alerts_service import classify_severity
from services.graph_store import get_recent_events

router = APIRouter()

@router.get("/alerts/dashboard")
def alerts_dashboard():
    """
    Build alerts based on recent agent_chain decisions stored in memory.
    """
    recent = get_recent_events(limit=5)

    # naive example: extract last ESG, Maintenance, Vendor statuses if present
    esg_status = None
    maint_status = None
    vendor_status = None

    for ev in reversed(recent):
        payload = ev.get("payload", {})
        if "esg_result" in payload and not esg_status:
            esg_status = payload["esg_result"]
        if "maintenance_status" in payload and not maint_status:
            maint_status = payload["maintenance_status"]
        if "overspend_detected" in payload and not vendor_status:
            vendor_status = payload["overspend_detected"]

    alerts = classify_severity(esg_status, maint_status, vendor_status)

    return {
        "agent": "alerts_agent",
        "alerts": alerts,
        "source_events": recent
    }
