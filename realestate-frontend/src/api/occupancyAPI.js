import BASE_URL from "./base";

const mockOccupancy = {
  rate: 92,
  trend: "UP",
  message: "Strong occupancy trend across the property",
};

export async function fetchOccupancy(propertyId = "property_A") {
  try {
    const res = await fetch(
      `${BASE_URL}/occupancy?property_id=${propertyId}&months_ahead=3`
    );

    if (!res.ok) throw new Error();
    const data = await res.json();

    return {
      rate: Math.round(data.current_occupancy || 92),
      trend: data.trend || "STABLE",
      message: "AI-based occupancy forecast",
    };
  } catch {
    return mockOccupancy;
  }
}
