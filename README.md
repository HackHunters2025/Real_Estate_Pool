# 🏢 EstateX Intelligence

> **EstateX Intelligence** is a real-estate decision intelligence platform that combines  
> forecasting, pricing, ESG, churn, maintenance, portfolio optimization, and more into  
> a single, agent-powered dashboard for asset managers, developers, and CRE operators.

This project is built as a **hackathon prototype with real-world B2B applicability**:  
It is structured like a production system (modular backend agents + React dashboard),  
but lightweight enough to run locally end-to-end.

---

## 🔍 Problem Statement

Traditional real-estate operations suffer from **fragmented data and reactive decisions**:

- Finance teams work on static Excel models.
- Operations teams react to issues (maintenance, churn) after they occur.
- Pricing decisions are often manual or gut-based.
- ESG & compliance tracking is siloed and manual.
- Portfolio decisions are not directly tied to live asset performance.

**EstateX Intelligence** addresses this by offering a **unified, AI-assisted intelligence layer**  
on top of real-estate data — enabling faster, data-driven, proactive decisions.

---

## 🎯 What This Platform Does

From a single dashboard, an operator can:

- 📈 **Forecast Rent/Cash Flow** for each property
- 💸 **Simulate Dynamic Pricing** and see impact on revenue
- 🧠 **Monitor Tenant Churn Risk**
- 🏠 **Track Occupancy Trends**
- 🌱 **Check ESG Compliance** vs thresholds
- 🏚 **Monitor Maintenance Risk**
- 📑 **Extract Key Terms from Leases** (NLP)
- 🔮 **Run What-If Scenarios** (rent/occupancy/expense changes)
- 📊 **Optimize Portfolio Allocation**
- 📰 **See City-Level News Sentiment**
- 🚨 **Review Consolidated AI Alerts**

All of this is powered by a **multi-agent backend** and a **React + Tailwind dashboard**.

---

## 🧩 High-Level Architecture

- **Frontend**
  - React (Vite)
  - TailwindCSS
  - Recharts for charts
  - Global `PropertyContext` to switch between properties
  - Components: Forecast, ESG, Churn, Pricing, Scenario, Lease, Alerts, etc.

- **Backend**
  - FastAPI (Python)
  - Multiple “agents” encapsulating different business functions:
    - `forecasting_agent`
    - `pricing_agent`
    - `tenant_churn_agent`
    - `occupancy_agent`
    - `esg_compliance_agent`
    - `maintenance_agent`
    - `lease_nlp_agent`
    - `portfolio_agent`
    - `scenario_agent`
    - `news_agent`
    - `alerts_agent`
    - `memory_agent`
  - Service layer (`services/*.py`) with forecasting, rules, etc.
  - File-based data under `backend/data/properties/<property_id>/`

---

## 📁 Folder Structure

A simplified view of the repository structure:

```bash
.
├── backend/
│   ├── main.py                     # FastAPI app entry point (includes routers + CORS)
│   ├── agents/
│   │   ├── forecasting_agent.py
│   │   ├── pricing_agent.py
│   │   ├── esg_compliance_agent.py
│   │   ├── maintenance_agent.py
│   │   ├── vendor_cost_agent.py
│   │   ├── news_agent.py
│   │   ├── alerts_agent.py
│   │   ├── occupancy_agent.py
│   │   ├── tenant_churn_agent.py
│   │   ├── portfolio_agent.py
│   │   ├── scenario_agent.py
│   │   ├── lease_nlp_agent.py
│   │   ├── memory_agent.py
│   │   └── __init__.py
│   ├── services/
│   │   ├── forecasting_service.py  # run_forecasting, simple_forecast, etc.
│   │   ├── esg_rules_service.py
│   │   ├── maintenance_service.py
│   │   ├── churn_service.py
│   │   ├── portfolio_service.py
│   │   ├── scenario_service.py
│   │   └── file_loader.py
│   ├── data/
│   │   └── properties/
│   │       ├── property_A/
│   │       │   ├── rent_history.csv
│   │       │   └── ... (other property-level files)
│   │       ├── property_B/
│   │       └── property_C/
│   └── requirements.txt
│
└── frontend/
    ├── index.html
    ├── vite.config.js
    ├── package.json
    └── src/
        ├── main.jsx
        ├── App.jsx
        ├── layouts/
        │   └── DashboardLayout.jsx
        ├── context/
        │   └── propertyContext.jsx
        ├── pages/
        │   ├── Home.jsx
        │   └── Dashboard.jsx
        ├── components/
        │   ├── common/
        │   │   └── PropertySelector.jsx
        │   ├── dashboard/
        │   │   ├── ForecastChart.jsx
        │   │   ├── ESGStatusCard.jsx
        │   │   ├── ChurnRiskCard.jsx
        │   │   ├── PricingSlider.jsx
        │   │   ├── ScenarioSimulator.jsx
        │   │   ├── LeaseAnalyzer.jsx
        │   │   ├── MaintenanceStatusCard.jsx
        │   │   └── OccupancyCard.jsx
        │   └── alerts/
        │       └── AlertsPanel.jsx
        └── api/
            ├── base.js              # BASE_URL for backend
            ├── forecastAPI.js
            ├── pricingAPI.js
            ├── churnAPI.js
            ├── esgAPI.js
            ├── alertsAPI.js
            ├── scenarioAPI.js
            ├── leaseAPI.js
            ├── maintenanceAPI.js
            ├── occupancyAPI.js
            ├── portfolioAPI.js
            └── newsAPI.js
````

> 🌱 New properties can be added by creating a folder under
> `backend/data/properties/<property_id>/` and pointing the UI selector to it.

---

## ⚙️ Tech Stack

**Frontend**

* React (Vite)
* TailwindCSS
* Recharts
* Lucide Icons
* Context API for property selection

**Backend**

* FastAPI
* Python 3.x
* NumPy / basic data utilities
* Modular “agent” architecture

---

## 🚀 How to Run the Project Locally

### 1️⃣ Backend Setup (FastAPI)

```bash
cd backend

