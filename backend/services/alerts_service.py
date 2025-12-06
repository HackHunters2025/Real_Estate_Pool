# backend/services/alerts_service.py

def classify_severity(esg_status: dict, maint_status: dict, vendor_status: dict):
    alerts = []

    if esg_status and esg_status.get("status") == "FAIL":
        alerts.append({"type": "ESG", "severity": "HIGH", "message": esg_status.get("details")})

    if maint_status and maint_status.get("status") == "FAILURE_PREDICTED":
        alerts.append({"type": "MAINTENANCE", "severity": "HIGH", "message": "HVAC failure predicted"})

    if vendor_status and vendor_status.get("status", "").startswith("OVER"):
        alerts.append({"type": "VENDOR", "severity": "MEDIUM", "message": "Vendor overspend detected"})

    if not alerts:
        alerts.append({"type": "SYSTEM", "severity": "LOW", "message": "No critical alerts"})

    return alerts
