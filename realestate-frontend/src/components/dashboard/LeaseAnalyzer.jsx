import { useState } from "react";
import { FileText, Upload, Loader2 } from "lucide-react";
import { uploadAndExtractLease } from "../../api/leaseAPI";

export default function LeaseAnalyzer() {
  const [file, setFile] = useState(null);
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) return;

    setLoading(true);
    try {
      const res = await uploadAndExtractLease(file);
      console.log("✅ LEASE DATA RECEIVED IN UI:", res);
      setData(res);
    } catch (err) {
      console.error("❌ Lease extraction error", err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-white rounded-2xl border border-slate-100 shadow-sm p-6">
      <div className="flex items-center gap-2 mb-4">
        <FileText size={18} className="text-indigo-600" />
        <h2 className="text-sm font-bold text-slate-900">
          Lease Analyzer
        </h2>
      </div>

      {/* Upload */}
      <div className="border-2 border-dashed rounded-xl p-6 text-center mb-4">
        <input
          type="file"
          accept=".txt,.pdf"
          onChange={(e) => setFile(e.target.files[0])}
          className="hidden"
          id="lease-upload"
        />
        <label
          htmlFor="lease-upload"
          className="cursor-pointer flex flex-col items-center gap-2 text-slate-500"
        >
          <Upload size={20} />
          <span className="text-sm">
            Upload Lease Agreement
          </span>
        </label>
      </div>

      <button
        onClick={handleUpload}
        disabled={loading || !file}
        className="w-full bg-indigo-600 text-white rounded-lg py-2 text-sm font-semibold hover:bg-indigo-700 transition"
      >
        {loading ? (
          <span className="flex items-center justify-center gap-2">
            <Loader2 className="animate-spin" size={16} />
            Analyzing Lease…
          </span>
        ) : (
          "Extract Lease Details"
        )}
      </button>

      {/* Results */}
      {data && (
        <div className="mt-6 grid grid-cols-2 gap-4 text-sm">
          <div><b>Monthly Rent:</b> ₹{data.monthlyRent}</div>
          <div><b>Lease Period:</b> {data.leaseStart} → {data.leaseEnd}</div>
          <div><b>Rent Escalation:</b> {data.rentEscalation}</div>
          <div><b>Penalty Fee:</b> ₹{data.penaltyFee}</div>
        </div>
      )}
    </div>
  );
}
