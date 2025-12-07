import BASE_URL from "./base";

export async function fetchMaintenanceStatus() {
  const res = await fetch(`${BASE_URL}/maintenance/predict`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      sensor_data: [26, 0.8, 30],
    }),
  });

  if (!res.ok) {
    throw new Error("Maintenance API failed");
  }

  const data = await res.json();

  return {
    status: data.maintenance_status.status, // ✅ NORMAL | WARNING | CRITICAL
    alerts: data.maintenance_status.alerts || [],
    executionMs: data.execution_ms,
  };
}
