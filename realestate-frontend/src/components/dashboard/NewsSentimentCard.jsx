import { useEffect, useState } from "react";
import { Newspaper, TrendingUp, TrendingDown, Minus, Loader2 } from "lucide-react";
import { fetchNewsSentiment } from "../../api/newsSentimentAPI";

export default function NewsSentimentCard({ city = "Bengaluru" }) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setLoading(true);

    fetchNewsSentiment(city)
      .then((res) => {
        console.log("✅ NEWS SENTIMENT DATA:", res);
        setData(res);
      })
      .catch((err) => {
        console.error("❌ News sentiment error:", err);
      })
      .finally(() => setLoading(false));
  }, [city]);

  if (loading) {
    return (
      <div className="bg-white rounded-2xl p-6 border shadow-sm flex items-center justify-center gap-2 text-slate-400">
        <Loader2 className="animate-spin" size={18} />
        Analyzing news…
      </div>
    );
  }

  const sentimentUI = {
    bullish: {
      icon: TrendingUp,
      color: "text-emerald-600",
      bg: "bg-emerald-50",
      label: "Positive Market Outlook",
    },
    bearish: {
      icon: TrendingDown,
      color: "text-rose-600",
      bg: "bg-rose-50",
      label: "Negative Market Sentiment",
    },
    neutral: {
      icon: Minus,
      color: "text-amber-600",
      bg: "bg-amber-50",
      label: "Neutral Market Sentiment",
    },
  };

  const { icon: Icon, color, bg, label } = sentimentUI[data.sentiment];

  return (
    <div className={`rounded-2xl border shadow-sm p-6 bg-white`}>
      <div className="flex justify-between items-center mb-4">
        <div>
          <h2 className="text-sm font-bold text-slate-900">
            News Sentiment
          </h2>
          <p className="text-xs text-slate-500">Market Intelligence</p>
        </div>
        <div className={`p-2 rounded-lg ${bg}`}>
          <Newspaper className={`${color}`} size={18} />
        </div>
      </div>

      <div className="flex items-center gap-3 mb-3">
        <Icon className={`${color}`} size={20} />
        <span className="text-sm font-semibold capitalize">
          {data.sentiment}
        </span>
      </div>

      <div className="text-xs text-slate-500 mb-2">
        Confidence Score
      </div>

      <div className="w-full bg-slate-100 h-2 rounded-full overflow-hidden">
        <div
          className={`h-2 rounded-full ${bg}`}
          style={{ width: `${data.score * 100}%` }}
        />
      </div>

      <p className="text-xs mt-3 text-slate-600">
        {label} in <b>{data.city}</b>
      </p>
    </div>
  );
}
