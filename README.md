# 🚀 **EstateX Intelligence — Real Estate Analytics Platform**

AI-driven insights for forecasting, risk analysis, ESG compliance, pricing optimization, and portfolio intelligence.

---

## 📌 **Overview**

**EstateX Intelligence** is a modern real estate decision-intelligence platform that brings together:

* Financial forecasting
* ESG compliance evaluation
* Tenant churn prediction
* Occupancy forecasting
* Dynamic pricing & elasticity analysis
* Scenario simulation (what-if analysis)
* Portfolio optimization
* Lease NLP extraction
* Maintenance risk analysis
* News sentiment analysis
* Smart alerts & recommendations

The system combines a **React + Vite + Tailwind frontend** and a **FastAPI backend** using modular AI “agents”.

---

## 🧠 **Architecture**

### **Frontend**

* ⚛️ React (Vite)
* 🎨 TailwindCSS
* 📊 Recharts for visual analytics
* 🔧 Property Context Provider (global dynamic property selection)
* 🧱 Modular dashboard components
* 🌐 REST API integrations for each backend agent

### **Backend**

* ⚡ FastAPI (Python)
* 🧩 12+ agents:

  * forecasting_agent
  * esg_compliance_agent
  * pricing_agent
  * tenant_churn_agent
  * occupancy_agent
  * maintenance_agent
  * lease_nlp_agent
  * portfolio_agent
  * scenario_agent
  * news_agent
  * alerts_agent
  * memory_agent
* 📁 Data-driven forecasting using `/data/properties/<id>/rent_history.csv`
* 🔒 CORS enabled for the Vite client

---

## 📂 **Project Structure**

```
EstateX/
│
├── backend/
│   ├── agents/
│   ├── services/
│   ├── data/
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   ├── components/
│   │   ├── context/
│   │   ├── pages/
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── index.html
│   └── vite.config.js
│
└── README.md
```

---

## ⚙️ **Installation**

### **1️⃣ Backend Setup (FastAPI)**

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

API will run at:

```
http://127.0.0.1:8000
```

### **2️⃣ Frontend Setup (React + Vite)**

```bash
cd frontend
npm install
npm run dev
```

App will run at:

```
http://localhost:5173
```

---

## 🔌 **Key API Endpoints**

### **Forecasting**

```
POST /forecast
GET  /forecast?property_id=A&months_ahead=6
```

### **Pricing Optimization**

```
POST /pricing/recommend
```

### **ESG Compliance**

```
POST /esg/check
```

### **Tenant Churn Prediction**

```
GET /churn?property_id=A
```

### **Occupancy Forecasting**

```
GET /occupancy?property_id=A&months_ahead=3
```

### **Portfolio Optimization**

```
POST /portfolio
```

### **Scenario Simulation**

```
POST /scenario/run
```

### **Lease Extraction (NLP)**

```
POST /lease/extract
```

### **Maintenance Prediction**

```
POST /maintenance/predict
```

### **News Sentiment**

```
GET /news/sentiment?city=Bengaluru
```

---

## 📊 **Dashboard Features**

### ✔ Dynamic Property Selector

Changes **every component’s data** instantly via global context.

### ✔ Financial Forecasting

Predict future rent/cashflow trends with confidence scores, seasonal modeling, and inflation adjustment.

### ✔ ESG Compliance

Evaluate emissions, energy usage & benchmarks.

### ✔ Pricing Simulator

Analyze market elasticity & AI-recommended rent adjustments.

### ✔ Churn & Risk Predictions

Tenant churn probability based on historical patterns.

### ✔ Maintenance Analyzer

Sensor-driven maintenance risk detection.

### ✔ Portfolio Recommendations

AI-driven weight allocation & risk-adjusted returns.

### ✔ Scenario Simulation

"What happens if rent increases 5%?" → Instantly visualized.

### ✔ Smart Alerts

Real-time insights and warnings integrated across all agents.

---

## 📈 **Data-Driven Forecasting**

Place rent history here:

```
backend/data/properties/<property_id>/rent_history.csv
```

Example:

```csv
month,rent
2023-01,18750
2023-02,19000
2023-03,19500
...
2025-02,25500
```

Backend uses:

* history trend
* inflation
* growth factor
* seasonal pattern

---

## 🏗️ **Tech Stack**

### **Frontend**

| Tech        | Purpose                           |
| ----------- | --------------------------------- |
| React       | UI framework                      |
| Vite        | Fast bundler                      |
| Tailwind    | Styling                           |
| Recharts    | Charts & visualizations           |
| Lucide      | Icons                             |
| Context API | Global state (property selection) |

### **Backend**

| Tech            | Purpose                |
| --------------- | ---------------------- |
| FastAPI         | REST backend           |
| NumPy           | Forecast computations  |
| spaCy / NLP     | Lease extraction       |
| Async agents    | Modular business logic |
| CORS middleware | Frontend communication |

---

## 🤖 **Why This Project Is Unique**

Unlike static dashboards, **EstateX Intelligence is fully dynamic**:

* Every component reacts to global `propertyId`
* Each backend agent produces unique output per property
* Real forecasting using CSV data per property
* AI-style decision reasoning in pricing, portfolio, and churn
* Modular "agent brain" architecture (inspired by AGI-style systems)

This makes it production-grade and extensible.

---

## 🚀 **How To Add More Properties**

1. Create folder:

```
backend/data/properties/property_X/
```

2. Add rent history:

```
rent_history.csv
```

3. Add any additional metadata (optional):

```
features.json
esg.json
maintenance.csv
```

4. The entire dashboard will now work for the new property.

---

## 📜 **License**

MIT License

---

## ✨ **Author**

**Soumyadeep Sarkar** - Team Lead & ML
**Rajat Singh** - Frontend & Integration
**Nitya Nama** - ML
**Rishabh Raushan** - Backend
