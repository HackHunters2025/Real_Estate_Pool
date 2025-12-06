# backend/agents/esg_compliance_agent.py
from fastapi import APIRouter
from services.esg_rules_service import check_esg_compliance

router = APIRouter()

@router.post("/esg/check")
def esg_check(payload: dict):
    energy = payload.get("energy_usage")
    building_name = payload.get("property")

    result = check_esg_compliance(energy, building_name)
    return {"agent": "esg_compliance_agent", "compliance": result}
