# occupancy_agent.py
"""
This agent handles occupancy forecasting requests.
It calls occupancy_service.py and returns JSON output.
"""

from services.occupancy_service import run_occupancy_forecast


def occupancy_agent(property_id="property_A"):
    """
    Main agent function.
    property_id allows switching between different buildings.
    """

    try:
        result = run_occupancy_forecast(property_id)

        return {
            "status": "success",
            "property_id": property_id,
            "months": result.get("months"),
            "occupancy_rate": result.get("occupancy_rate"),
            "trend": result.get("trend"),
            "current_occupancy": result.get("current_occupancy"),
            "predicted_future_rate": result.get("predicted_future_rate")
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }


# ------------------------------------------------------------
# Standalone test (python occupancy_agent.py)
# ------------------------------------------------------------
if __name__ == "__main__":
    output = occupancy_agent("property_A")
    print(output)
