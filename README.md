# FinSight — AI-Powered Financial Risk Intelligence Platform

An end-to-end, cloud-native BFSI financial intelligence platform integrating data engineering, ML-based risk monitoring, and LLM-powered narrative generation — built to simulate enterprise-grade financial analytics workflows.

**Live App →** https://infamous010-financial-risk-platform-project.streamlit.app/

---

## What It Does

FinSight ingests multi-source financial market datasets, transforms and warehouses them in a cloud PostgreSQL database, runs ML-based anomaly detection, and generates institutional-style risk narratives using a locally hosted LLM — all surfaced through a multi-page enterprise dashboard.

---

## Architecture

```
Multi-Source Financial CSVs
        ↓
Python Ingestion Layer (ingestion/)
        ↓
Transformation & Cleaning Layer (transformations/)
        ↓
Cloud PostgreSQL Warehouse — Supabase (warehouse/)
        ↓
Analytics & Risk Intelligence Layer (backend/)
        ↓
ML Anomaly Detection Layer (ml_models/)
        ↓
AI Narrative Engine — Ollama + Gemma (ai_engine/)
        ↓
Multi-Page Streamlit Dashboard (dashboard/)
```

---

## Tech Stack

| Layer | Tools |
|---|---|
| Data Engineering | Python, Pandas, SQLAlchemy |
| Warehouse | PostgreSQL (Supabase) |
| ML / Risk | Scikit-learn, Isolation Forest |
| AI / LLM | Ollama, Gemma |
| Dashboard | Streamlit, Plotly |
| Deployment | Streamlit Cloud, Supabase, Environment-based secret management |

---

## Features

### 1. Modular ETL Pipeline
Reusable ingestion and transformation pipelines handling multi-source financial datasets — automating cleaning, schema normalization, and warehouse loading across:
- `active_companies_list.csv`
- `quote_data.csv`
- `corporate_news_data.csv`
- `peers_comparisons_data.csv`

### 2. Cloud PostgreSQL Warehouse
Analytics-ready warehouse tables built on Supabase PostgreSQL via SQLAlchemy ORM:
- `companies`, `quotes`, `news`, `peer_comparisons`
- `market_summary`, `sector_performance`, `top_gainers`, `top_losers`
- `risk_metrics`, `anomaly_scores`

### 3. Risk Intelligence Layer
Volatility-based risk scoring and classification system identifying high-risk market behaviour across sectors — generating structured `risk_metrics` for downstream monitoring.

### 4. ML Anomaly Detection
Isolation Forest model identifying statistically abnormal market movement patterns — dynamically surfacing anomalies across the dashboard with confidence scoring.

### 5. AI Narrative Engine
Locally hosted LLM (Ollama + Gemma) with a custom prompt engineering layer generating:
- Institutional-style market intelligence commentary
- Anomaly investigation summaries
- Risk monitoring narratives

Output resembles analyst-grade financial intelligence rather than generic chatbot responses.

### 6. Multi-Page Enterprise Dashboard
Interactive Streamlit application with five dedicated views:
- **Market Analytics** — KPIs, sector performance, top movers
- **Risk Monitoring** — Volatility scores, risk classification
- **ML Anomaly Detection** — Isolation Forest outputs, anomaly explorer
- **Financial Report Generator** — Automated report generation
- **AI Narrative Intelligence** — LLM-generated market commentary

---

## Project Structure

```
finsight/
│
├── ingestion/              # Data ingestion pipelines
├── transformations/        # Cleaning and analytics table generation
├── warehouse/              # PostgreSQL warehouse loading (Supabase)
├── backend/                # Risk intelligence and KPI modelling
├── ml_models/              # Isolation Forest anomaly detection
├── ai_engine/              # Ollama + Gemma LLM narrative layer
├── dashboard/              # Multi-page Streamlit app
├── data/raw/               # Source financial CSVs
│
├── main.py                 # ETL orchestration entry point
├── requirements.txt
└── README.md
```

---

## Running Locally

### Prerequisites
- Python 3.10+
- [Ollama](https://ollama.ai) installed with Gemma model pulled (`ollama pull gemma`)
- Supabase project with connection string (or swap for local PostgreSQL)

### Setup

```bash
# Clone the repo
git clone https://github.com/infamous010/Financial-Risk-Platform-Project.git
cd Financial-Risk-Platform-Project

# Create and activate virtual environment
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Add environment variables
# Create a .env file with your Supabase connection string:
# DATABASE_URL=postgresql://...
```

### Run

```bash
# Run ETL pipeline
python main.py

# Launch dashboard
streamlit run dashboard/app.py
```

---

## Deployment

- **Dashboard:** Streamlit Cloud
- **Warehouse:** Supabase PostgreSQL (cloud-hosted)
- **AI Layer:** Locally hosted (Ollama) — not deployed to cloud
- **Secrets:** Environment variable-based secret management

---

## Author

**Diya Gupta** — Data Analyst, ETL & BFSI Financial Reporting  
[LinkedIn](https://linkedin.com) · diya49968@gmail.com
