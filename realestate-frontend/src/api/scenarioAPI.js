import BASE_URL from "./base";

export async function runScenarioSimulation(payload) {
  const res = await fetch(`${BASE_URL}/scenario`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });

  if (!res.ok) {
    throw new Error("Scenario API failed");
  }

  const data = await res.json();
  console.log("✅ RAW SCENARIO BACKEND RESPONSE:", data);

  return data.scenario_result;
}
