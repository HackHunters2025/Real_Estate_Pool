# backend/main.py

from fastapi import FastAPI
from pydantic import BaseModel

# Import services
from backend.services.churn_service import run_churn_prediction
from backend.services.forecasting_service import run_forecasting
from backend.services.occupancy_service import run_occupancy_forecast

# ---------------------------------------------------------
# Initialize FastAPI App
# ---------------------------------------------------------
app = FastAPI(
    title="SingularityNET Real Estate Intelligence API",
    description="AI-powered forecasting, churn analysis, and occupancy intelligence",
    version="1.0.0"
)

# ---------------------------------------------------------
# Request Models
# ---------------------------------------------------------

class ChurnRequest(BaseModel):
    property_id: str = "property_A"

class ForecastRequest(BaseModel):
    property_id: str = "property_A"
    months_ahead: int = 6

class OccupancyRequest(BaseModel):
    property_id: str = "property_A"
    months_ahead: int = 3


# ---------------------------------------------------------
# Root Endpoint
# ---------------------------------------------------------

@app.get("/")
def home():
    return {"message": "Real Estate Intelligence API is running!"}


# ---------------------------------------------------------
# -----------     CHURN ENDPOINTS     ----------------------
# ---------------------------------------------------------

@app.get("/churn")
def churn_get(property_id: str = "property_A"):
    """GET endpoint for churn prediction."""
    return run_churn_prediction(property_id)


@app.post("/churn")
def churn_post(request: ChurnRequest):
    """POST endpoint for churn prediction."""
    return run_churn_prediction(request.property_id)


# ---------------------------------------------------------
# -----------     FORECAST ENDPOINTS     -------------------
# ---------------------------------------------------------

@app.get("/forecast")
def forecast_get(property_id: str = "property_A"):
    """GET endpoint for financial forecasting."""
    return run_forecasting(property_id)


@app.post("/forecast")
def forecast_post(request: ForecastRequest):
    """POST endpoint for financial forecasting."""
    return run_forecasting(request.property_id)


# ---------------------------------------------------------
# -----------     OCCUPANCY ENDPOINTS     ------------------
# ---------------------------------------------------------

@app.get("/occupancy")
def occupancy_get(property_id: str = "property_A"):
    """GET endpoint for occupancy forecasting."""
    return run_occupancy_forecast(property_id)


@app.post("/occupancy")
def occupancy_post(request: OccupancyRequest):
    """POST endpoint for occupancy forecasting."""
    return run_occupancy_forecast(request.property_id)


# ---------------------------------------------------------
# Run the app:
#  uvicorn backend.main:app --reload
# ---------------------------------------------------------
