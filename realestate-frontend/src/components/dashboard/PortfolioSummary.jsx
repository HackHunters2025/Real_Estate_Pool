import { useEffect, useState } from "react";
import { PieChart, Pie, Cell, Tooltip, ResponsiveContainer } from "recharts";
import { Briefcase, Loader2 } from "lucide-react";
import { optimizePortfolio } from "../../api/portfolioAPI";

const COLORS = ["#6366f1", "#22c55e", "#f59e0b", "#ef4444"];

export default function PortfolioOptimization() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setLoading(true);

    optimizePortfolio({
      riskLevel: "low",
      properties: [
        { id: "property_A", current_value: 1000000, noi: 60000, risk_score: 0.3 },
        { id: "property_B", current_value: 800000, noi: 45000, risk_score: 0.5 },
      ],
    })
      .then((res) => {
        console.log("✅ PORTFOLIO DATA:", res);
        setData(res);
      })
      .catch(console.error)
      .finally(() => setLoading(false));
  }, []);

  if (loading || !data) {
    return (
      <div className="bg-white rounded-2xl border p-6 flex items-center justify-center text-slate-400">
        <Loader2 className="animate-spin" size={18} />
        <span className="ml-2 text-sm">Optimizing portfolio…</span>
      </div>
    );
  }

  return (
    <div className="bg-white rounded-2xl border border-slate-100 shadow-sm p-6">
      <div className="flex items-center gap-2 mb-4">
        <Briefcase size={18} className="text-indigo-600" />
        <h2 className="text-sm font-bold text-slate-900">
          Portfolio Optimization
        </h2>
      </div>

      <p className="text-xs text-slate-500 mb-4">
        Strategy risk level: <b>{data.strategyRisk}</b> · Top pick:{" "}
        <b>{data.topRecommendation}</b>
      </p>

      <ResponsiveContainer width="100%" height={220}>
        <PieChart>
          <Pie
            data={data.allocation}
            dataKey="weight"
            nameKey="id"
            innerRadius={55}
            outerRadius={85}
          >
            {data.allocation.map((_, i) => (
              <Cell key={i} fill={COLORS[i % COLORS.length]} />
            ))}
          </Pie>
          <Tooltip formatter={(v) => `${v}%`} />
        </PieChart>
      </ResponsiveContainer>

      <p className="text-xs text-slate-500 mt-4 bg-slate-50 p-3 rounded-lg">
        {data.explanation}
      </p>
    </div>
  );
}
