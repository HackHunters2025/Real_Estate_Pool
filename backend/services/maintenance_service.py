# backend/services/maintenance_service.py

def predict_failure(sensor_values: list):
    """
    sensor_values is a list of integers: [temp, vibration, pressure]
    Hackathon rule: any value above threshold triggers maintenance alert
    """

    THRESHOLDS = {
        "temperature": 80,
        "vibration": 60,
        "pressure": 120
    }

    if not sensor_values or len(sensor_values) < 3:
        return {"status": "DATA_INSUFFICIENT"}

    temperature, vibration, pressure = sensor_values

    alerts = []
    if temperature > THRESHOLDS["temperature"]:
        alerts.append("High Temperature — Cooling Required")
    if vibration > THRESHOLDS["vibration"]:
        alerts.append("Abnormal Vibration — Bearing Fault Possible")
    if pressure > THRESHOLDS["pressure"]:
        alerts.append("Pressure Spike — Leak Warning")

    if alerts:
        return {"status": "FAILURE_PREDICTED", "alerts": alerts}

    return {"status": "NORMAL", "alerts": []}
