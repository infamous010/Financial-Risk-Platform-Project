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
# RISK ALERT ENGINE
# -----------------------------------

alerts = []


for _, row in latest_df.iterrows():

    # -----------------------------
    # HIGH VOLATILITY ALERT
    # -----------------------------

    if row["rolling_volatility_30d"] > 3:

        alerts.append({

            "ticker": row["ticker"],

            "alert_type":
            "High Volatility",

            "alert_message":

            f"{row['ticker']} "
            f"showing elevated "
            f"volatility levels.",

            "risk_level": "High"
        })


    # -----------------------------
    # SHARP PRICE DROP ALERT
    # -----------------------------

    if row["daily_return_pct"] < -2:

        alerts.append({

            "ticker": row["ticker"],

            "alert_type":
            "Sharp Downside Movement",

            "alert_message":

            f"{row['ticker']} "
            f"declined sharply "
            f"in latest session.",

            "risk_level": "Critical"
        })


    # -----------------------------
    # ABNORMAL VOLUME ALERT
    # -----------------------------

    avg_volume = (

        df[
            df["ticker"] == row["ticker"]
        ]["volume"]

        .mean()
    )


    if row["volume"] > avg_volume * 1.8:

        alerts.append({

            "ticker": row["ticker"],

            "alert_type":
            "Abnormal Trading Volume",

            "alert_message":

            f"{row['ticker']} "
            f"recorded abnormal "
            f"market activity volume.",

            "risk_level": "Medium"
        })


# -----------------------------------
# CREATE ALERT DATAFRAME
# -----------------------------------

alerts_df = pd.DataFrame(alerts)


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

alerts_df.to_sql(
    "market_alerts",
    engine,
    if_exists="replace",
    index=False
)


print(
    "Live analytics tables created successfully!"
)