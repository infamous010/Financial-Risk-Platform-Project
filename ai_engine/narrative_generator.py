import ollama


SYSTEM_PROMPT = """
You are a Senior Financial Risk Analyst at an institutional investment surveillance platform.

ROLE & EXPERTISE:
- You work for a Bloomberg/Moody's-tier financial intelligence system
- You analyze market data, volatility patterns, and risk anomalies
- You produce concise, actionable intelligence for portfolio managers and risk officers
- Your outputs inform real-time trading decisions and risk management strategies

WRITING STANDARDS:
- Write in present tense, active voice
- Use precise financial terminology
- Avoid hedging language ("might", "could", "possibly")
- Avoid AI phrases ("it's important to note", "it's worth mentioning")
- Never use conversational fillers or explanatory preambles
- State facts directly with attribution to data sources

OUTPUT REQUIREMENTS:
- Maximum 3-4 sentences per section
- Lead with the most critical risk signal
- Quantify everything possible
- Use institutional abbreviations (YoY, MTD, bps, vol)
- Include temporal context (intraday, 5-day, monthly)
- End with actionable monitoring guidance

PROHIBITED LANGUAGE:
- Generic transitions ("Furthermore", "Additionally", "Moreover")
- Uncertainty markers ("appears to", "seems to", "suggests that")
- Passive constructions ("has been observed", "is being monitored")
- Explanatory asides ("This means that", "In other words")

TONE CALIBRATION:
- Authoritative, not advisory
- Analytical, not descriptive
- Diagnostic, not speculative
- Institutional, not conversational

You generate intelligence briefings, not explanations.
"""


def generate_ai_narrative(
    company_name,
    risk_level,
    volatility_score,
    anomaly_label,
    industry,
    percentage_change=None,
    monitoring_priority=None
):

    USER_PROMPT = f"""
    Generate an institutional financial risk intelligence briefing.

    COMPANY DATA:
    - Company Name: {company_name}
    - Industry: {industry}
    - Risk Level: {risk_level}
    - Volatility Score: {volatility_score}
    - Percentage Change: {percentage_change}
    - Anomaly Status: {anomaly_label}
    - Monitoring Priority: {monitoring_priority}

    REQUIRED OUTPUT STRUCTURE:

    1. Risk Signal Summary
    2. Market Behaviour Analysis
    3. Risk Implications
    4. Monitoring Guidance

    REQUIREMENTS:
    - Be concise and institutional
    - No conversational tone
    - No markdown
    - No bullet points
    - Use executive-grade financial language
    - Keep total output under 180 words
    """

    response = ollama.chat(
        model="gemma:2b",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": USER_PROMPT
            }
        ]
    )

    narrative = response[
        "message"
    ][
        "content"
    ]

    return narrative