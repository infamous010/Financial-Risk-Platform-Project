from sqlalchemy import create_engine
from dotenv import load_dotenv
import os


# Load .env variables
load_dotenv()

# Fetch variables
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")

# SQLAlchemy connection string
DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{USER}:{PASSWORD}@"
    f"{HOST}:{PORT}/"
    f"{DBNAME}?sslmode=require"
)

# Create engine
engine = create_engine(DATABASE_URL)