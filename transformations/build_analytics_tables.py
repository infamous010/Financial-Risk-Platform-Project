import pandas as pd
import sqlite3
from pathlib import Path


DB_PATH = Path("warehouse/risk_platform.db")


def create_connection():

    conn = sqlite3.connect(DB_PATH)

    return conn


def create_market_summary():

    conn = create_connection()

    quotes_df = pd.read_sql("SELECT * FROM quotes", conn)
    companies_df = pd.read_sql("SELECT * FROM companies", conn)

    # Merge datasets
    merged_df = quotes_df.merge(
        companies_df,
        on="scripcode",
        how="left"
    )
    print(merged_df.columns)


    # Select useful columns
    market_summary = merged_df[
    [
        "companyname_x",
        "industry_x",
        "currentvalue",
        "change",
        "pchange"
    ]
]

    market_summary = market_summary.rename(
        columns={
            "companyname_x": "companyname",
            "industry_x": "industry"
        }
    )

    # Save analytics table
    market_summary.to_sql(
        "market_summary",
        conn,
        if_exists="replace",
        index=False
    )

    print("Created analytics table: market_summary")

    conn.close()