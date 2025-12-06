# tenant_churn_agent.py
"""
This agent handles tenant churn prediction.
It calls churn_service.py and returns clean JSON output.
"""

from services.churn_service import run_churn_prediction


def tenant_churn_agent(property_id="property_A"):
    """
    Main agent function called by backend routes.
    property_id supports multi-property input.
    """

    try:
        result = run_churn_prediction(property_id)

        return {
            "status": "success",
            "property_id": property_id,
            "churn_score": result.get("churn_score"),
            "risk_level": result.get("risk_level"),
            "top_factors": result.get("top_factors"),
            "tenant_count": result.get("tenant_count")
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }


# ------------------------------------------------------------
# Standalone test (python tenant_churn_agent.py)
# ------------------------------------------------------------
if __name__ == "__main__":
    output = tenant_churn_agent("property_A")
    print(output)
