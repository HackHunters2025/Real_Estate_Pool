# backend/services/forecasting_service.py

def simple_forecast(history: list[float], new_rent: float):
    """
    Super simple forecast:
    - Take last value as base
    - Apply small growth based on delta between new_rent and last_rent
    Returns list of 6 'monthly' forecasts.
    """
    if not history:
        history = [new_rent]

    last = history[-1]
    growth_factor = (new_rent - last) / max(last, 1)  # avoid div-by-zero
    growth_factor = max(min(growth_factor, 0.15), -0.15)  # clamp

    forecast = []
    current = last
    for _ in range(6):
        current = current * (1 + growth_factor / 2)
        forecast.append(round(current, 2))

    return {
        "base_rent": last,
        "new_rent": new_rent,
        "monthly_forecast": forecast
    }
