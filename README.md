# FinSight — AI-Powered Financial Risk Intelligence Platform

> **Turning fragmented market data into institutional-grade risk intelligence — automatically.**

Financial risk teams in BFSI spend 10–14 days per quarter manually compiling risk reports from fragmented data sources — market feeds, peer comparisons, news, and internal systems that don't talk to each other. FinSight automates that pipeline end-to-end, from raw data ingestion to AI-generated risk narratives, cutting report turnaround from weeks to hours.

🔗 **[Live Demo](https://your-streamlit-app-url.streamlit.app)** &nbsp;|&nbsp; 📁 **[GitHub](https://github.com/infamous010/Financial-Risk-Platform-Project)**

---

<img width="1919" height="871" alt="image" src="https://github.com/user-attachments/assets/80a5deb8-c7c3-4d03-836e-9a3a8ad16046" />
<img width="1918" height="878" alt="image" src="https://github.com/user-attachments/assets/51f755d2-92c4-41a9-9a9c-c033ccf0d08e" />
<img width="1919" height="874" alt="image" src="https://github.com/user-attachments/assets/6db15a7a-74d0-417e-b719-59af82b9d104" />

---

## Who This Is For

Built for **risk analysts, compliance teams, and CFOs** at NBFCs, fintechs, and financial institutions who need automated risk monitoring without enterprise software costs.

Adaptable for any organisation ingesting multi-source financial data and needing structured warehousing + ML anomaly detection + automated reporting.

---

## What It Does

FinSight evolved from a static financial analytics dashboard into a live AI-powered financial intelligence platform with hybrid historical and real-time market monitoring capabilities.

The platform supports:

- **Live NSE stock market ingestion** via Yahoo Finance with automated ETL workflows
- **Cloud data warehousing** on Supabase PostgreSQL for centralised analytics storage
- **Operational analytics** — rolling volatility, daily returns, moving averages, dynamic top gainers/losers
- **ML anomaly detection** via Isolation Forest to surface abnormal market behaviour
- **AI narrative generation** — locally hosted LLM (Ollama + Gemma 2B) converting risk scores into institutional-style commentary
- **Hybrid live/demo architecture** — configurable data modes for both real-time monitoring and offline fallback

---

## Dashboard Pages

### Market Analytics & Live Monitoring
Interactive time-series visualisations, live NSE stock ingestion, volatility heatmaps, and operational timestamps across all dashboard pages.

<img width="1919" height="876" alt="image" src="https://github.com/user-attachments/assets/acfb2d98-f5ac-4005-87b5-f2021714e3f9" />


### ML Anomaly Detection
Isolation Forest-based anomaly detection surfacing abnormal price and volume behaviour patterns with confidence scoring.

<img width="1910" height="878" alt="image" src="https://github.com/user-attachments/assets/cdde0729-e32d-4802-865d-72fa996ddcf9" />

### AI Narrative Engine
Custom prompt engineering layer generating institutional-style financial narratives, anomaly explanations, and risk commentary from structured data.

### Risk Intelligence & Volatility Heatmaps
Enterprise-style risk classification, peer comparison analytics, and volatility scoring across monitored companies.

<img width="1632" height="879" alt="image" src="https://github.com/user-attachments/assets/815e73db-3a1c-4f24-b6ac-0a7bfe0a0734" />
<img width="1919" height="882" alt="image" src="https://github.com/user-attachments/assets/49d1f2e4-23da-4edd-b3f8-c562f3aca2ef" />


---

## Architecture

```
Data Sources (Yahoo Finance API / CSV fallback)
        │
        ▼
ETL Ingestion Layer (Python · Pandas)
        │
        ▼
Cloud Data Warehouse (Supabase PostgreSQL · SQLAlchemy)
        │
        ▼
Analytics Transformation Pipeline
├── Rolling Volatility & Moving Averages
├── Daily Returns & Top Gainers/Losers
└── ML Anomaly Detection (Isolation Forest)
        │
        ▼
AI Narrative Layer (Ollama · Gemma 2B · Prompt Engineering)
        │
        ▼
Enterprise Streamlit Dashboard (Multi-page · Live Timestamps)
```

---

## Smart Refresh Architecture

Live market data is automatically refreshed only when stale using Streamlit's caching layer (`@st.cache_data` with TTL), eliminating the need for schedulers, paid infrastructure, or background services while minimising API usage.

```python
@st.cache_data(ttl=3600)
def fetch_market_data(tickers):
    # Fetches fresh data once per hour, cached otherwise
```

---

## Data Sources

**Live Mode:** Real-time and historical market data via `yfinance` covering top NSE-listed companies with daily OHLCV, market cap, sector data, and corporate news feeds.

**Demo Mode:** Static Indian Stock Market Dataset as offline fallback — ensuring dashboard availability independent of external API status.

```python
DATA_MODE = os.getenv("DATA_MODE", "live")  # Switch between "live" and "demo"
```

Monitored companies include Reliance Industries, TCS, HDFC Bank, Infosys, ICICI Bank, SBI, Bajaj Finance, Bharti Airtel, Kotak Mahindra Bank, and HUL — covering approximately ₹120L Cr combined market capitalisation.

---

## Tech Stack

| Layer | Tools |
|---|---|
| Data Ingestion | Python · yfinance · Pandas |
| Data Warehouse | Supabase PostgreSQL · SQLAlchemy |
| Analytics | Pandas · NumPy · Rolling Statistics |
| Machine Learning | Scikit-learn · Isolation Forest |
| AI Narrative | Ollama · Gemma 2B · Prompt Engineering |
| Dashboard | Streamlit · Plotly · Multi-page Architecture |
| Deployment | Streamlit Cloud · Supabase Cloud |
| Version Control | Git · GitHub |

---

## Latest Updates — v2.0

- Upgraded from static CSV pipeline to live NSE data ingestion via Yahoo Finance
- Migrated local SQLite to Supabase PostgreSQL cloud warehouse
- Added rolling volatility, moving averages, and dynamic top gainers/losers
- Implemented smart refresh architecture (no scheduler, no infra cost)
- Added time-series visualisations and volatility heatmaps
- Introduced hybrid live/demo data mode for resilience
- Enhanced dashboard with operational timestamps and live monitoring pages

---

## Running Locally

```bash
# Clone the repository
git clone https://github.com/infamous010/Financial-Risk-Platform-Project.git
cd Financial-Risk-Platform-Project

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Add your Supabase credentials to .env

# Run the dashboard
streamlit run app.py
```

**Environment Variables Required:**
```
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_anon_key
DATA_MODE=live  # or "demo" for offline mode
```

---

## Project Structure

```
FinSight/
├── app.py                  # Main Streamlit entry point
├── etl/                    # Modular ETL pipeline
│   ├── ingestion.py        # Yahoo Finance data ingestion
│   ├── transformation.py   # Analytics transformations
│   └── warehouse.py        # Supabase PostgreSQL integration
├── analytics/              # Analytics & ML layer
│   ├── volatility.py       # Rolling volatility calculations
│   ├── anomaly.py          # Isolation Forest detection
│   └── narratives.py       # AI narrative generation
├── pages/                  # Multi-page Streamlit dashboard
├── docs/
│   └── screenshots/        # Dashboard screenshots
└── requirements.txt
```

---

## Author

**Diya Gupta** — Financial Data Analyst specialising in BFSI ETL pipelines, compliance automation, and financial risk intelligence systems. Currently building data infrastructure for international audit engagements across BFSI clients with combined AUM exceeding $500M.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/diya-gupta-dr1001/)
[![Email](https://img.shields.io/badge/Email-diya49968%40gmail.com-red)](mailto:diya49968@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-infamous010-black)](https://github.com/infamous010)

---

## License

MIT License — free to use, adapt, and build on with attribution.
