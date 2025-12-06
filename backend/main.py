from fastapi import FastAPI
from agents.lease_nlp_agent import router as lease_router
from agents.esg_compliance_agent import router as esg_router
from agents.pricing_agent import router as pricing_router
from agents.maintenance_agent import router as maintenance_router
from agents.vendor_cost_agent import router as vendor_router
from agents.news_agent import router as news_router
from agents.alerts_agent import router as alerts_router
from agents.memory_agent import router as memory_router
app = FastAPI(title="SingularityNET Real Estate Intelligence Agents")

# Register All Developer 3 Agents
app.include_router(lease_router)
app.include_router(esg_router)
app.include_router(pricing_router)
app.include_router(maintenance_router)
app.include_router(vendor_router)
app.include_router(news_router)
app.include_router(alerts_router)
app.include_router(memory_router)

@app.get("/")
def root():
    return {"message": "Real Estate AI Agents Active"}
