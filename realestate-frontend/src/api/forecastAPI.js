export async function fetchCashFlowForecast(propertyId) {
  await new Promise((resolve) => setTimeout(resolve, 800));

  return [
    { month: "Jan", cash: 12000 },
    { month: "Feb", cash: 13500 },
    { month: "Mar", cash: 12800 },
    { month: "Apr", cash: 14200 },
    { month: "May", cash: 15000 },
    { month: "Jun", cash: 15800 },
  ];
}
