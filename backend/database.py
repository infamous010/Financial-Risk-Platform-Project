import os

from sqlalchemy import create_engine
from dotenv import load_dotenv


# Load local .env
load_dotenv()

# Try local env first
DATABASE_URL = os.getenv(
    "SUPABASE_DB_URL"
)

# Fallback for Streamlit Cloud
if DATABASE_URL is None:

    import streamlit as st

    DATABASE_URL = st.secrets[
        "SUPABASE_DB_URL"
    ]

# Create engine
engine = create_engine(
    DATABASE_URL
)