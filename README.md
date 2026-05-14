# Financial Risk Monitoring Platform

## Project Overview

This project is an enterprise-style financial analytics and risk monitoring platform built using Python, SQLite, and modular ETL architecture principles.

The goal of the project is to simulate how financial institutions and analytics teams ingest, transform, warehouse, and analyze large-scale financial datasets for reporting and business intelligence purposes.

The current phase focuses on:
- Multi-source data ingestion
- Data cleaning and transformation
- Warehouse creation using SQLite
- Analytics-ready data modelling

Future phases will expand into:
- Risk scoring
- Machine learning pipelines
- AI-generated financial insights
- Dashboarding and monitoring systems

---

# Business Problem

Financial institutions work with large volumes of fragmented financial data originating from:
- market feeds
- company statements
- transaction systems
- news sources
- peer comparison datasets

These datasets are often:
- inconsistent
- duplicated
- poorly formatted
- difficult to analyze directly

This project aims to build a scalable pipeline that transforms raw financial datasets into structured analytics-ready warehouse tables.

---

# Current Project Architecture

Raw CSV Files
↓
Python Ingestion Pipeline
↓
Cleaning & Transformation Layer
↓
SQLite Warehouse
↓
Analytics Tables

---

# Dataset Used

The project currently uses a multi-source Indian financial markets dataset containing:
- company master data
- stock quote information
- corporate news data
- peer comparison metrics

Files currently integrated:
- active_companies_list.csv
- quote_data.csv
- corporate_news_data.csv
- peers_comparisons_data.csv

---

# Current Features

## 1. Multi-Source Data Ingestion

Built reusable ingestion pipelines to load multiple financial datasets dynamically using Python and Pandas.

Implemented:
- automated CSV loading
- error handling
- modular ingestion logic
- dataset previews for validation

File:
- ingestion/ingest_transactions.py

---

## 2. Transformation & Cleaning Layer

Created reusable transformation functions to standardize incoming datasets before warehouse loading.

Implemented:
- column standardization
- duplicate removal
- unnamed column cleanup
- schema consistency improvements

File:
- transformations/clean_transactions.py

---

## 3. SQLite Warehouse Layer

Built a local SQLite warehouse to persist transformed financial datasets.

Implemented:
- automated table creation
- warehouse loading functions
- persistent structured storage
- modular database connection handling

File:
- warehouse/load_to_sqlite.py

---

## 4. Analytics Modelling Layer

Created the first analytics-ready business table:
- market_summary

This layer merges multiple warehouse tables to generate structured business intelligence datasets for downstream analytics.

Implemented:
- warehouse joins
- schema conflict handling
- curated analytics modelling

File:
- transformations/build_analytics_tables.py

---

# Technologies Used

- Python
- Pandas
- SQLite
- VS Code
- Git
- SQL

---

# Current Project Structure

financial-risk-monitoring-platform/

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

## Run Pipeline

python main.py

---

# Current Output

The pipeline currently:
- ingests multiple raw financial datasets
- transforms and standardizes them
- stores them in SQLite warehouse tables
- creates analytics-ready market summary tables

Generated warehouse tables:
- companies
- quotes
- news
- peer_comparisons
- market_summary

---

# Next Planned Improvements

Upcoming phases will include:
- advanced analytics tables
- anomaly detection
- financial risk scoring
- machine learning pipelines
- AI-generated financial summaries
- interactive dashboards