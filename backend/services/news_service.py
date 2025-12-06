# backend/services/news_service.py

import random

def analyze_market_sentiment(city: str):
    """
    Hackathon-friendly fake sentiment generator.
    Later you can replace with real HTTP call to a news API + sentiment model.
    """
    sentiments = ["bullish", "bearish", "neutral"]
    s = random.choice(sentiments)

    score_map = {"bullish": 0.8, "neutral": 0.5, "bearish": 0.2}
    return {
        "city": city,
        "sentiment": s,
        "score": score_map[s]
    }
