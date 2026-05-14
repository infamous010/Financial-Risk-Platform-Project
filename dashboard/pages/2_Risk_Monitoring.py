import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
from pathlib import Path


DB_PATH = Path("warehouse/risk_platform.db")


def load_table(table_name):

    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql(
        f"SELECT * FROM {table_name}",
        conn
    )

    conn.close()

    return df


# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="Risk Monitoring",
    layout="wide"
)

st.title("Risk Monitoring")

st.markdown(
    "Volatility-based financial risk intelligence and monitoring system."
)

# -----------------------------------
# LOAD TABLES
# -----------------------------------

risk_metrics = load_table("risk_metrics")

# -----------------------------------
# SIDEBAR FILTERS
# -----------------------------------

st.sidebar.header("Risk Filters")

selected_risk = st.sidebar.multiselect(
    "Select Risk Level",
    options=risk_metrics["risk_level"].unique(),
    default=list(
        risk_metrics["risk_level"].unique()
    )
)

if selected_risk:

    filtered_risk = risk_metrics[
        risk_metrics["risk_level"].isin(selected_risk)
    ]

else:

    filtered_risk = risk_metrics.copy()

# -----------------------------------
# KPI SECTION
# -----------------------------------

st.header("Risk Overview")

col1, col2, col3 = st.columns(3)

# High risk companies
col1.metric(
    "High Risk Companies",
    len(
        risk_metrics[
            risk_metrics["risk_level"] == "High Risk"
        ]
    )
)

# Average volatility
col2.metric(
    "Average Volatility Score",
    round(
        risk_metrics["volatility_score"].mean(),
        2
    )
)

# Highest volatility company
highest_volatility_company = (
    risk_metrics
    .sort_values(
        by="volatility_score",
        ascending=False
    )
    .iloc[0]["companyname"]
)

col3.metric(
    "Highest Volatility Company",
    highest_volatility_company
)

st.divider()

# -----------------------------------
# RISK DISTRIBUTION CHART
# -----------------------------------

st.header("Risk Distribution")

risk_distribution = (
    risk_metrics["risk_level"]
    .value_counts()
    .reset_index()
)

risk_distribution.columns = [
    "risk_level",
    "count"
]

risk_chart = px.pie(
    risk_distribution,
    names="risk_level",
    values="count",
    title="Risk Level Distribution"
)

st.plotly_chart(
    risk_chart,
    use_container_width=True
)

st.divider()

# -----------------------------------
# RISK TABLE
# -----------------------------------

st.header("Risk Intelligence Table")

st.dataframe(
    filtered_risk,
    use_container_width=True
)