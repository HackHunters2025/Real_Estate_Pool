import BASE_URL from "./base";

export async function optimizePortfolio({
  riskLevel = "low",
  properties,
}) {
  const res = await fetch(`${BASE_URL}/portfolio`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      risk_level: riskLevel,
      properties,
    }),
  });

  if (!res.ok) {
    throw new Error("Portfolio optimization failed");
  }

  const data = await res.json();

  const allocation = data.optimization_decision?.allocation_plan;

  if (!allocation) {
    throw new Error("Invalid portfolio response");
  }

  return {
    strategyRisk: data.optimization_decision.strategy_risk_level,
    topRecommendation: data.optimization_decision.top_recommendation,
    explanation: data.optimization_decision.explanation,
    allocation: allocation.map((a) => ({
      id: a.id,
      weight: Math.round(a.suggested_weight * 100),
      expectedReturn: Math.round(a.expected_return * 100),
      riskScore: a.risk_score,
    })),
  };
}
