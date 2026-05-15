import pandas as pd


def standardize_column_names(df):
    """
    Standardizes column names:
    - lowercase
    - replaces spaces with underscores
    """

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # Rename unnamed index column
    df.columns = [
        "id" if "unnamed" in col
        else col
        for col in df.columns
    ]

    return df


def remove_unnamed_columns(df):
    """
    Removes unnamed index columns.
    """

    unnamed_cols = [col for col in df.columns if "unnamed" in col]

    df = df.drop(columns=unnamed_cols)

    return df


def remove_duplicates(df):
    """
    Removes duplicate rows.
    """

    return df.drop_duplicates()


def clean_dataframe(df):
    """
    Full cleaning pipeline.
    """

    df = standardize_column_names(df)

    df = remove_unnamed_columns(df)

    df = remove_duplicates(df)

    return df