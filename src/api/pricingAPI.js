export async function calculatePricingScenario(propertyId, adjustment) {
  await new Promise((resolve) => setTimeout(resolve, 600));

  const baseRent = 12000;
  const adjustedRent = Math.round(baseRent * (1 + adjustment / 100));

  return {
    baseRent,
    adjustedRent,
    annualRevenue: adjustedRent * 12,
    explanation:
      "AI pricing agent optimized rent based on occupancy, demand, and market benchmarks.",
  };
}
