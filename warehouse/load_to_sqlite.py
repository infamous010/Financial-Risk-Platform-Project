from backend.database import engine
from pathlib import Path


DB_PATH = Path("warehouse/risk_platform.db")


def load_dataframe_to_sqlite(df, table_name):
    """
    Loads dataframe into SQLite table.
    """

    try:
        df.to_sql(
            table_name,
            engine,
            if_exists="replace",
            index=False
        )

        print(f"Loaded table: {table_name}")

    except Exception as e:
        print(f"Error loading {table_name}: {e}")

    finally:
        engine.dispose()