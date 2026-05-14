import streamlit as st


# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="Risk Report Generator",
    layout="wide"
)

st.title("Financial Risk Report Generator")

st.markdown(
    """
    Generate structured financial risk intelligence reports
    using market movement and volatility indicators.
    """
)

st.divider()

# -----------------------------------
# INPUT SECTION
# -----------------------------------

st.header("Input Financial Data")

col1, col2 = st.columns(2)

# LEFT COLUMN
with col1:

    company_name = st.text_input(
        "Company Name"
    )

    current_price = st.number_input(
        "Current Stock Price",
        min_value=0.0,
        value=1000.0
    )

    percentage_change = st.number_input(
        "Percentage Change (%)",
        value=0.0
    )

    volatility_score = st.number_input(
        "Volatility Score",
        value=0.0
    )

# RIGHT COLUMN
with col2:

    risk_level = st.selectbox(
        "Risk Level",
        [
            "Low Risk",
            "Medium Risk",
            "High Risk"
        ]
    )

    industry = st.text_input(
        "Industry"
    )

    trading_volume = st.text_input(
        "Trading Volume"
    )

    peer_observation = st.text_area(
        "Peer Comparison Observation"
    )

# Full width section
analyst_notes = st.text_area(
    "Analyst Notes"
)

st.divider()

# -----------------------------------
# REPORT GENERATION
# -----------------------------------

if st.button("Generate Risk Report"):

    # -----------------------------------
    # EXECUTIVE SUMMARY
    # -----------------------------------

    executive_summary = f"""
    {company_name} currently exhibits a percentage movement of
    {percentage_change}% with a volatility score of
    {volatility_score}.

    The company operates within the {industry} sector
    and is currently categorized as {risk_level}.
    """

    # -----------------------------------
    # RISK ASSESSMENT
    # -----------------------------------

    if risk_level == "High Risk":

        risk_assessment = (
            "The company demonstrates elevated market risk "
            "characteristics driven by abnormal movement "
            "patterns and heightened volatility indicators."
        )

    elif risk_level == "Medium Risk":

        risk_assessment = (
            "The company demonstrates moderate market risk "
            "with observable volatility fluctuations that "
            "require periodic monitoring."
        )

    else:

        risk_assessment = (
            "The company currently demonstrates relatively "
            "stable market behaviour with lower volatility exposure."
        )

    # -----------------------------------
    # MONITORING RECOMMENDATION
    # -----------------------------------

    if volatility_score >= 3:

        recommendation = (
            "Enhanced short-term monitoring is recommended "
            "due to elevated volatility indicators and "
            "potential abnormal movement behaviour."
        )

    else:

        recommendation = (
            "Standard monitoring procedures are currently "
            "sufficient based on observed market behaviour."
        )

    # -----------------------------------
    # REPORT OUTPUT
    # -----------------------------------

    st.header("Generated Financial Risk Report")

    st.subheader("Executive Summary")

    st.write(executive_summary)

    st.subheader("Risk Assessment")

    st.write(risk_assessment)

    st.subheader("Market Behaviour Analysis")

    st.write(
        f"Current Stock Price: {current_price}"
    )

    st.write(
        f"Trading Volume Observation: {trading_volume}"
    )

    st.write(
        f"Peer Comparison Insight: {peer_observation}"
    )

    st.write(
        f"Analyst Notes: {analyst_notes}"
    )

    st.subheader("Monitoring Recommendation")

    st.write(recommendation)

    st.success(
        "Risk report generated successfully."
    )