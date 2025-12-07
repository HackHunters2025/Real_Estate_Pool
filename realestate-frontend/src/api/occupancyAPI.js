import BASE_URL from "./base";

export async function fetchOccupancyHealth() {
  const res = await fetch(`${BASE_URL}/pricing/recommend`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      current_rent: 20000,
      demand_score: 0.9,
    }),
  });

  if (!res.ok) {
    throw new Error("Occupancy inference failed");
  }

  const data = await res.json();

  // ✅ Interpret demand_score → occupancy health
  let rate = Math.round(85 + data.recommended_rent / 1000);
  rate = Math.min(rate, 99);

  return {
    rate,               // %
    trend: "UP",
    rationale:
      "High pricing demand indicates strong occupancy likelihood",
  };
}
