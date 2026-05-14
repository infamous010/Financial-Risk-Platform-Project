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

def create_sector_performance():

    conn = create_connection()

    quotes_df = pd.read_sql("SELECT * FROM quotes", conn)
    companies_df = pd.read_sql("SELECT * FROM companies", conn)

    merged_df = quotes_df.merge(
        companies_df,
        on="scripcode",
        how="left"
    )

    sector_summary = (
        merged_df
        .groupby("industry_y")
        .agg({
            "currentvalue": "mean",
            "pchange": "mean",
            "companyname_x": "count"
        })
        .reset_index()
    )

    sector_summary = sector_summary.rename(
        columns={
            "industry_y": "industry",
            "currentvalue": "avg_stock_price",
            "pchange": "avg_percentage_change",
            "companyname_x": "company_count"
        }
    )

    sector_summary.to_sql(
        "sector_performance",
        conn,
        if_exists="replace",
        index=False
    )

    print("Created analytics table: sector_performance")

    conn.close()

def create_top_movers():

    conn = create_connection()

    quotes_df = pd.read_sql(
        "SELECT * FROM quotes",
        conn
    )

    # Select relevant columns
    movers_df = quotes_df[
        [
            "companyname",
            "currentvalue",
            "change",
            "pchange",
            "totaltradedquantity"
        ]
    ].copy()

    # Top gainers
    top_gainers = (
        movers_df
        .sort_values(by="pchange", ascending=False)
        .head(10)
    )

    # Top losers
    top_losers = (
        movers_df
        .sort_values(by="pchange", ascending=True)
        .head(10)
    )

    # Save tables
    top_gainers.to_sql(
        "top_gainers",
        conn,
        if_exists="replace",
        index=False
    )

    top_losers.to_sql(
        "top_losers",
        conn,
        if_exists="replace",
        index=False
    )

    print("Created analytics table: top_gainers")
    print("Created analytics table: top_losers")

    conn.close()

def create_risk_metrics():

    conn = create_connection()

    quotes_df = pd.read_sql(
        "SELECT * FROM quotes",
        conn
    )

    risk_df = quotes_df[
        [
            "companyname",
            "currentvalue",
            "change",
            "pchange",
            "totaltradedquantity"
        ]
    ].copy()

    # Convert percentage change to absolute volatility score
    risk_df["volatility_score"] = risk_df["pchange"].abs()

    # Simple risk categorization
    risk_df["risk_level"] = risk_df["volatility_score"].apply(
        lambda x:
            "High Risk" if x >= 3 else
            "Medium Risk" if x >= 1.5 else
            "Low Risk"
    )

    # Sort highest risk first
    risk_df = risk_df.sort_values(
        by="volatility_score",
        ascending=False
    )

    # Save analytics table
    risk_df.to_sql(
        "risk_metrics",
        conn,
        if_exists="replace",
        index=False
    )

    print("Created analytics table: risk_metrics")

    conn.close()