
import BASE_URL from "./base";

export async function fetchNewsSentiment(city = "Bengaluru") {
  const res = await fetch(
    `${BASE_URL}/news/sentiment?city=${encodeURIComponent(city)}`
  );

  if (!res.ok) {
    throw new Error("Failed to fetch news sentiment");
  }

  const data = await res.json();

  return {
    city: data.result.city,
    sentiment: data.result.sentiment, // bullish | neutral | bearish
    score: data.result.score,         // 0–1
    agent: data.agent,
  };
}
