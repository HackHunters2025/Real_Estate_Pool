# backend/services/iot_sim_service.py

import random

def generate_hvac_sample():
    """
    Returns one synthetic sensor triplet:
    [temperature, vibration, pressure]
    """
    return [
        round(random.uniform(72, 90), 1),
        round(random.uniform(40, 75), 1),
        round(random.uniform(100, 135), 1),
    ]

def generate_hvac_series(n: int = 10):
    return [generate_hvac_sample() for _ in range(n)]
