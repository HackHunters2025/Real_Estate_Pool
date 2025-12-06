import BASE_URL from "./base";

const mockVendor = {
  anomalies: [
    {
      vendor: "HVAC Corp",
      issue: "Invoice above historical average",
      severity: "MEDIUM",
    },
  ],
};

export async function analyzeVendorCosts() {
  try {
    const res = await fetch(`${BASE_URL}/vendor/analyze`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ costs: [] }),
    });

    if (!res.ok) throw new Error();
    const data = await res.json();

    return {
      anomalies: data.findings || [],
    };
  } catch {
    return mockVendor;
  }
}
