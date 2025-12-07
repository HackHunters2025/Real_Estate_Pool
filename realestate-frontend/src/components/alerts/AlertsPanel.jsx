import { useEffect, useState } from "react";
import {
  Bell,
  AlertTriangle,
  CheckCircle2,
  AlertCircle,
  Loader2,
} from "lucide-react";

import { fetchAlerts } from "../../api/alertAPI";

export default function AlertsPanel({ propertyId = "A" }) {
  const [alerts, setAlerts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setLoading(true);

    fetchAlerts(propertyId)
      .then((res) => {
        console.log("✅ ALERTS FROM BACKEND:", res);
        setAlerts(res);
      })
      .catch((err) => {
        console.error("❌ Alerts UI error:", err);
        setAlerts([]);
      })
      .finally(() => setLoading(false));
  }, [propertyId]);

  if (loading) {
    return (
      <div className="bg-white rounded-2xl border border-slate-100 shadow-sm p-6 flex flex-col items-center justify-center text-slate-400 gap-2 h-48">
        <Loader2 className="animate-spin" size={20} />
        <span className="text-sm font-medium">
          Aggregating AI alerts…
        </span>
      </div>
    );
  }

  const styleMap = {
    HIGH: {
      bg: "bg-rose-50",
      border: "border-rose-100",
      icon: AlertCircle,
      iconColor: "text-rose-600",
      label: "HIGH RISK",
      labelColor: "text-rose-700",
    },
    MEDIUM: {
      bg: "bg-amber-50",
      border: "border-amber-100",
      icon: AlertTriangle,
      iconColor: "text-amber-600",
      label: "MEDIUM RISK",
      labelColor: "text-amber-700",
    },
    LOW: {
      bg: "bg-emerald-50",
      border: "border-emerald-100",
      icon: CheckCircle2,
      iconColor: "text-emerald-600",
      label: "LOW RISK",
      labelColor: "text-emerald-700",
    },
  };

  return (
    <div className="bg-white rounded-2xl border border-slate-100 shadow-sm p-6">
      <div className="flex items-center gap-2 mb-6">
        <div className="bg-indigo-50 p-2 rounded-lg">
          <Bell size={18} className="text-indigo-600" />
        </div>
        <div>
          <h2 className="text-sm font-bold text-slate-900">
            Risk & Alerts
          </h2>
          <p className="text-xs text-slate-500 font-medium">
            AI system monitoring
          </p>
        </div>
      </div>

      {alerts.length > 0 ? (
        <div className="space-y-3">
          {alerts.map((alert, idx) => {
            const style = styleMap[alert.level] || styleMap.LOW;
            const Icon = style.icon;

            return (
              <div
                key={idx}
                className={`flex items-start gap-3 p-4 rounded-xl border transition-all hover:shadow-md ${style.bg} ${style.border}`}
              >
                <div className={`mt-0.5 ${style.iconColor}`}>
                  <Icon size={18} />
                </div>

                <div className="flex-1">
                  <p
                    className={`text-xs font-bold mb-1 ${style.labelColor}`}
                  >
                    {style.label}
                  </p>
                  <p className="text-sm text-slate-800 leading-relaxed">
                    {alert.message}
                  </p>
                </div>
              </div>
            );
          })}
        </div>
      ) : (
        <div className="text-center py-8 text-slate-400 text-sm bg-slate-50 rounded-xl border border-dashed border-slate-200">
          No active alerts at this time.
        </div>
      )}
    </div>
  );
}
