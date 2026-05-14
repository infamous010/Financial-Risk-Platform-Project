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
    page_title="Market Analytics",
    layout="wide"
)

st.title("Market Analytics")

st.markdown(
    "Financial market performance and sector intelligence dashboard."
)

# -----------------------------------
# LOAD TABLES
# -----------------------------------

market_summary = load_table("market_summary")
sector_performance = load_table("sector_performance")
top_gainers = load_table("top_gainers")
top_losers = load_table("top_losers")

# -----------------------------------
# KPI SECTION
# -----------------------------------

st.header("Market Overview")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Companies",
    len(market_summary)
)

col2.metric(
    "Average Market Change %",
    round(
        market_summary["pchange"].mean(),
        2
    )
)

col3.metric(
    "Highest Gainer %",
    round(
        top_gainers["pchange"].max(),
        2
    )
)

st.divider()

# -----------------------------------
# CHARTS SECTION
# -----------------------------------

st.header("Sector Analytics")

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

# Top gainers chart
with chart_col2:

    gainers_chart = px.bar(
        top_gainers,
        x="companyname",
        y="pchange",
        title="Top Gainers"
    )

    st.plotly_chart(
        gainers_chart,
        use_container_width=True
    )

st.divider()

# -----------------------------------
# TOP MOVERS TABLES
# -----------------------------------

st.header("Top Market Movers")

table_col1, table_col2 = st.columns(2)

with table_col1:

    st.subheader("Top Gainers")

    st.dataframe(
        top_gainers,
        use_container_width=True
    )

with table_col2:

    st.subheader("Top Losers")

    st.dataframe(
        top_losers,
        use_container_width=True
    )