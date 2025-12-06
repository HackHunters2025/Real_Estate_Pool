// import { useEffect, useState } from "react";
// import { fetchAlerts } from "../../api/alertAPI";

// export default function AlertsPanel({ propertyId = "A" }) {
//   const [alerts, setAlerts] = useState(null);
//   const [loading, setLoading] = useState(true);

//   useEffect(() => {
//     setLoading(true);
//     fetchAlerts(propertyId).then((res) => {
//       setAlerts(res);
//       setLoading(false);
//     });
//   }, [propertyId]);

//   if (loading) {
//     return (
//       <div className="bg-white rounded-2xl ring-1 ring-slate-200 shadow-sm p-6 flex items-center justify-center text-sm text-slate-500">
//         Aggregating alerts from AI agents…
//       </div>
//     );
//   }

//   const colorMap = {
//     HIGH: "border-red-500 bg-red-50 text-red-700",
//     MEDIUM: "border-yellow-500 bg-yellow-50 text-yellow-700",
//     LOW: "border-green-500 bg-green-50 text-green-700",
//   };

//   return (
//     <div className="bg-white rounded-2xl ring-1 ring-slate-200 shadow-sm p-6 space-y-4">
//       <h2 className="text-sm font-semibold text-slate-900">
//         Risks & Alerts
//       </h2>

//       {alerts.map((alert, idx) => (
//         <div
//           key={idx}
//           className={`border-l-4 px-4 py-3 rounded-md ${colorMap[alert.level]}`}
//         >
//           <p className="text-xs font-semibold">{alert.level} RISK</p>
//           <p className="text-sm">{alert.message}</p>
//         </div>
//       ))}
//     </div>
//   );
// }

import { useEffect, useState } from "react";
import { Bell, AlertTriangle, CheckCircle2, AlertCircle, Loader2 } from "lucide-react";
// Re-importing to ensure the file path resolves correctly after recreation
import { fetchAlerts } from "../../api/alertAPI";

export default function AlertsPanel({ propertyId = "A" }) {
  const [alerts, setAlerts] = useState(null);
  const [loading, setLoading] = useState(true);

  // Logic Preserved: Fetching alerts on propertyId change
  useEffect(() => {
    setLoading(true);
    fetchAlerts(propertyId).then((res) => {
      setAlerts(res);
      setLoading(false);
    });
  }, [propertyId]);

  // Enhanced UI for Loading State
  if (loading) {
    return (
      <div className="bg-white rounded-2xl border border-slate-100 shadow-sm p-6 flex flex-col items-center justify-center text-slate-400 gap-2 h-48">
        <Loader2 className="animate-spin" size={20} />
        <span className="text-sm font-medium">Aggregating AI alerts...</span>
      </div>
    );
  }

  // UI Configuration Map (Visuals only)
  const styleMap = {
    HIGH: {
      bg: "bg-rose-50",
      border: "border-rose-100",
      iconColor: "text-rose-600",
      textColor: "text-slate-800",
      labelColor: "text-rose-700",
      Icon: AlertCircle
    },
    MEDIUM: {
      bg: "bg-amber-50",
      border: "border-amber-100",
      iconColor: "text-amber-600",
      textColor: "text-slate-800",
      labelColor: "text-amber-700",
      Icon: AlertTriangle
    },
    LOW: {
      bg: "bg-emerald-50",
      border: "border-emerald-100",
      iconColor: "text-emerald-600",
      textColor: "text-slate-800",
      labelColor: "text-emerald-700",
      Icon: CheckCircle2
    },
  };

  return (
    <div className="bg-white rounded-2xl border border-slate-100 shadow-sm p-6">
      <div className="flex items-center gap-2 mb-6">
        <div className="bg-indigo-50 p-2 rounded-lg">
          <Bell size={18} className="text-indigo-600" />
        </div>
        <div>
           <h2 className="text-sm font-bold text-slate-900">Risk & Alerts</h2>
           <p className="text-xs text-slate-500 font-medium">Real-time system monitoring</p>
        </div>
      </div>

      <div className="space-y-3">
        {alerts && alerts.length > 0 ? (
          alerts.map((alert, idx) => {
            // Default to LOW style if level is unknown
            const style = styleMap[alert.level] || styleMap.LOW;
            const Icon = style.Icon;

            return (
              <div
                key={idx}
                className={`flex items-start gap-3 p-4 rounded-xl border transition-all hover:shadow-md ${style.bg} ${style.border}`}
              >
                <div className={`mt-0.5 shrink-0 ${style.iconColor}`}>
                  <Icon size={18} />
                </div>
                <div className="flex-1">
                  <p className={`text-xs font-bold mb-0.5 ${style.labelColor}`}>
                    {alert.level} RISK
                  </p>
                  <p className={`text-sm font-medium leading-relaxed ${style.textColor}`}>
                    {alert.message}
                  </p>
                </div>
              </div>
            );
          })
        ) : (
          <div className="text-center py-8 text-slate-400 text-sm bg-slate-50 rounded-xl border border-dashed border-slate-200">
            No active alerts at this time.
          </div>
        )}
      </div>
    </div>
  );
}