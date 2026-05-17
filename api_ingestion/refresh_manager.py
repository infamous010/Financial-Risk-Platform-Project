import sys
from pathlib import Path

# Add project root to Python path
sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

import subprocess
import pandas as pd

from datetime import datetime
from datetime import timedelta

from backend.database import engine


# -----------------------------------
# CHECK LAST REFRESH
# -----------------------------------

def refresh_live_data_if_needed():

    try:

        df = pd.read_sql(

            """
            SELECT MAX(ingestion_timestamp)
            AS last_refresh

            FROM live_market_data
            """,

            engine
        )

        last_refresh = df[
            "last_refresh"
        ][0]


        # -----------------------------------
        # IF NO DATA EXISTS
        # -----------------------------------

        if pd.isna(last_refresh):

            print(
                "No live data found."
            )

            run_refresh_pipeline()

            return


        # -----------------------------------
        # CHECK DATA AGE
        # -----------------------------------

        time_difference = (

            datetime.now()

            - pd.to_datetime(
                last_refresh
            )
        )


        # -----------------------------------
        # REFRESH IF OLDER THAN 6 HOURS
        # -----------------------------------

        if time_difference > timedelta(hours=6):

            print(
                "Live market data is stale."
            )

            run_refresh_pipeline()

        else:

            print(
                "Live market data still fresh."
            )


    except Exception as e:

        print(
            f"Refresh check failed: {e}"
        )


# -----------------------------------
# RUN REFRESH PIPELINE
# -----------------------------------

def run_refresh_pipeline():

    print(
        "Refreshing live market data..."
    )

    subprocess.run(

        [
            sys.executable,
            "api_ingestion/fetch_live_market_data.py"
        ]
    )

    subprocess.run(

        [
            sys.executable,
            "transformations/build_live_market_analytics.py"
        ]
    )

    print(
        "Live market refresh completed!"
    )