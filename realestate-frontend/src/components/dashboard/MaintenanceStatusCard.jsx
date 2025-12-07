import { useEffect, useState } from "react";
import {
  Wrench,
  Loader2,
  CheckCircle2,
  AlertTriangle,
  AlertCircle,
} from "lucide-react";
import { fetchMaintenanceStatus } from "../../api/maintenanceAPI";

export default function MaintenanceStatusCard() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    setLoading(true);

    fetchMaintenanceStatus()
      .then((res) => {
        console.log("✅ MAINTENANCE DATA RECEIVED:", res);
        setData(res);
      })
      .catch((err) => {
        console.error("❌ Maintenance UI error:", err);
        setError("Failed to load maintenance status");
      })
      .finally(() => setLoading(false));
  }, []);

  if (loading) {
    return (
      <div className="bg-white rounded-2xl border shadow-sm p-6 h-full flex flex-col items-center justify-center gap-2 text-slate-400">
        <Loader2 className="animate-spin" />
        <span className="text-xs">Analyzing sensors…</span>
      </div>
    );
  }

  if (error) {
    return (
      <div className="bg-white rounded-2xl border border-red-100 p-6 text-red-500">
        {error}
      </div>
    );
  }

  const statusConfig = {
    NORMAL: {
      label: "All Systems Normal",
      icon: CheckCircle2,
      color: "emerald",
    },
    WARNING: {
      label: "Maintenance Warning",
      icon: AlertTriangle,
      color: "amber",
    },
    CRITICAL: {
      label: "Critical Maintenance Risk",
      icon: AlertCircle,
      color: "rose",
    },
  };

  const config = statusConfig[data.status] || statusConfig.NORMAL;
  const Icon = config.icon;

  return (
    <div className="bg-white rounded-2xl border border-slate-100 shadow-sm p-6 h-full">
      <div className="flex items-center gap-3 mb-4">
        <div className={`bg-${config.color}-50 p-2 rounded-lg`}>
          <Wrench className={`text-${config.color}-600`} size={18} />
        </div>
        <div>
          <h2 className="text-sm font-bold text-slate-900">
            Maintenance Health
          </h2>
          <p className="text-xs text-slate-500">Predictive Monitoring</p>
        </div>
      </div>

      <div
        className={`flex items-center gap-2 text-${config.color}-700 bg-${config.color}-50 px-3 py-2 rounded-xl text-sm font-semibold mb-3`}
      >
        <Icon size={16} />
        {config.label}
      </div>

      {data.alerts.length > 0 ? (
        <ul className="text-xs text-slate-600 space-y-1">
          {data.alerts.map((a, i) => (
            <li key={i}>• {a}</li>
          ))}
        </ul>
      ) : (
        <p className="text-xs text-slate-500">
          No maintenance actions required.
        </p>
      )}
    </div>
  );
}
