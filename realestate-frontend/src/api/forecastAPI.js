import BASE_URL from "./base";

export async function fetchCashFlowForecast(propertyId = "property_A") {
  const res = await fetch(`${BASE_URL}/forecast`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      historical_values: [18000, 19000, 20000, 21000],
      duration_months: 6,
    }),
  });

  if (!res.ok) {
    throw new Error("Forecast API failed");
  }

  const data = await res.json();

  if (data.status !== "success") {
    throw new Error("Invalid forecast response");
  }

  const forecast = data.forecast_result?.predicted_rent;

  if (!Array.isArray(forecast)) {
    throw new Error("No forecast array returned");
  }

  return forecast.map((value, index) => ({
    month: `M${index + 1}`,
    cash: Math.round(value),
  }));
}
