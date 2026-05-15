import sys
from pathlib import Path

sys.path.append(
    str(
        Path(__file__).resolve().parents[2]
    )
)

import streamlit as st
import pandas as pd
from backend.database import engine
from pathlib import Path

from ai_engine.narrative_generator import (
    generate_ai_narrative
)


DB_PATH = Path("warehouse/risk_platform.db")


# -----------------------------------
# DATABASE LOADER
# -----------------------------------

def load_table(table_name):

    df = pd.read_sql(
        f"SELECT * FROM {table_name}",
        engine
    )

    engine.dispose()

    return df


# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="AI Narrative Intelligence",
    layout="wide"
)

st.title("AI Narrative Intelligence")

st.markdown(
    """
    Generate AI-powered financial intelligence narratives
    for detected market anomalies.
    """
)

st.divider()

# -----------------------------------
# LOAD DATA
# -----------------------------------

anomaly_detection = load_table(
    "anomaly_detection"
)

# -----------------------------------
# COMPANY SELECTION
# -----------------------------------

company_list = anomaly_detection[
    "companyname"
].unique()

selected_company = st.selectbox(
    "Select Company",
    company_list
)

company_data = anomaly_detection[
    anomaly_detection[
        "companyname"
    ] == selected_company
].iloc[0]

st.divider()

# -----------------------------------
# DISPLAY METRICS
# -----------------------------------

col1, col2, col3 = st.columns(3)

col1.metric(
    "Risk Level",
    company_data["risk_level"]
)

col2.metric(
    "Volatility Score",
    round(
        company_data[
            "volatility_score"
        ],
        2
    )
)

col3.metric(
    "Anomaly Status",
    company_data[
        "anomaly_label"
    ]
)

st.divider()

# -----------------------------------
# GENERATE AI NARRATIVE
# -----------------------------------

if st.button(
    "Generate AI Financial Narrative"
):

    with st.spinner(
        "Generating AI intelligence narrative..."
    ):

        narrative = generate_ai_narrative(
            company_name=company_data[
                "companyname"
            ],
            risk_level=company_data[
                "risk_level"
            ],
            volatility_score=company_data[
                "volatility_score"
            ],
            anomaly_label=company_data[
                "anomaly_label"
            ],
            industry="Financial Markets",
            percentage_change=company_data[
                "pchange"
            ],
            monitoring_priority="Enhanced Monitoring"
        )

    st.subheader(
        "AI-Generated Financial Narrative"
    )

    st.write(narrative)