import streamlit as st


st.set_page_config(
    page_title="Financial Risk Monitoring Platform",
    layout="wide"
)

st.title("Financial Risk Monitoring Platform")

st.markdown(
    """
    Enterprise-style financial analytics and risk intelligence platform.

    This project demonstrates:
    - ETL pipelines
    - warehouse architecture
    - analytics engineering
    - risk intelligence
    - machine learning anomaly detection
    - interactive dashboarding
    """
)

st.divider()

col1, col2 = st.columns(2)

with col1:

    st.info(
        """
        ### Phase 1 — Analytics Engineering

        Includes:
        - multi-source data ingestion
        - data transformations
        - SQLite warehouse
        - analytics modelling
        - KPI dashboards
        """
    )

with col2:

    st.warning(
        """
        ### Phase 2 — Machine Learning

        Includes:
        - Isolation Forest anomaly detection
        - anomaly scoring
        - anomaly severity classification
        - ML risk intelligence
        """
    )

st.divider()

st.success(
    "Use the sidebar navigation to explore the dashboard pages."
)