# backend/utils/rules_engine.py

def evaluate_rules(value: float, threshold: float, return_message=True):
    """
    Generic comparison helper for sustainability and maintenance decisions.
    """
    if value > threshold:
        return {"status": "FAIL", "exceeded_by": value - threshold} if not return_message else \
            f"Value {value} exceeds allowed limit {threshold}"
    return {"status": "PASS", "margin": threshold - value} if not return_message else \
        f"Value {value} is within the safe range"