# (Optional but recommended)
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

pip install -r requirements.txt

# Run backend
uvicorn main:app --reload
```

By default, the backend will run at:

```text
http://127.0.0.1:8000
```

You can view auto-generated API docs (Swagger):

```text
http://127.0.0.1:8000/docs
```

---

### 2️⃣ Frontend Setup (React + Vite)

```bash
cd frontend
npm install
npm run dev
```

This will start the frontend dev server, usually at:

```text
http://localhost:5173
```

> Make sure the backend (port `8000`) and frontend (port `5173`) are both running.
> CORS is already configured in `backend/main.py` to allow these origins.

---

## 🧪 How to Use the App (Judge / Stakeholder Walkthrough)

1. **Open Home Page**

   * Go to `http://localhost:5173/`
   * You’ll see a marketing-style landing page with major developers and a CTA.

2. **Click “Get Started” / “Start Exploring”**

   * This navigates to `/dashboard`.

3. **Select a Property (Top Right)**

   * Use the **PropertySelector** in the dashboard header.
   * When you switch property, the context updates and triggers all cards & charts to refetch using that `propertyId`.

4. **Explore Modules:**

   * **Cash Flow Forecast (Top Left)**
     Fetches from `POST /forecast` for the selected property and plots 6-month projected rent / cash flow.

   * **ESG Status Card**
     Calls `POST /esg/check` and shows PASS/FAIL with usage bar and message.

   * **Churn Risk Card**
     Uses `GET /churn?property_id=...` and shows a normalized risk score and drivers.

   * **Dynamic Pricing Slider**
     Moves a range input and fires `POST /pricing/recommend` to compute new rent and annual revenue.

   * **Scenario Simulator**
     Adjust rent/occupancy/expense sliders → calls `POST /scenario` and visualizes NOI over time.

   * **Maintenance Status Card**
     Calls `POST /maintenance/predict` using sensor-like mock data.

   * **Occupancy Card**
     Calls `GET /occupancy?property_id=...&months_ahead=3` and shows rate + trend.

   * **Lease Analyzer**
     Demonstrates lease extraction using `POST /lease/extract` (NLP-based backend).

   * **Alerts Panel**
     Fetches `GET /alerts/dashboard` and shows synthesized alerts from agent-chain memory.

   * **(Optional Extension) News Sentiment**
     `GET /news/sentiment?city=Bengaluru` → can be plugged into a small card showing bullish/bearish score.

---

## 🔌 Key API Endpoints (Backend)

Some important endpoints exposed by FastAPI:

* `POST /forecast`
  → Rent / cash flow forecast for given property & parameters.

* `POST /pricing/recommend`
  → Recommended rent based on demand score.

* `GET /churn`
  → Tenant churn risk and top drivers.

* `GET /occupancy`
  → Occupancy forecast and trend.

* `POST /esg/check`
  → ESG compliance evaluation.

* `POST /maintenance/predict`
  → Maintenance risk & alerts.

* `POST /lease/extract`
  → Extracts key fields from lease text/file.

* `POST /portfolio`
  → Portfolio optimization recommendation.

* `POST /scenario`
  → “What-if” NOI projection under changed conditions.

* `GET /alerts/dashboard`
  → Aggregated alerts from past agent runs.

* `GET /news/sentiment`
  → City-level property news sentiment.

Swagger UI: `http://127.0.0.1:8000/docs`

---

## 🧪 Hackathon Angle vs Real-World Readiness

### For Hackathon Judging

* **Innovation**: Multi-agent AI architecture applied to real estate operations, not just a single model.
* **Technical Depth**:

  * Modular FastAPI agents
  * Scenario engine
  * Forecasting using history + inflation + seasonal factors
  * Context-driven frontend (property-aware APIs)
* **UX**: Single pane of glass dashboard with multiple AI modules.

### For Real-World / B2B Use

* Agents can be:

  * Swapped out for production-grade ML models.
  * Connected to real databases (Postgres/Snowflake/BigQuery).
* Data folders per property make it extensible for real portfolios.
* Clear separation between:

  * **Experience layer** (React UI)
  * **Intelligence layer** (agents)
  * **Data layer** (files/db)

---

## 📌 Limitations (Current Prototype)

* Uses synthetic / sample data for demo properties.
* Models are lightweight (rule-based / simple logic) for speed and clarity.
* Authentication/authorization is not yet integrated (hackathon scope).
* Lease extraction uses simplified assumptions vs full LLM/NLP pipeline.

----

## 📜 License

MIT License (can be adapted for enterprise licensing if needed).

----

## 🤝 Contributors / Team

Built as part of a hackathon project with the goal of evolving into a **production-ready real estate intelligence platform** for enterprises.

> For collaborations, enterprise interest, or integration ideas, feel free to reach out.
