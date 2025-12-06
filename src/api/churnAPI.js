export async function fetchChurnRisk(propertyId) {
  await new Promise((resolve) => setTimeout(resolve, 700));

  return {
    score: 68,              // 0–100
    level: "MEDIUM",        // LOW | MEDIUM | HIGH
    message:
      "Tenant engagement and payment patterns indicate moderate churn risk.",
  };
}
