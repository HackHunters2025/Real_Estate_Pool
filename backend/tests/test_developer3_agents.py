# backend/tests/test_developer3_agents.py
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# -------- Lease NLP Agent Test --------
def test_lease_extraction():
    sample_text = """
    Rent Amount: 28000
    Start Date: 01/05/2023
    End Date: 01/05/2025
    Escalation: 5%
    Renewal Clause: Yes
    """
    files = {"file": ("lease.txt", sample_text)}
    response = client.post("/lease/extract", files=files)
    data = response.json()
    assert "extracted_fields" in data
    assert data["extracted_fields"]["monthly_rent"] == "28000"


# -------- ESG Agent Test --------
def test_esg_compliance():
    payload = {"energy_usage": 1450, "property": "Property_A"}
    response = client.post("/esg/check", json=payload)
    data = response.json()
    assert "compliance" in data
    assert data["compliance"]["status"] in ["PASS", "FAIL"]


# -------- Pricing Agent Test --------
def test_pricing_recommendation():
    payload = {"current_rent": 28000, "demand_score": 0.8}
    response = client.post("/pricing/recommend", json=payload)
    data = response.json()
    assert "recommended_rent" in data
    assert type(data["recommended_rent"]) == float or int


# -------- Maintenance Agent Test --------
def test_maintenance_prediction():
    payload = {"sensor_data": [82, 63, 130]}
    response = client.post("/maintenance/predict", json=payload)
    data = response.json()
    assert "maintenance_status" in data
    assert data["maintenance_status"]["status"] in ["NORMAL", "FAILURE_PREDICTED"]


# -------- Vendor Anomaly Agent Test --------
def test_vendor_cost_anomaly():
    payload = {
        "history": [1200, 1300, 900, 1100],
        "invoice_amount": 1800
    }
    response = client.post("/vendor/analyze", json=payload)
    data = response.json()
    
    # It must detect an anomaly here
    assert "overspend_detected" in data
    assert data["overspend_detected"]["status"] in ["NORMAL", "OVERSPEED_DETECTED"]
