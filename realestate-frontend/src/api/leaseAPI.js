import BASE_URL from "./base";

export async function uploadAndExtractLease(file) {
  const formData = new FormData();
  formData.append("file", file);

  const res = await fetch(`${BASE_URL}/lease/extract`, {
    method: "POST",
    body: formData, // ✅ multipart/form-data automatically
  });

  if (!res.ok) {
    throw new Error("Lease extraction failed");
  }

  const data = await res.json();

  console.log("✅ RAW LEASE BACKEND RESPONSE:", data);

  const fields = data.extracted_fields || {};

  return {
    monthlyRent: Number(fields.monthly_rent || 0),
    leaseStart: fields.lease_start || "-",
    leaseEnd: fields.lease_end || "-",
    rentEscalation: fields.rent_escalation || "-",
    penaltyFee: Number(fields.penalty_fee || 0),
    executionTime: data.execution_ms,
    filename: data.filename,
  };
}
