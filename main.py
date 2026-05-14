from ingestion.ingest_transactions import ingest_all_files
from warehouse.load_to_sqlite import load_dataframe_to_sqlite
from transformations.build_analytics_tables import create_market_summary


def main():

    datasets = ingest_all_files()

    for table_name, df in datasets.items():

        load_dataframe_to_sqlite(df, table_name)

    create_market_summary()


if __name__ == "__main__":
    main()