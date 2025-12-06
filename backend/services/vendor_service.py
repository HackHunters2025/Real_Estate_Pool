# backend/services/vendor_service.py

def detect_vendor_anomaly(history: list, new_invoice: float):
    """
    history: [1000, 1200, 900]
    new_invoice: 1800
    If new invoice > avg + 30% => flag anomaly
    """

    if not history or new_invoice is None:
        return {"status": "NO_DATA"}

    avg_spend = sum(history) / len(history)
    threshold = avg_spend * 1.3

    if new_invoice > threshold:
        return {
            "status": "OVERSPEED_DETECTED",
            "avg_spend": avg_spend,
            "new_invoice": new_invoice
        }

    return {
        "status": "NORMAL",
        "avg_spend": avg_spend,
        "new_invoice": new_invoice
    }
