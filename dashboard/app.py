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


# -------------------------------
# PAGE CONFIG
# -------------------------------

st.set_page_config(
    page_title="Financial Risk Monitoring Platform",
    layout="wide"
)

st.title("Financial Risk Monitoring Platform")

st.markdown(
    "Enterprise-style analytics dashboard for financial market monitoring and risk intelligence."
)

# -------------------------------
# LOAD TABLES
# -------------------------------

market_summary = load_table("market_summary")
sector_performance = load_table("sector_performance")
top_gainers = load_table("top_gainers")
top_losers = load_table("top_losers")
risk_metrics = load_table("risk_metrics")

# -------------------------------
# SIDEBAR FILTERS
# -------------------------------

st.sidebar.header("Filters")

selected_risk = st.sidebar.multiselect(
    "Select Risk Level",
    options=risk_metrics["risk_level"].unique(),
    default=list(risk_metrics["risk_level"].unique())
)

if selected_risk:
    filtered_risk = risk_metrics[
        risk_metrics["risk_level"].isin(selected_risk)
    ]
else:
    filtered_risk = risk_metrics.copy()

# -------------------------------
# KPI SECTION
# -------------------------------

st.header("Market Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Companies",
    len(market_summary)
)

col2.metric(
    "Average Market Change %",
    round(market_summary["pchange"].mean(), 2)
)

col3.metric(
    "High Risk Companies",
    len(
        risk_metrics[
            risk_metrics["risk_level"] == "High Risk"
        ]
    )
)

col4.metric(
    "Highest Gainer %",
    round(top_gainers["pchange"].max(), 2)
)

# -------------------------------
# CHARTS SECTION
# -------------------------------

st.header("Market Analytics")

chart_col1, chart_col2 = st.columns(2)

# Sector performance chart
with chart_col1:

    sector_chart = px.bar(
        sector_performance.sort_values(
            by="avg_percentage_change",
            ascending=False
        ),
        x="industry",
        y="avg_percentage_change",
        title="Sector Performance"
    )

    st.plotly_chart(
        sector_chart,
        use_container_width=True
    )

# Risk distribution chart
with chart_col2:

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
        title="Risk Distribution"
    )

    st.plotly_chart(
        risk_chart,
        use_container_width=True
    )

# -------------------------------
# TOP MOVERS
# -------------------------------

st.header("Top Market Movers")

mover_col1, mover_col2 = st.columns(2)

with mover_col1:

    st.subheader("Top Gainers")

    st.dataframe(
        top_gainers,
        use_container_width=True
    )

with mover_col2:

    st.subheader("Top Losers")

    st.dataframe(
        top_losers,
        use_container_width=True
    )

# -------------------------------
# RISK MONITORING
# -------------------------------

st.header("Risk Monitoring")

st.dataframe(
    filtered_risk,
    use_container_width=True
)