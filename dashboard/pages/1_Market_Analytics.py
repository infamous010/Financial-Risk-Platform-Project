import sys
from pathlib import Path

# Add project root to Python path
sys.path.append(
    str(Path(__file__).resolve().parent.parent.parent)
)

import streamlit as st
import pandas as pd
import plotly.express as px

from backend.database import engine


# -----------------------------------
# LOAD TABLE FUNCTION
# -----------------------------------

def load_table(table_name):

    df = pd.read_sql(
        f"SELECT * FROM {table_name}",
        engine
    )

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
    """
    Financial market performance and
    sector intelligence dashboard.
    """
)


# -----------------------------------
# LOAD TABLES
# -----------------------------------

market_summary = load_table(
    "market_summary"
)

sector_performance = load_table(
    "sector_performance"
)

live_gainers = load_table(
    "top_gainers"
)

live_losers = load_table(
    "top_losers"
)


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
    "Highest Live Return %",
    round(
        live_gainers[
            "daily_return_pct"
        ].max(),
        2
    )
)

st.divider()


# -----------------------------------
# CHARTS SECTION
# -----------------------------------

st.header("Sector Analytics")

chart_col1, chart_col2 = st.columns(2)


# -----------------------------------
# SECTOR PERFORMANCE CHART
# -----------------------------------

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


# -----------------------------------
# LIVE TOP GAINERS CHART
# -----------------------------------

with chart_col2:

    gainers_chart = px.bar(

        live_gainers,

        x="ticker",
        y="daily_return_pct",

        title="Live Top Gainers"
    )

    st.plotly_chart(
        gainers_chart,
        use_container_width=True
    )


st.divider()


# -----------------------------------
# LIVE MARKET MOVERS
# -----------------------------------

st.header(
    "Live Market Movers"
)

table_col1, table_col2 = st.columns(2)


# -----------------------------------
# TOP GAINERS TABLE
# -----------------------------------

with table_col1:

    st.subheader(
        "Top Gainers"
    )

    st.dataframe(

        live_gainers[
            [
                "ticker",
                "close",
                "daily_return_pct",
                "volume"
            ]
        ],

        use_container_width=True
    )


# -----------------------------------
# TOP LOSERS TABLE
# -----------------------------------

with table_col2:

    st.subheader(
        "Top Losers"
    )

    st.dataframe(

        live_losers[
            [
                "ticker",
                "close",
                "daily_return_pct",
                "volume"
            ]
        ],

        use_container_width=True
    )