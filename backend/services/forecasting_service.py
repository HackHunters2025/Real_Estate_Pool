import numpy as np
from services.file_loader import load_json_or_csv

def simple_forecast(history, new_rent, months_ahead=6, inflation_rate=0.04):
    """
    Improved adaptive rent forecasting model
    Includes:
       - History trend
       - Inflation weight
       - Seasonal pattern simulation
    """
    if not history:
        history = [new_rent]  # start baseline

    last_rent = history[-1]

    # Compute base growth direction from change
    rent_delta = new_rent - last_rent
    growth_factor = rent_delta / max(last_rent, 1)
    growth_factor = max(min(growth_factor, 0.15), -0.15)

    # Inflation dampening effect
    inflation_adjustment = inflation_rate / 3

    # Seasonal curve simulation
    seasonal_pattern = np.array([1.00, 1.03, 1.02, 0.98, 0.97, 1.05])
    seasonal_pattern = seasonal_pattern[:months_ahead]

    current_value = last_rent
    predictions = []

    for i in range(months_ahead):
        trend_step = current_value * (growth_factor + inflation_adjustment)
        next_value = current_value + trend_step
        next_value *= seasonal_pattern[i]

        current_value = next_value
        predictions.append(round(next_value, 2))

    # Confidence Scoring
    confidence_score = round(0.55 + abs(growth_factor), 2)
    confidence_score = max(min(confidence_score, 0.95), 0.50)

    return {
        "predicted_rent_series": predictions,
        "confidence_score": confidence_score,
        "inflation_rate": inflation_rate,
        "seasonal_pattern_used": seasonal_pattern.tolist(),
    }


def run_forecasting(property_id="property_A", current_rent=None, months_ahead=6, inflation_rate=0.04):
    """
    Main wrapper called by forecasting_agent
    Loads historical rent if exists
    """

    history_path = f"backend/data/properties/{property_id}/rent_history.csv"

    try:
        history_data = load_json_or_csv(history_path)
        history = [float(row.get("rent", 0)) for row in history_data]
    except Exception:
        history = []

    if current_rent is None:
        current_rent = history[-1] if history else 20000  # fallback

    forecast_output = simple_forecast(
        history=history,
        new_rent=current_rent,
        months_ahead=months_ahead,
        inflation_rate=inflation_rate
    )

    return {
        "property_id": property_id,
        "input_rent": current_rent,
        "forecast_months": months_ahead,
        "predicted_rent": forecast_output["predicted_rent_series"],
        "confidence_score": forecast_output["confidence_score"],
        "inflation_rate": forecast_output["inflation_rate"],
        "seasonal_pattern_used": forecast_output["seasonal_pattern_used"]
    }
