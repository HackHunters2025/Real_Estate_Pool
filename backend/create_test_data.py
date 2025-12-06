# backend/create_test_data.py

import os
import pandas as pd
import numpy as np

# Base directory
base_dir = "backend/data/properties/property_A"
os.makedirs(base_dir, exist_ok=True)

# ----------------------------
# 1. Generate rent_expenses.csv
# ----------------------------
months = [f"2023-{str(i).zfill(2)}" for i in range(1, 13)] + [f"2024-{str(i).zfill(2)}" for i in range(1, 13)]
revenue = np.random.randint(150000, 200000, size=len(months))
expenses = np.random.randint(50000, 80000, size=len(months))
df_re = pd.DataFrame({"month": months, "revenue": revenue, "expenses": expenses})
df_re.to_csv(os.path.join(base_dir, "rent_expenses.csv"), index=False)

# ----------------------------
# 2. Generate occupancy.csv
# ----------------------------
occupancy_rate = np.round(np.random.uniform(0.65, 0.95, size=len(months)), 2)
df_occ = pd.DataFrame({"month": months, "occupancy_rate": occupancy_rate})
df_occ.to_csv(os.path.join(base_dir, "occupancy.csv"), index=False)

# ----------------------------
# 3. Generate tenant_data.csv
# ----------------------------
tenant_data = pd.DataFrame({
    "tenant_id": range(1, 101),
    "late_payments": np.random.poisson(1.2, size=100),
    "complaints": np.random.poisson(0.8, size=100),
    "months_stayed": np.random.randint(2, 36, size=100),
    "rent_increase": np.random.randint(0, 12, size=100)
})
tenant_data.to_csv(os.path.join(base_dir, "tenant_data.csv"), index=False)

print("✅ Test CSV files created in:", base_dir)
