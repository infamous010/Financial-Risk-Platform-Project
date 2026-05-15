from ai_engine.narrative_generator import (
    generate_ai_narrative
)

result = generate_ai_narrative(
    company_name="TCS",
    risk_level="High Risk",
    volatility_score=4.2,
    anomaly_label="Anomalous",
    industry="Information Technology"
)

print(result)