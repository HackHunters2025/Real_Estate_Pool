# backend/services/nlp_lease_service.py

import re

def extract_lease_terms(text: str):
    """
    Simple regex/Lite-NLP lease extraction
    Works for hackathon demo — replace w/ LLM later for production
    """

    rent = re.search(r"(rent|monthly payment).{0,20}?(\d{4,6})", text, re.I)
    start_date = re.search(r"(start date|lease begins).{0,20}?(\d{2}/\d{2}/\d{4})", text, re.I)
    end_date = re.search(r"(end date|lease expires).{0,20}?(\d{2}/\d{2}/\d{4})", text, re.I)
    escalation = re.search(r"(escalation|increase).{0,20}?(\d{1,2}%)", text, re.I)
    penalty = re.search(r"(late fee|penalty).{0,30}?(\d{2,4})", text, re.I)

    return {
        "monthly_rent": rent.group(2) if rent else "Not Found",
        "lease_start": start_date.group(2) if start_date else "Not Found",
        "lease_end": end_date.group(2) if end_date else "Not Found",
        "rent_escalation": escalation.group(2) if escalation else "Not Found",
        "penalty_fee": penalty.group(2) if penalty else "Not Found"
    }
