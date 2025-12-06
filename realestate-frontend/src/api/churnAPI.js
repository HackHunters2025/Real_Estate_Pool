import BASE_URL from "./base";

// ✅ Mock fallback (your existing logic)
const mockChurnRisk = {
  score: 68,              // 0–100
  level: "MEDIUM",        // LOW | MEDIUM | HIGH
  message:
    "Tenant engagement and payment patterns indicate moderate churn risk.",
};

export async function fetchChurnRisk(propertyId = "property_A") {
  try {
    const res = await fetch(
      `${BASE_URL}/churn?property_id=${propertyId}`
    );

    if (!res.ok) {
      throw new Error("Backend not available");
    }

    const data = await res.json();

    // ✅ Validate backend response structure
    if (data.status !== "success") {
      throw new Error("Invalid backend response");
    }

    // ✅ Normalize backend → frontend format
    return {
      score: Math.round((data.churn_score || 0) * 100),
      level: data.risk_level || "LOW",
      message: `Top churn drivers: ${(data.top_factors || []).join(", ")}`,
    };
  } catch (err) {
    console.warn("⚠ Backend churn API failed — using mock data");
    return mockChurnRisk;
  }
}
