import sqlite3
import pandas as pd
from pathlib import Path
from sklearn.ensemble import IsolationForest


DB_PATH = Path("warehouse/risk_platform.db")


def create_connection():
    """
    Creates SQLite database connection.
    """

    conn = sqlite3.connect(DB_PATH)

    return conn


def run_anomaly_detection():
    """
    Runs Isolation Forest anomaly detection
    on financial risk metrics.
    """

    conn = create_connection()

    # Load risk metrics table
    risk_df = pd.read_sql(
        "SELECT * FROM risk_metrics",
        conn
    )

    # -----------------------------------
    # FEATURE ENGINEERING
    # -----------------------------------

    features = risk_df[
        [
            "currentvalue",
            "change",
            "pchange",
            "volatility_score"
        ]
    ]

    # -----------------------------------
    # ISOLATION FOREST MODEL
    # -----------------------------------

    model = IsolationForest(
        contamination=0.1,
        random_state=42
    )

    # Train model
    model.fit(features)

    # Generate predictions
    predictions = model.predict(features)

    # Generate anomaly confidence scores
    anomaly_scores = model.decision_function(features)

    # -----------------------------------
    # STORE MODEL OUTPUTS
    # -----------------------------------

    risk_df["anomaly_flag"] = predictions

    risk_df["anomaly_label"] = risk_df[
        "anomaly_flag"
    ].apply(
        lambda x:
            "Anomalous"
            if x == -1
            else "Normal"
    )

    # Lower score = more anomalous
    risk_df["anomaly_score"] = anomaly_scores

    # Severity classification
    risk_df["anomaly_severity"] = risk_df[
        "anomaly_score"
    ].apply(
        lambda x:
            "Critical" if x < -0.10 else
            "High" if x < -0.05 else
            "Medium" if x < 0 else
            "Low"
    )

    # Sort highest risk anomalies first
    risk_df = risk_df.sort_values(
        by="anomaly_score"
    )

    # -----------------------------------
    # SAVE RESULTS
    # -----------------------------------

    risk_df.to_sql(
        "anomaly_detection",
        conn,
        if_exists="replace",
        index=False
    )

    print("Created ML table: anomaly_detection")

    conn.close()


if __name__ == "__main__":

    run_anomaly_detection()