# Financial Risk Monitoring Platform

## Project Overview

An enterprise-style financial analytics and risk monitoring platform built using Python, SQLite, Streamlit, and modular ETL architecture principles.

This project simulates how modern financial analytics and risk teams ingest, transform, warehouse, analyze, and monitor financial market data using layered data engineering and analytics workflows.

The platform currently supports:
- Multi-source financial data ingestion
- Automated ETL pipelines
- Data transformation and cleaning
- SQLite warehouse architecture
- Analytics-ready business tables
- Risk scoring and volatility monitoring
- Interactive Streamlit dashboarding

Check out the app on -> https://infamous010-financial-risk-platform-project.streamlit.app/

---

# Business Problem

Financial institutions and analytics teams work with fragmented financial datasets originating from:
- market feeds
- company master data
- peer comparison systems
- financial reporting systems
- corporate news sources

These datasets are often:
- inconsistent
- duplicated
- semi-structured
- difficult to analyze directly

This project aims to simulate an enterprise financial monitoring workflow by transforming raw financial datasets into structured analytics-ready business intelligence models.

---

# Current Architecture

Raw Financial CSV Files
↓
Python Ingestion Pipeline
↓
Transformation & Cleaning Layer
↓
SQLite Warehouse
↓
Analytics Models
↓
Risk Intelligence Layer
↓
Interactive Streamlit Dashboard

---

# Dataset Used

The platform currently integrates multiple financial market datasets containing:
- company information
- stock quote metrics
- peer comparisons
- corporate news feeds

Integrated datasets:
- active_companies_list.csv
- quote_data.csv
- corporate_news_data.csv
- peers_comparisons_data.csv

---

# Current Features

## 1. Multi-Source Data Ingestion

Built modular ingestion pipelines to dynamically load multiple financial datasets using Python and Pandas.

Implemented:
- automated CSV loading
- reusable ingestion functions
- validation previews
- error handling

File:
- ingestion/ingest_transactions.py

---

## 2. Transformation & Cleaning Layer

Created reusable transformation pipelines for standardizing raw financial datasets before warehouse loading.

Implemented:
- column standardization
- duplicate removal
- unnamed column cleanup
- schema normalization

File:
- transformations/clean_transactions.py

---

## 3. SQLite Warehouse Layer

Built a local warehouse architecture using SQLite to persist transformed datasets.

Implemented:
- automated table creation
- reusable warehouse loading functions
- persistent structured storage

File:
- warehouse/load_to_sqlite.py

---

## 4. Analytics Modelling Layer

Created analytics-ready business intelligence tables for downstream reporting and dashboarding.

Current analytics tables:
- market_summary
- sector_performance
- top_gainers
- top_losers

Implemented:
- warehouse joins
- aggregation pipelines
- KPI modelling
- business intelligence summaries

File:
- transformations/build_analytics_tables.py

---

## 5. Risk Intelligence Layer

Built a volatility-based financial risk scoring system for identifying high-risk companies based on abnormal market movement patterns.

Implemented:
- volatility score calculation
- risk categorization
- risk analytics modelling

Generated table:
- risk_metrics

---

## 6. Interactive Dashboard Layer

Built an interactive Streamlit dashboard for monitoring:
- market KPIs
- sector performance
- top movers
- risk metrics
- volatility insights

Implemented:
- KPI cards
- interactive charts
- risk filters
- analytics tables
- risk monitoring interface

File:
- dashboard/app.py

---

# Technologies Used

- Python
- Pandas
- SQLite
- Streamlit
- Plotly
- SQL
- Git
- VS Code

---

# Current Project Structure

financial-risk-monitoring-platform/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── curated/
│
├── ingestion/
├── transformations/
├── warehouse/
├── dashboard/
├── notebooks/
├── docs/
├── tests/
│
├── main.py
├── requirements.txt
└── README.md

---

# How To Run The Project

## Activate Virtual Environment

Windows:
venv\Scripts\activate

---

## Run ETL Pipeline

python main.py

---

## Launch Dashboard

streamlit run dashboard/app.py

---

# Current Output

The platform currently:
- ingests raw financial datasets
- transforms and standardizes data
- stores structured warehouse tables
- builds analytics-ready business models
- generates volatility-based risk metrics
- visualizes insights through an interactive dashboard

Generated warehouse & analytics tables:
- companies
- quotes
- news
- peer_comparisons
- market_summary
- sector_performance
- top_gainers
- top_losers
- risk_metrics

---

# Future Enhancements

Upcoming phases will include:
- anomaly detection pipelines
- machine learning risk models
- AI-generated financial summaries
- NLP-based news sentiment analysis
- predictive analytics
- cloud deployment architecture
