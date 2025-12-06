export async function fetchAlerts(propertyId) {
  await new Promise((resolve) => setTimeout(resolve, 600));

  return [
    {
      level: "HIGH",
      message: "Building A may exceed carbon limits by Q4.",
    },
    {
      level: "MEDIUM",
      message: "Elevated tenant churn risk for Unit 302.",
    },
    {
      level: "LOW",
      message: "Maintenance cost trending up for HVAC system.",
    },
  ];
}
