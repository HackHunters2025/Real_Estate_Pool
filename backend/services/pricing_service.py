# backend/services/pricing_service.py

from utils.file_loader import load_json
from services.news_service import analyze_market_sentiment
from services.esg_rules_service import check_esg_compliance

def recommend_price(current_rent: float, demand_score: float, city="Bengaluru", future_energy_usage=1150, property_name="Property_A"):
    """
    Agentic pricing:
    - Uses market benchmark from /data/market/rent_benchmarks.json
    - Adjusts pricing using sentiment agent
    - Applies season multiplier
    - ESG penalty pre-warns and adjusts down if needed
    """

    # Load market benchmark
    market_data = load_json("backend/data/market/rent_benchmarks.json") or {}
    market_avg = market_data.get("avg_market_rent_per_sqft", 50)
    festival_multiplier = market_data.get("festival_season_multiplier", 1.0)
    projection = market_data.get("next_12_month_projection_percent", 5.5)

    # External world influence — sentiment agent
    sentiment = analyze_market_sentiment(city)
    sentiment_score = sentiment.get("score", 0.5)

    # Base elasticity adjustment
    # Demand heavily affects rent if > 0.75 or < 0.35
    elasticity = (demand_score - 0.5) * 0.25  # small elasticity factor
    sentiment_boost = (sentiment_score - 0.5) * 0.15  # influence sentiment

    # Initial new price computation
    new_price = current_rent * (1 + elasticity + sentiment_boost)

    # Apply seasonal multiplier
    new_price *= festival_multiplier

    # Apply future projection scaling
    new_price *= (1 + projection / 100 / 12)  # future-proofing

    # ESG simulated compliance check
    esg_check = check_esg_compliance(future_energy_usage, property_name)

    if esg_check["status"] == "FAIL":
        new_price *= 0.97  # ESG penalty reduces pricing power

    return round(new_price, 2)
