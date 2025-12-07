import { useEffect, useState } from "react";
import { Users, TrendingUp, Loader2 } from "lucide-react";
import { fetchOccupancyHealth } from "../../api/occupancyAPI";

export default function OccupancyCard() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setLoading(true);

    fetchOccupancyHealth()
      .then((res) => {
        console.log("✅ OCCUPANCY DATA:", res);
        setData(res);
      })
      .finally(() => setLoading(false));
  }, []);

  if (loading) {
    return (
      <div className="bg-white rounded-2xl border p-6 flex flex-col items-center justify-center text-slate-400">
        <Loader2 className="animate-spin" />
        <span className="text-xs mt-1">Analyzing demand…</span>
      </div>
    );
  }

  return (
    <div className="bg-white rounded-2xl border shadow-sm p-6">
      <div className="flex items-center gap-3 mb-4">
        <div className="bg-indigo-50 p-2 rounded-lg">
          <Users size={18} className="text-indigo-600" />
        </div>
        <div>
          <h2 className="text-sm font-bold text-slate-900">
            Occupancy Health
          </h2>
          <p className="text-xs text-slate-500">
            AI Demand-Derived Signal
          </p>
        </div>
      </div>

      <div className="flex items-center gap-3 mb-3">
        <TrendingUp className="text-emerald-600" size={18} />
        <span className="text-2xl font-bold text-slate-900">
          {data.rate}%
        </span>
      </div>

      <p className="text-xs text-slate-500">
        {data.rationale}
      </p>
    </div>
  );
}
