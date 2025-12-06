import BASE_URL from "./base";

const mockPortfolio = {
  recommendedAllocation: [
    { id: "property_A", weight: 0.45 },
    { id: "property_B", weight: 0.35 },
    { id: "property_C", weight: 0.20 },
  ],
};

export async function optimizePortfolio(riskLevel = "medium") {
  try {
    const res = await fetch(`${BASE_URL}/portfolio`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ risk_level: riskLevel }),
    });

    if (!res.ok) throw new Error();
    const data = await res.json();

    return {
      recommendedAllocation: data.optimization.allocation,
    };
  } catch {
    return mockPortfolio;
  }
}
