import sys
from pathlib import Path

# Add project root to Python path
sys.path.append(
    str(Path(__file__).resolve().parent.parent.parent)
)

import pandas as pd
import plotly.express as px
import streamlit as st

from backend.database import engine


# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="Live Market Intelligence",
    layout="wide"
)

st.title(
    "Live Market Intelligence"
)

st.markdown(
    """
    Real-time financial surveillance and
    operational market intelligence powered
    by live Yahoo Finance ingestion pipelines.
    """
)


# -----------------------------------
# LOAD DATA
# -----------------------------------

analytics_df = pd.read_sql(
    "SELECT * FROM live_market_analytics",
    engine
)

gainers_df = pd.read_sql(
    "SELECT * FROM top_gainers",
    engine
)

losers_df = pd.read_sql(
    "SELECT * FROM top_losers",
    engine
)


# -----------------------------------
# LAST UPDATED TIMESTAMP
# -----------------------------------

last_updated = analytics_df[
    "ingestion_timestamp"
].max()

st.caption(
    f"Last Updated: {last_updated}"
)


# -----------------------------------
# COMPANY SELECTOR
# -----------------------------------

ticker = st.selectbox(
    "Select Company",
    sorted(
        analytics_df["ticker"].unique()
    )
)


company_df = analytics_df[
    analytics_df["ticker"] == ticker
]


# -----------------------------------
# TIME RANGE FILTER
# -----------------------------------

time_range = st.selectbox(

    "Select Time Window",

    [
        "30 Days",
        "90 Days"
    ]
)


if time_range == "30 Days":

    filtered_df = company_df.tail(30)

else:

    filtered_df = company_df.tail(90)


# -----------------------------------
# PRICE + MOVING AVERAGE CHART
# -----------------------------------

st.subheader(
    "Price Intelligence"
)

price_fig = px.line(

    filtered_df,

    x="date",

    y=[
        "close",
        "moving_avg_7d"
    ],

    title=f"{ticker} Price Trend & Moving Average"
)

st.plotly_chart(
    price_fig,
    use_container_width=True
)


# -----------------------------------
# VOLUME TREND CHART
# -----------------------------------

st.subheader(
    "Volume Trend"
)

volume_fig = px.bar(
    company_df,
    x="date",
    y="volume",
    title=f"{ticker} Market Activity Volume"
)

st.plotly_chart(
    volume_fig,
    use_container_width=True
)


# -----------------------------------
# VOLATILITY TREND
# -----------------------------------

st.subheader(
    "Risk Volatility Monitoring"
)

volatility_fig = px.line(
    company_df,
    x="date",
    y="rolling_volatility_30d",
    title=f"{ticker} Rolling 30D Volatility"
)

st.plotly_chart(
    volatility_fig,
    use_container_width=True
)


# -----------------------------------
# TOP GAINERS & LOSERS
# -----------------------------------

col1, col2 = st.columns(2)

with col1:

    st.subheader(
        "Top Gainers"
    )

    st.dataframe(

        gainers_df[
            [
                "ticker",
                "daily_return_pct"
            ]
        ]
    )

with col2:

    st.subheader(
        "Top Losers"
    )

    st.dataframe(

        losers_df[
            [
                "ticker",
                "daily_return_pct"
            ]
        ]
    )