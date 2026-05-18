import os
import pandas as pd


def load_data(data_path: str | None = None) -> pd.DataFrame:
    if data_path is None:
        data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "covid_2025.csv")
    df = pd.read_csv(data_path)
    return preprocess_data(df)


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = df.columns.str.strip()
    lower_columns = {col.lower(): col for col in df.columns}

    # Rename source columns to standard names used by the dashboard
    column_mapping = {}
    if "date" in lower_columns:
        column_mapping[lower_columns["date"]] = "date"
    elif "day" in lower_columns:
        column_mapping[lower_columns["day"]] = "date"
    elif "time" in lower_columns:
        column_mapping[lower_columns["time"]] = "date"

    if "country" in lower_columns:
        column_mapping[lower_columns["country"]] = "country"

    if "total_cases" in lower_columns:
        column_mapping[lower_columns["total_cases"]] = "confirmed"
    elif "confirmed" in lower_columns:
        column_mapping[lower_columns["confirmed"]] = "confirmed"

    if "total_deaths" in lower_columns:
        column_mapping[lower_columns["total_deaths"]] = "deaths"
    elif "deaths" in lower_columns:
        column_mapping[lower_columns["deaths"]] = "deaths"

    if "recovered_cases" in lower_columns:
        column_mapping[lower_columns["recovered_cases"]] = "recovered"
    elif "recovered" in lower_columns:
        column_mapping[lower_columns["recovered"]] = "recovered"

    if "active_cases" in lower_columns:
        column_mapping[lower_columns["active_cases"]] = "active"
    elif "active" in lower_columns:
        column_mapping[lower_columns["active"]] = "active"

    if "total_tests" in lower_columns:
        column_mapping[lower_columns["total_tests"]] = "tests"
    elif "tests" in lower_columns:
        column_mapping[lower_columns["tests"]] = "tests"

    if column_mapping:
        df = df.rename(columns=column_mapping)

    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")

    if "country" in df.columns:
        df["country"] = df["country"].astype(str)

    numeric_cols = ["confirmed", "deaths", "recovered", "active", "tests"]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0).astype(int)

    # Drop any unnamed index columns imported from CSV
    unnamed_cols = [col for col in df.columns if col.lower().startswith("unnamed")]
    if unnamed_cols:
        df = df.drop(columns=unnamed_cols)

    return df


def get_countries(df: pd.DataFrame) -> list[str]:
    if "country" not in df.columns:
        return []
    return sorted(df["country"].dropna().unique().tolist())


def get_latest_metrics(df: pd.DataFrame) -> dict[str, int]:
    if "date" in df.columns:
        latest_date = df["date"].max()
        latest = df[df["date"] == latest_date]
    else:
        latest_date = None
        latest = df

    return {
        "date": latest_date,
        "confirmed": int(latest.get("confirmed", pd.Series([0])).sum()),
        "deaths": int(latest.get("deaths", pd.Series([0])).sum()),
        "recovered": int(latest.get("recovered", pd.Series([0])).sum()),
    }
