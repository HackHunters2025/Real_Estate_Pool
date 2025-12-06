# backend/agents/lease_agent.py

from fastapi import APIRouter, UploadFile, File
from services.nlp_lease_service import extract_lease_terms
from services.graph_store import save_event
import time

router = APIRouter()

@router.post("/lease/extract")
async def lease_extract(file: UploadFile = File(...)):
    start = time.time()

    # Read file content
    content = await file.read()
    text = content.decode("utf-8", errors="ignore")  # Basic fallback for plain text/PDF extract

    # Call NLP service
    extracted = extract_lease_terms(text)

    duration = time.time() - start

    # Save memory
    save_event(
        agent_name="lease_extraction_agent",
        event_type="lease_parsing",
        payload=extracted,
        success=True,
        chain=["lease_extraction_agent"],
        duration=duration
    )

    return {
        "agent": "lease_extraction_agent",
        "filename": file.filename,
        "extracted_fields": extracted,
        "execution_ms": round(duration * 1000, 2)
    }
