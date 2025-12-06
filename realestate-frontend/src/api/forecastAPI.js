import BASE_URL from "./base";

// ✅ Mock fallback (your original data)
const mockCashFlowForecast = [
  { month: "Jan", cash: 12000 },
  { month: "Feb", cash: 13500 },
  { month: "Mar", cash: 12800 },
  { month: "Apr", cash: 14200 },
  { month: "May", cash: 15000 },
  { month: "Jun", cash: 15800 },
];

export async function fetchCashFlowForecast(propertyId = "property_A") {
  try {
    const res = await fetch(
      `${BASE_URL}/forecast?property_id=${propertyId}&months_ahead=6`
    );

    if (!res.ok) {
      throw new Error("Backend not available");
    }

    const data = await res.json();

    if (data.status !== "success") {
      throw new Error("Invalid backend response");
    }

    /**
     * Backend forecast contains predicted NOI / revenue.
     * We map it to frontend-friendly cash flow format.
     */
    const forecast = data.forecast?.predicted_noi || [];

    if (!forecast.length) {
      throw new Error("Empty forecast");
    }

    return forecast.slice(-6).map((value, index) => ({
      month: `M${index + 1}`,
      cash: Math.round(value),
    }));
  } catch (err) {
    console.warn("⚠ Forecast backend unavailable — using mock data");
    return mockCashFlowForecast;
  }
}
