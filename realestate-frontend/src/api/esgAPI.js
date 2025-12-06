import BASE_URL from "./base";

// ✅ Mock fallback (your original data)
const mockESGStatus = {
  status: "PASS", // PASS | FAIL
  energyUsage: 82,
  message: "Energy usage within permitted ESG limits",
};

export async function fetchESGStatus(propertyId = "property_A") {
  try {
    const res = await fetch(`${BASE_URL}/esg/check`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        property: propertyId,
        energy_usage: 820, // mock or derived value
      }),
    });

    if (!res.ok) {
      throw new Error("Backend not available");
    }

    const data = await res.json();

    // ✅ Normalize backend response → frontend format
    return {
      status: data.status || "PASS",
      energyUsage: Math.round((data.energy_usage || 820) / 10),
      message:
        data.details ||
        (data.status === "PASS"
          ? "Energy usage within permitted ESG limits"
          : "Energy usage exceeds ESG thresholds"),
    };
  } catch (err) {
    console.warn("⚠ ESG backend unavailable — using mock data");
    return mockESGStatus;
  }
}
