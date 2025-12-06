import { useEffect, useState } from "react";
import { Leaf, Loader2, CheckCircle2, AlertTriangle } from "lucide-react";
import { fetchESGStatus } from "../../api/esgAPI";

export default function ESGStatusCard({ propertyId = "A" }) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  // useEffect(() => {
  //   setLoading(true);
  //   fetchESGStatus(propertyId).then((res) => {
  //     setData(res);
  //     setLoading(false);
  //   });
  // }, [propertyId]);

  useEffect(() => {
  setLoading(true);

  fetchESGStatus(propertyId)
    .then((res) => {
      console.log("✅ ESG DATA RECEIVED:", res);
      setData(res);
    })
    .catch((err) => {
      console.error("❌ ESG UI error:", err);
    })
    .finally(() => setLoading(false));
}, [propertyId]);


  if (loading) {
    return (
      <div className="bg-white rounded-2xl border border-slate-100 shadow-sm p-6 h-full flex flex-col items-center justify-center text-slate-400 gap-2">
        <Loader2 className="animate-spin" size={20} />
        <span className="text-xs">Checking compliance...</span>
      </div>
    );
  }

  const isPass = data.status === "PASS";

  return (
    <div className="bg-white rounded-2xl border border-slate-100 shadow-sm p-6 h-full flex flex-col">
      <div className="flex justify-between items-start mb-4">
        <div>
          <h2 className="text-sm font-bold text-slate-900">ESG Compliance</h2>
          <p className="text-xs text-slate-500 mt-0.5">Sustainability Monitor</p>
        </div>
        <div className={`p-2 rounded-lg ${isPass ? 'bg-emerald-50' : 'bg-rose-50'}`}>
          <Leaf size={18} className={isPass ? 'text-emerald-600' : 'text-rose-600'} />
        </div>
      </div>

      <div className="flex-1 flex flex-col justify-center">
        <div className="flex items-center gap-3 mb-4">
          <span
            className={`flex items-center gap-1.5 pl-2 pr-3 py-1 rounded-full text-xs font-bold border ${
              isPass 
                ? "bg-emerald-50 border-emerald-100 text-emerald-700" 
                : "bg-rose-50 border-rose-100 text-rose-700"
            }`}
          >
            {isPass ? <CheckCircle2 size={12} /> : <AlertTriangle size={12} />}
            {data.status}
          </span>
          <span className="text-sm font-medium text-slate-600">
             {data.energyUsage}% <span className="text-slate-400 font-normal">of cap</span>
          </span>
        </div>

        {/* Progress Bar Visual */}
        <div className="w-full bg-slate-100 h-2 rounded-full mb-3 overflow-hidden">
          <div 
            className={`h-full rounded-full transition-all duration-1000 ${
              data.energyUsage > 100 ? 'bg-rose-500' : 'bg-emerald-500'
            }`}
            style={{ width: `${Math.min(data.energyUsage, 100)}%` }}
          />
        </div>

        <p className="text-xs text-slate-500 leading-relaxed bg-slate-50 p-3 rounded-lg border border-slate-100">
          {data.message}
        </p>
      </div>
    </div>
  );
}
