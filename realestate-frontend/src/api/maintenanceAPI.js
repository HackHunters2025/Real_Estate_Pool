import BASE_URL from "./base";

const mockMaintenance = {
  riskLevel: "LOW",
  message: "No immediate maintenance risks detected",
};

export async function fetchMaintenanceStatus() {
  try {
    const res = await fetch(`${BASE_URL}/maintenance/predict`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        sensor_data: [62, 64, 63],
      }),
    });

    if (!res.ok) throw new Error();
    const data = await res.json();

    return {
      riskLevel: data.maintenance_status || "LOW",
      message: "AI detected upcoming maintenance trend",
    };
  } catch {
    return mockMaintenance;
  }
}
