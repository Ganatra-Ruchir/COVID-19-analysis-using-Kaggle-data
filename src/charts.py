import plotly.express as px


def line_chart_overview(df, value_column: str = "confirmed"):
    if "date" not in df.columns:
        raise ValueError("The dataframe must include a 'date' column.")

    grouped = df.groupby("date")[value_column].sum().reset_index()
    return px.line(
        grouped,
        x="date",
        y=value_column,
        title=f"Global {value_column.capitalize()} Over Time",
        labels={"date": "Date", value_column: value_column.capitalize()},
    )


def bar_top_countries(df, value_column: str = "confirmed", top_n: int = 10):
    if "country" not in df.columns:
        raise ValueError("The dataframe must include a 'country' column.")

    grouped = df.groupby("country")[value_column].sum().reset_index()
    grouped = grouped.sort_values(value_column, ascending=False).head(top_n)
    return px.bar(
        grouped,
        x=value_column,
        y="country",
        orientation="h",
        title=f"Top {top_n} Countries by {value_column.capitalize()}",
        labels={"country": "Country", value_column: value_column.capitalize()},
    )


def line_chart_country_trends(df, country: str):
    if "date" not in df.columns or "country" not in df.columns:
        raise ValueError("The dataframe must include 'date' and 'country' columns.")

    subset = df[df["country"] == country]
    if subset.empty:
        return None

    daily = subset.groupby("date")[["confirmed", "deaths", "recovered"]].sum().reset_index()
    return px.line(
        daily,
        x="date",
        y=["confirmed", "deaths", "recovered"],
        title=f"COVID-19 Trends for {country}",
        labels={"value": "Count", "variable": "Metric"},
    )
