import { useEffect, useState } from "react";
import { Users, Loader2, ArrowUpRight } from "lucide-react";
import { fetchChurnRisk } from "../../api/churnAPI";

export default function ChurnRiskCard({ propertyId = "A" }) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  // useEffect(() => {
  //   setLoading(true);
  //   fetchChurnRisk(propertyId).then((res) => {
  //     setData(res);
  //     setLoading(false);
  //   });
  // }, [propertyId]);

  useEffect(() => {
  setLoading(true);

  fetchChurnRisk(propertyId)
    .then((res) => {
      console.log("✅ CHURN DATA RECEIVED:", res);
      setData(res);
    })
    .catch((err) => {
      console.error("❌ Churn UI error:", err);
    })
    .finally(() => setLoading(false));
}, [propertyId]);


  if (loading) {
    return (
      <div className="bg-white rounded-2xl border border-slate-100 shadow-sm p-6 h-full flex flex-col items-center justify-center text-slate-400 gap-2">
        <Loader2 className="animate-spin" size={20} />
        <span className="text-xs">Analyzing churn...</span>
      </div>
    );
  }

  const colorMap = {
    HIGH: "bg-rose-50 text-rose-700 border-rose-100",
    MEDIUM: "bg-amber-50 text-amber-700 border-amber-100",
    LOW: "bg-emerald-50 text-emerald-700 border-emerald-100",
  };

  const ringColorMap = {
    HIGH: "text-rose-500",
    MEDIUM: "text-amber-500",
    LOW: "text-emerald-500",
  };

  return (
    <div className="bg-white rounded-2xl border border-slate-100 shadow-sm p-6 h-full flex flex-col">
      <div className="flex justify-between items-start mb-4">
        <div>
          <h2 className="text-sm font-bold text-slate-900">Tenant Churn Risk</h2>
          <p className="text-xs text-slate-500 mt-0.5">Behavioral Analysis</p>
        </div>
        <div className="bg-indigo-50 p-2 rounded-lg">
          <Users size={18} className="text-indigo-600" />
        </div>
      </div>

      <div className="flex-1 flex flex-col justify-center">
        <div className="flex items-end gap-1 mb-4">
          <span className={`text-4xl font-black tracking-tight ${ringColorMap[data.level]}`}>
            {data.score}
          </span>
          <span className="text-sm text-slate-400 font-medium mb-1.5">/ 100 Score</span>
        </div>

        <div className="flex items-start justify-between mb-4">
           <span
            className={`px-3 py-1 rounded-full text-xs font-bold border ${colorMap[data.level]}`}
          >
            {data.level} RISK
          </span>
        </div>

        <p className="text-xs text-slate-500 leading-relaxed bg-slate-50 p-3 rounded-lg border border-slate-100">
          {data.message}
        </p>
      </div>
    </div>
  );
}
