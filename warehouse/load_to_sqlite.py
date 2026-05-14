import sqlite3
from pathlib import Path


DB_PATH = Path("warehouse/risk_platform.db")


def create_connection():
    """
    Creates SQLite database connection.
    """

    conn = sqlite3.connect(DB_PATH)

    return conn


def load_dataframe_to_sqlite(df, table_name):
    """
    Loads dataframe into SQLite table.
    """

    conn = create_connection()

    try:
        df.to_sql(
            table_name,
            conn,
            if_exists="replace",
            index=False
        )

        print(f"Loaded table: {table_name}")

    except Exception as e:
        print(f"Error loading {table_name}: {e}")

    finally:
        conn.close()