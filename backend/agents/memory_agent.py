from fastapi import APIRouter
from services.graph_store import get_recent_events, get_events_by_agent, clear_memory

router = APIRouter()

@router.get("/memory/recent")
def memory_recent(limit: int = 5):
    return {"recent_events": get_recent_events(limit)}

@router.get("/memory/by-agent")
def memory_by_agent(agent_name: str):
    return get_events_by_agent(agent_name)

@router.delete("/memory/clear")
def memory_clear():
    return clear_memory()
    return {"status": "memory_cleared"}