# backend/agents/maintenance_agent.py

from fastapi import APIRouter
import time

from services.maintenance_service import predict_failure
from services.iot_sim_service import generate_hvac_series
from services.graph_store import save_event

router = APIRouter()

# 👉 Basic prediction on provided sensor input
@router.post("/maintenance/predict")
def maintenance(payload: dict):
    start = time.time()

    sensor_values = payload.get("sensor_data")
    result = predict_failure(sensor_values)

    duration = time.time() - start

    save_event(
        agent_name="maintenance_agent",
        event_type="failure_check",
        payload={"input": sensor_values, "result": result},
        success=(result["status"] == "NORMAL"),
        chain=["maintenance_agent"],
        duration=duration
    )

    return {
        "agent": "maintenance_agent",
        "maintenance_status": result,
        "execution_ms": round(duration * 1000, 2)
    }


# 👉 Generate real-time IoT stream (for UI simulation)
@router.get("/maintenance/simulate")
def maintenance_simulated(samples: int = 5):
    """
    Generate a live-like simulated IoT sensor stream for demo.
    Useful for UI, charts, and hackathon wow-factor.
    """
    data = generate_hvac_series(samples)

    # Single pass check
    predictions = [predict_failure(d) for d in data]

    save_event(
        agent_name="maintenance_agent",
        event_type="iot_simulation",
        payload={"generated_samples": data, "predictions": predictions},
        success=True,
        chain=["maintenance_agent"],
        duration=0
    )

    return {
        "agent": "maintenance_agent",
        "simulated_sensor_data": data,
        "predictions": predictions
    }
