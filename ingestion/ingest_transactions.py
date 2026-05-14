import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import pandas as pd
from transformations.clean_transactions import clean_dataframe

# Base data folder
DATA_PATH = Path("data/raw")

# Files to ingest
FILES = {
    "companies": "active_companies_list.csv",
    "quotes": "quote_data.csv",
    "news": "corporate_news_data.csv",
    "peer_comparisons": "peers_comparisons_data.csv"
}

def load_csv(file_name):
    file_path = DATA_PATH / file_name

    try:
        df = pd.read_csv(file_path)
        print(f"Loaded {file_name} successfully.")
        print(f"Shape: {df.shape}")
        print("-" * 50)
        return df

    except Exception as e:
        print(f"Error loading {file_name}: {e}")
        return None

def ingest_all_files():
    dataframes = {}

    for table_name, file_name in FILES.items():
        df = load_csv(file_name)

        if df is not None:
            cleaned_df = clean_dataframe(df)
            dataframes[table_name] = cleaned_df

    return dataframes


if __name__ == "__main__":
    datasets = ingest_all_files()

    for name, df in datasets.items():
        print(f"\nPreview of {name}:")
        print(df.head())