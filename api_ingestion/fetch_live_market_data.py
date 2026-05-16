import pandas as pd
import yfinance as yf

import sys
from pathlib import Path


# Add project root to Python path
sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from datetime import datetime

from backend.database import engine

from api_ingestion.market_tickers import (
    NSE_TICKERS
)

from api_ingestion.data_mode import (
    DATA_MODE
)

# -----------------------------------
# VALIDATE DATA MODE
# -----------------------------------

if DATA_MODE != "live":

    raise Exception(
        "DATA_MODE is not set to live."
    )


# -----------------------------------
# FETCH LIVE MARKET DATA
# -----------------------------------

all_data = []

for ticker in NSE_TICKERS:

    print(f"Fetching data for {ticker}...")

    stock = yf.Ticker(ticker)

    df = stock.history(
        period="3mo",
        interval="1d"
    )

    df.reset_index(inplace=True)

    # Add metadata
    df["ticker"] = ticker

    df["data_source"] = "yfinance"

    df["ingestion_timestamp"] = (
        datetime.now()
    )

    all_data.append(df)


# -----------------------------------
# COMBINE ALL DATA
# -----------------------------------

market_df = pd.concat(
    all_data,
    ignore_index=True
)


# -----------------------------------
# CLEAN COLUMN NAMES
# -----------------------------------

market_df.columns = [

    col.lower().replace(" ", "_")

    for col in market_df.columns
]


# -----------------------------------
# SAVE TO SUPABASE
# -----------------------------------

market_df.to_sql(
    "live_market_data",
    engine,
    if_exists="replace",
    index=False
)


print(
    "Live market data uploaded successfully!"
)