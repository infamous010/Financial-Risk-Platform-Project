import streamlit as st


# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="AI Risk Report Generator",
    layout="wide"
)

st.title("AI-Assisted Financial Risk Intelligence Engine")

st.markdown(
    """
    Generate intelligent financial risk reports using
    market movement behaviour, volatility indicators,
    and anomaly-aware financial intelligence logic.
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

    previous_price = st.number_input(
        "Previous Closing Price",
        min_value=0.0,
        value=1000.0
    )

    current_price = st.number_input(
        "Current Stock Price",
        min_value=0.0,
        value=1050.0
    )

# RIGHT COLUMN
with col2:

    industry = st.text_input(
        "Industry"
    )

    trading_volume = st.text_input(
        "Trading Volume"
    )

    peer_observation = st.text_area(
        "Peer Comparison Observation"
    )

analyst_notes = st.text_area(
    "Additional Analyst Notes"
)

st.divider()

# -----------------------------------
# REPORT GENERATION
# -----------------------------------

if st.button("Generate AI Risk Report"):

    # -----------------------------------
    # AUTO CALCULATE PERCENTAGE CHANGE
    # -----------------------------------

    if previous_price == 0:

        percentage_change = 0

    else:

        percentage_change = (
            (
                current_price - previous_price
            )
            /
            previous_price
        ) * 100

    percentage_change = round(
        percentage_change,
        2
    )

    # -----------------------------------
    # VOLATILITY SCORE
    # -----------------------------------

    volatility_score = abs(
        percentage_change
    )

    # -----------------------------------
    # RISK CLASSIFICATION
    # -----------------------------------

    if volatility_score < 1.5:

        risk_level = "Low Risk"

    elif volatility_score < 3:

        risk_level = "Medium Risk"

    else:

        risk_level = "High Risk"

    # -----------------------------------
    # VOLATILITY INTERPRETATION
    # -----------------------------------

    if volatility_score < 1:

        volatility_interpretation = (
            "Low Volatility"
        )

    elif volatility_score < 2:

        volatility_interpretation = (
            "Moderate Volatility"
        )

    elif volatility_score < 4:

        volatility_interpretation = (
            "Elevated Volatility"
        )

    else:

        volatility_interpretation = (
            "Extreme Volatility"
        )

    # -----------------------------------
    # MONITORING PRIORITY
    # -----------------------------------

    if volatility_score >= 4:

        monitoring_priority = (
            "Immediate Attention Required"
        )

    elif volatility_score >= 2:

        monitoring_priority = (
            "Enhanced Monitoring Recommended"
        )

    else:

        monitoring_priority = (
            "Routine Monitoring"
        )

    # -----------------------------------
    # EXECUTIVE SUMMARY
    # -----------------------------------

    executive_summary = f"""
    {company_name} currently exhibits a percentage
    movement of {percentage_change}% based on the
    observed movement between the previous closing
    price and current market price.

    The company operates within the {industry} sector
    and currently demonstrates
    {volatility_interpretation.lower()} characteristics.

    Current market intelligence indicators classify
    the company as {risk_level}.
    """

    # -----------------------------------
    # ANALYST COMMENTARY
    # -----------------------------------

    if risk_level == "High Risk":

        analyst_commentary = (
            "The company demonstrates elevated market "
            "risk characteristics driven by significant "
            "price movement behaviour and abnormal "
            "volatility indicators. Current observations "
            "suggest increased short-term uncertainty "
            "relative to stable market conditions."
        )

    elif risk_level == "Medium Risk":

        analyst_commentary = (
            "The company demonstrates moderate market "
            "risk with observable volatility fluctuations "
            "requiring continued monitoring and periodic "
            "market review."
        )

    else:

        analyst_commentary = (
            "The company currently demonstrates relatively "
            "stable market behaviour with controlled "
            "volatility exposure and lower short-term "
            "risk indicators."
        )

    # -----------------------------------
    # MONITORING RECOMMENDATION
    # -----------------------------------

    if risk_level == "High Risk":

        recommendation = (
            "Enhanced monitoring procedures are strongly "
            "recommended due to elevated volatility "
            "behaviour and abnormal market movement "
            "characteristics."
        )

    elif risk_level == "Medium Risk":

        recommendation = (
            "Periodic monitoring and volatility tracking "
            "are recommended to identify potential changes "
            "in market behaviour."
        )

    else:

        recommendation = (
            "Standard monitoring procedures are currently "
            "sufficient based on observed market behaviour."
        )

    # -----------------------------------
    # REPORT OUTPUT
    # -----------------------------------

    st.header("Generated Financial Intelligence Report")

    st.subheader("Automated Risk Metrics")

    st.write(
        f"Percentage Change: {percentage_change}%"
    )

    st.write(
        f"Volatility Score: {volatility_score}"
    )

    st.write(
        f"Volatility Interpretation: {volatility_interpretation}"
    )

    st.write(
        f"Risk Classification: {risk_level}"
    )

    st.write(
        f"Monitoring Priority: {monitoring_priority}"
    )

    st.divider()

    st.subheader("Executive Summary")

    st.write(executive_summary)

    st.subheader("AI-Generated Analyst Commentary")

    st.write(analyst_commentary)

    st.subheader("Market Behaviour Analysis")

    st.write(
        f"Trading Volume Observation: {trading_volume}"
    )

    st.write(
        f"Peer Comparison Insight: {peer_observation}"
    )

    st.write(
        f"Additional Analyst Notes: {analyst_notes}"
    )

    st.subheader("Monitoring Recommendation")

    st.write(recommendation)

    st.success(
        "AI-assisted financial risk report generated successfully."
    )