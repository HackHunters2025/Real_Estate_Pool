// import BASE_URL from "./base";

// // ✅ Mock fallback (your original data)
// const mockAlerts = [
//   {
//     level: "HIGH",
//     message: "Building A may exceed carbon limits by Q4.",
//   },
//   {
//     level: "MEDIUM",
//     message: "Elevated tenant churn risk for Unit 302.",
//   },
//   {
//     level: "LOW",
//     message: "Maintenance cost trending up for HVAC system.",
//   },
// ];

// export async function fetchAlerts(propertyId = "property_A") {
//   try {
//     const res = await fetch(`${BASE_URL}/alerts/dashboard`);

//     if (!res.ok) {
//       throw new Error("Backend not available");
//     }

//     const data = await res.json();

//     // ✅ If backend returns empty or invalid → fallback safely
//     if (!data || !data.alerts || data.alerts.length === 0) {
//       return mockAlerts;
//     }

//     return data.alerts;
//   } catch (err) {
//     console.warn("⚠ Backend unavailable, using mock alerts");
//     return mockAlerts;
//   }
// }

import BASE_URL from "./base";

export async function fetchAlerts(propertyId = "property_A") {
  const res = await fetch(`${BASE_URL}/alerts/dashboard`);

  if (!res.ok) {
    throw new Error("Alerts API failed");
  }

  const data = await res.json();

  // ✅ Normalize backend → frontend format
  return (data.alerts || []).map((alert) => ({
    level: alert.severity,   // ✅ FIXED
    message: alert.message,
    type: alert.type
  }));
}

