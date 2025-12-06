# backend/agents/news_agent.py

from fastapi import APIRouter
from services.news_service import analyze_market_sentiment

router = APIRouter()

@router.get("/news/sentiment")
def news_sentiment(city: str = "Bengaluru"):
    result = analyze_market_sentiment(city)
    return {
        "agent": "news_sentiment_agent",
        "result": result
    }
