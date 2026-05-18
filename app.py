import streamlit as st
from src.data import load_data, get_countries, get_latest_metrics

st.set_page_config(page_title="COVID-19 Dashboard", page_icon="🦠", layout="wide")


def main():
    df = load_data()
    metrics = get_latest_metrics(df)
    countries = get_countries(df)

    st.title("COVID-19 Dashboard")
    st.markdown("### Interactive pandemic analytics for global trends and country comparisons.")

    summary_col, info_col = st.columns([3, 1])
    with summary_col:
        st.markdown(
            """
            This dashboard presents clean, interactive COVID-19 insights backed by the latest dataset.
            Use the navigation menu to switch between the global overview and country-specific analysis.
            """
        )
        st.markdown(
            "- View overall confirmed cases, deaths, and recoveries over time.\n"
            "- Compare top affected countries.\n"
            "- Drill into country-level trends and latest metrics."
        )

    with info_col:
        st.metric("Latest snapshot", str(metrics.get("date", "-")))
        st.metric("Countries in data", f"{len(countries):,}")
        st.metric("Total records", f"{len(df):,}")
        st.metric("Data fields", "Confirmed / Deaths / Recovered")

    st.markdown("---")
    st.header("How to use this dashboard")
    st.write(
        "Use the pages menu to explore the two main sections: Overview for broad trends, and Country Analysis for detailed time series by country."
    )
    st.info(
        "Keep `data/covid_2025.csv` updated with clean date and country values for best results."
    )


if __name__ == "__main__":
    main()
