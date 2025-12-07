import { useEffect, useState } from "react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid,
  Area,
  AreaChart
} from "recharts";
import { TrendingUp, Loader2, AlertCircle } from "lucide-react";

import { fetchCashFlowForecast } from "../../api/forecastAPI.js";

export default function ForecastChart({ propertyId = "A" }) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // useEffect(() => {
  //   setLoading(true);
  //   setError(null);

  //   fetchCashFlowForecast(propertyId)
  //     .then((res) => setData(res))
  //     .catch(() => setError("Failed to load forecast"))
  //     .finally(() => setLoading(false));
  // }, [propertyId]);

useEffect(() => {
  setLoading(true);
  setError(null);

  fetchCashFlowForecast(propertyId)
    .then((res) => {
      console.log("✅ Forecast data received in UI:", res);
      setData(res);
    })
    .catch((err) => {
      console.error("❌ Forecast UI error:", err);
      setError("Failed to load forecast");
    })
    .finally(() => setLoading(false));
}, [propertyId]);


  if (loading) {
    return (
      <div className="bg-white rounded-2xl border border-slate-100 shadow-sm p-6 h-[400px] flex flex-col items-center justify-center text-slate-400 gap-3">
        <Loader2 className="animate-spin text-indigo-500" size={24} />
        <span className="text-sm font-medium">Forecasting agent analyzing signals...</span>
      </div>
    );
  }

  if (error) {
    return (
      <div className="bg-white rounded-2xl border border-red-100 shadow-sm p-6 h-[400px] flex flex-col items-center justify-center text-red-500 gap-3">
        <AlertCircle size={24} />
        <span className="text-sm font-medium">{error}</span>
      </div>
    );
  }

  // Custom Tooltip for better UI
  const CustomTooltip = ({ active, payload, label }) => {
    if (active && payload && payload.length) {
      return (
        <div className="bg-slate-900 text-white text-xs rounded-lg py-2 px-3 shadow-xl">
          <p className="font-semibold mb-1">{label}</p>
          <p className="text-indigo-300">
            Cash Flow: <span className="text-white font-bold">₹{payload[0].value.toLocaleString()}</span>
          </p>
        </div>
      );
    }
    return null;
  };

  return (
    <div className="bg-white rounded-2xl border border-slate-100 shadow-sm p-6 h-[400px] flex flex-col">
      <div className="flex justify-between items-start mb-6">
        <div>
          <h2 className="text-base font-bold text-slate-900 flex items-center gap-2">
            Cash Flow Forecast
          </h2>
          <p className="text-xs text-slate-500 mt-1">
            AI Projection • Next 6 Months
          </p>
        </div>
        <div className="bg-indigo-50 p-2 rounded-lg">
          <TrendingUp size={18} className="text-indigo-600" />
        </div>
      </div>

      <div className="flex-1 w-full min-h-0">
        <ResponsiveContainer width="100%" height="100%">
          <AreaChart data={data} margin={{ top: 10, right: 10, left: 0, bottom: 0 }}>
            <defs>
              <linearGradient id="colorCash" x1="0" y1="0" x2="0" y2="1">
                <stop offset="5%" stopColor="#6366f1" stopOpacity={0.1}/>
                <stop offset="95%" stopColor="#6366f1" stopOpacity={0}/>
              </linearGradient>
            </defs>
            <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#f1f5f9" />
            <XAxis 
              dataKey="month" 
              axisLine={false} 
              tickLine={false} 
              tick={{ fontSize: 11, fill: '#64748b' }} 
              dy={10}
            />
            <YAxis 
              axisLine={false} 
              tickLine={false} 
              tick={{ fontSize: 11, fill: '#64748b' }} 
              tickFormatter={(value) => `₹${value/1000}k`}
            />
            <Tooltip content={<CustomTooltip />} cursor={{ stroke: '#6366f1', strokeWidth: 1, strokeDasharray: '4 4' }} />
            <Area 
              type="monotone" 
              dataKey="cash" 
              stroke="#6366f1" 
              strokeWidth={3} 
              fillOpacity={1} 
              fill="url(#colorCash)" 
            />
          </AreaChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}
