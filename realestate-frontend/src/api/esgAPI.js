export async function fetchESGStatus(propertyId) {
  await new Promise((resolve) => setTimeout(resolve, 600));

  return {
    status: "PASS", // PASS | FAIL
    energyUsage: 82,
    message: "Energy usage within permitted ESG limits",
  };
}
