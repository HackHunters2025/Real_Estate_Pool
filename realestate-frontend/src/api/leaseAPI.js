import BASE_URL from "./base";

const mockLease = {
  tenant: "Acme Corp",
  rent: 12000,
  startDate: "2023-01-01",
  endDate: "2026-12-31",
  alerts: ["Renewal due in 9 months"],
};

export async function fetchLeaseDetails() {
  try {
    const res = await fetch(`${BASE_URL}/lease/extract`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: "mock lease text" }),
    });

    if (!res.ok) throw new Error();

    const data = await res.json();
    return {
      tenant: data.tenant_name || "Unknown",
      rent: data.rent || 12000,
      startDate: data.start_date,
      endDate: data.end_date,
      alerts: data.flags || [],
    };
  } catch {
    return mockLease;
  }
}
