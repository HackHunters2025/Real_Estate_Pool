import BASE_URL from "./base";

const mockScenario = {
  impactScore: 52,
  projection: [
    { month: 1, noiChange: 1200 },
    { month: 2, noiChange: 2400 },
  ],
};

export async function runScenarioSimulation(inputs) {
  try {
    const res = await fetch(`${BASE_URL}/scenario`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: inputs,
    });

    if (!res.ok) throw new Error();
    const data = await res.json();

    return {
      impactScore: Math.round(data.scenario_result.impact_score * 10),
      projection: data.scenario_result.projection.map((p) => ({
        month: p.month,
        noiChange: p.mock_noi_change,
      })),
    };
  } catch {
    return mockScenario;
  }
}
