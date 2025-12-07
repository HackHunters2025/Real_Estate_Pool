import { useState } from "react";
import {
  AreaChart,
  Area,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
} from "recharts";
import { Sliders, Loader2, Play } from "lucide-react";
import { runScenarioSimulation } from "../../api/scenarioAPI";

export default function ScenarioSimulator({ propertyId = "property_A" }) {
  const [inputs, setInputs] = useState({
    rent: 0,
    occupancy: 0,
    expense: 0,
  });

  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);

  const runScenario = async () => {
    setLoading(true);
    try {
      const res = await runScenarioSimulation({
        property_id: propertyId,
        rent_change_pct: inputs.rent,
        occupancy_change_pct: inputs.occupancy,
        expense_change_pct: inputs.expense,
        months_ahead: 6,
      });

      console.log("✅ SCENARIO DATA SHOWN IN UI:", res);
      setData(res);
    } catch (err) {
      console.error("❌ Scenario UI error:", err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-white rounded-2xl border border-slate-100 shadow-sm p-6">
      <div className="flex items-center gap-2 mb-4">
        <Sliders size={18} className="text-indigo-600" />
        <h2 className="text-sm font-bold text-slate-900">
          Scenario Simulation
        </h2>
      </div>

      {/* Controls */}
      <div className="grid grid-cols-3 gap-4 mb-6 text-xs">
        {[
          { label: "Rent %", key: "rent" },
          { label: "Occupancy %", key: "occupancy" },
          { label: "Expenses %", key: "expense" },
        ].map((s) => (
          <div key={s.key}>
            <label className="text-slate-500">{s.label}</label>
            <input
              type="range"
              min={-10}
              max={10}
              value={inputs[s.key]}
              onChange={(e) =>
                setInputs({ ...inputs, [s.key]: Number(e.target.value) })
              }
              className="w-full"
            />
            <div className="text-center font-semibold">
              {inputs[s.key]}%
            </div>
          </div>
        ))}
      </div>

      <button
        onClick={runScenario}
        className="flex items-center gap-2 bg-indigo-600 hover:bg-indigo-700 text-white px-4 py-2 rounded-lg text-sm font-semibold"
      >
        {loading ? <Loader2 className="animate-spin" size={16} /> : <Play size={16} />}
        Run Scenario
      </button>

      {data && (
        <>
          <div className="grid grid-cols-3 gap-4 text-sm mt-6">
            <div>Impact: <b>{data.impact_classification}</b></div>
            <div>Confidence: {(data.confidence_score * 100).toFixed(0)}%</div>
            <div>Final NOI: ₹{Math.round(data.final_month_NOI).toLocaleString()}</div>
          </div>

          <ResponsiveContainer width="100%" height={220}>
            <AreaChart data={data.projection_monthly}>
              <XAxis dataKey="month" />
              <YAxis />
              <Tooltip />
              <Area
                type="monotone"
                dataKey="projected_NOI"
                stroke="#6366f1"
                fill="#e0e7ff"
                strokeWidth={2}
              />
            </AreaChart>
          </ResponsiveContainer>
        </>
      )}
    </div>
  );
}
