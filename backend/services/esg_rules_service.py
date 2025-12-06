# backend/services/esg_rules_service.py

import json
import os

# Dynamically build path no matter where pytest or uvicorn is run
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH = os.path.join(BASE_DIR, "data/config/esg_thresholds.json")

def check_esg_compliance(energy_usage: float, building_name: str):
    if not os.path.exists(CONFIG_PATH):
        return {"status": "CONFIG_MISSING", "path_checked": CONFIG_PATH}

    with open(CONFIG_PATH, "r") as file:
        thresholds = json.load(file)

    limit = thresholds.get("energy_kwh_limit", 1200)
    penalty_per_100 = thresholds.get("esg_penalty_rate", 50)

    if energy_usage <= limit:
        return {
            "status": "PASS",
            "details": "Energy usage is within allowed ESG limits",
            "allowed_limit_kwh": limit
        }

    extra = energy_usage - limit
    estimated_penalty = (extra / 100) * penalty_per_100

    return {
        "status": "FAIL",
        "details": f"Exceeded by {extra} kWh",
        "allowed_limit_kwh": limit,
        "projected_penalty_$": round(estimated_penalty, 2)
    }
