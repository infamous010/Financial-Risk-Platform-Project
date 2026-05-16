import sys
from pathlib import Path

# Add project root to Python path
sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

import time
import schedule
import subprocess


# -----------------------------------
# JOB FUNCTION
# -----------------------------------

def run_market_pipeline():

    print(
        "Running live market ingestion..."
    )

    subprocess.run(

        [
            sys.executable,
            "api_ingestion/fetch_live_market_data.py"
        ]
    )

    print(
        "Rebuilding analytics tables..."
    )

    subprocess.run(

        [
            sys.executable,
            "transformations/build_live_market_analytics.py"
        ]
    )

    print(
        "Pipeline completed successfully!"
    )


# -----------------------------------
# SCHEDULE DAILY RUN
# -----------------------------------

schedule.every().day.at(
    "18:30"
).do(run_market_pipeline)


print(
    "Live market scheduler running..."
)


# -----------------------------------
# KEEP PROCESS RUNNING
# -----------------------------------
run_market_pipeline()

'''while True:

    schedule.run_pending()

    time.sleep(60)'''