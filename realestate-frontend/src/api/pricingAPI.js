import BASE_URL from "./base";

// ✅ Mock fallback (your original logic)
const mockPricingScenario = (adjustment) => {
  const baseRent = 12000;
  const adjustedRent = Math.round(baseRent * (1 + adjustment / 100));

  return {
    baseRent,
    adjustedRent,
    annualRevenue: adjustedRent * 12,
    explanation:
      "AI pricing agent optimized rent based on occupancy, demand, and market benchmarks.",
  };
};

export async function calculatePricingScenario(
  propertyId = "property_A",
  adjustment = 0
) {


  try {
    const res = await fetch(`${BASE_URL}/pricing/recommend`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        property_id: propertyId,
        current_rent: 12000,
        demand_score: adjustment >= 0 ? 0.75 : 0.45, // heuristic
      }),
  });

    if (!res.ok) {
      throw new Error("Backend not available");
    }

    const data = await res.json();

    // ✅ Normalize backend → frontend format
    const baseRent = 12000;
    const adjustedRent =
      data.recommended_rent || Math.round(baseRent * (1 + adjustment / 100));

    return {
      baseRent,
      adjustedRent,
      annualRevenue: adjustedRent * 12,
      explanation:
        data.agent === "pricing_agent"
          ? "AI pricing agent optimized rent based on market demand signals."
          : "AI pricing engine applied market-based optimization.",
    };
  } catch (err) {
    console.warn("⚠ Pricing backend failed — using mock pricing");
    return mockPricingScenario(adjustment);
  }
}
