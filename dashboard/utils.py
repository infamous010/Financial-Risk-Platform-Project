import sqlite3
import pandas as pd
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