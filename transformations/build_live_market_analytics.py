import sys
from pathlib import Path

# Add project root to Python path
sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

import pandas as pd

from backend.database import engine


# -----------------------------------
# LOAD LIVE MARKET DATA
# -----------------------------------

df = pd.read_sql(
    "SELECT * FROM live_market_data",
    engine
)


# -----------------------------------
# CALCULATE DAILY RETURNS
# -----------------------------------

df["daily_return_pct"] = (

    df.groupby("ticker")["close"]

    .pct_change()

    * 100
)


# -----------------------------------
# CALCULATE 7-DAY MOVING AVERAGE
# -----------------------------------

df["moving_avg_7d"] = (

    df.groupby("ticker")["close"]

    .transform(
        lambda x:
        x.rolling(7).mean()
    )
)


# -----------------------------------
# CALCULATE 30-DAY VOLATILITY
# -----------------------------------

df["rolling_volatility_30d"] = (

    df.groupby("ticker")["daily_return_pct"]

    .transform(
        lambda x:
        x.rolling(30).std()
    )
)


# -----------------------------------
# CREATE TOP GAINERS / LOSERS
# -----------------------------------

latest_date = df["date"].max()

latest_df = df[
    df["date"] == latest_date
]


top_gainers = (

    latest_df

    .sort_values(
        by="daily_return_pct",
        ascending=False
    )

    .head(5)
)


top_losers = (

    latest_df

    .sort_values(
        by="daily_return_pct",
        ascending=True
    )

    .head(5)
)


# -----------------------------------
# SAVE ANALYTICS TABLES
# -----------------------------------

df.to_sql(
    "live_market_analytics",
    engine,
    if_exists="replace",
    index=False
)

top_gainers.to_sql(
    "top_gainers",
    engine,
    if_exists="replace",
    index=False
)

top_losers.to_sql(
    "top_losers",
    engine,
    if_exists="replace",
    index=False
)


print(
    "Live analytics tables created successfully!"
)