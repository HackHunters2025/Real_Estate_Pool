import sys
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from agents.lease_nlp_agent import router as lease_router
from agents.esg_compliance_agent import router as esg_router
from agents.pricing_agent import router as pricing_router
from agents.maintenance_agent import router as maintenance_router
from agents.vendor_cost_agent import router as vendor_router
from agents.news_agent import router as news_router
from agents.alerts_agent import router as alerts_router
from agents.forecasting_agent import router as forecast_router
from agents.occupancy_agent import router as occupancy_router
from agents.tenant_churn_agent import router as churn_router
from agents.portfolio_agent import router as portfolio_router
from agents.scenario_agent import router as scenario_router
from agents.memory_agent import router as memory_router

sys.path.append(os.path.dirname(__file__))

app = FastAPI(title="SingularityNET Real Estate Intelligence Agents")

# ==========================
#       CORS MIDDLEWARE
# ==========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173", 
        "http://127.0.0.1:5173"
    ],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================
#     REGISTER ROUTERS
# ==========================
app.include_router(lease_router)
app.include_router(esg_router)
app.include_router(pricing_router)
app.include_router(maintenance_router)
app.include_router(vendor_router)
app.include_router(news_router)
app.include_router(alerts_router)
app.include_router(memory_router)
app.include_router(forecast_router)
app.include_router(occupancy_router)
app.include_router(churn_router)
app.include_router(portfolio_router)
app.include_router(scenario_router)


@app.get("/")
def root():
    return {"message": "Real Estate AI Agents Active"}