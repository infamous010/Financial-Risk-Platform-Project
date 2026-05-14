import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
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


# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="ML Anomaly Detection",
    layout="wide"
)

st.title("ML Anomaly Detection")

st.markdown(
    """
    Isolation Forest-based anomaly detection system for identifying abnormal market behaviour patterns.
    """
)

# -----------------------------------
# LOAD TABLE
# -----------------------------------

anomaly_detection = load_table(
    "anomaly_detection"
)

# -----------------------------------
# FILTERS
# -----------------------------------

st.sidebar.header("ML Filters")

selected_severity = st.sidebar.multiselect(
    "Select Severity",
    options=anomaly_detection[
        "anomaly_severity"
    ].unique(),
    default=list(
        anomaly_detection[
            "anomaly_severity"
        ].unique()
    )
)

if selected_severity:

    filtered_anomalies = anomaly_detection[
        anomaly_detection[
            "anomaly_severity"
        ].isin(selected_severity)
    ]

else:

    filtered_anomalies = anomaly_detection.copy()

# -----------------------------------
# KPI SECTION
# -----------------------------------

st.header("ML Risk Intelligence")

col1, col2, col3 = st.columns(3)

# Total anomalies
total_anomalies = len(
    anomaly_detection[
        anomaly_detection[
            "anomaly_label"
        ] == "Anomalous"
    ]
)

# Anomaly percentage
anomaly_percentage = round(
    (
        total_anomalies
        /
        len(anomaly_detection)
    ) * 100,
    2
)

# Critical anomalies
critical_anomalies = len(
    anomaly_detection[
        anomaly_detection[
            "anomaly_severity"
        ] == "Critical"
    ]
)

col1.metric(
    "Anomalies Detected",
    total_anomalies
)

col2.metric(
    "Anomaly Percentage",
    f"{anomaly_percentage}%"
)

col3.metric(
    "Critical Anomalies",
    critical_anomalies
)

st.divider()

# -----------------------------------
# ANOMALY DISTRIBUTION CHART
# -----------------------------------

st.header("Anomaly Distribution")

anomaly_chart_data = (
    anomaly_detection[
        "anomaly_label"
    ]
    .value_counts()
    .reset_index()
)

anomaly_chart_data.columns = [
    "anomaly_label",
    "count"
]

anomaly_chart = px.bar(
    anomaly_chart_data,
    x="anomaly_label",
    y="count",
    title="ML Anomaly Detection Results"
)

st.plotly_chart(
    anomaly_chart,
    use_container_width=True
)

st.divider()

# -----------------------------------
# SEVERITY DISTRIBUTION
# -----------------------------------

st.header("Severity Distribution")

severity_chart_data = (
    anomaly_detection[
        "anomaly_severity"
    ]
    .value_counts()
    .reset_index()
)

severity_chart_data.columns = [
    "severity",
    "count"
]

severity_chart = px.pie(
    severity_chart_data,
    names="severity",
    values="count",
    title="Anomaly Severity Distribution"
)

st.plotly_chart(
    severity_chart,
    use_container_width=True
)

st.divider()

# -----------------------------------
# ANOMALY TABLE
# -----------------------------------

st.header("Detected Market Anomalies")

anomalies_only = filtered_anomalies[
    filtered_anomalies[
        "anomaly_label"
    ] == "Anomalous"
]

st.dataframe(
    anomalies_only,
    use_container_width=True
)