import streamlit as st
from src.data import load_data, get_countries, get_latest_metrics
from src.charts import line_chart_overview, bar_top_countries


def main():
    st.set_page_config(page_title="Global Overview", page_icon="📈", layout="wide")
    st.title("Global COVID-19 Overview")
    st.write("A high-level summary of key pandemic metrics and the most impacted countries.")

    with st.spinner("Loading data..."):
        df = load_data()

    metrics = get_latest_metrics(df)
    world_cols = st.columns(4)
    world_cols[0].metric("Confirmed", f"{metrics.get('confirmed', 0):,}")
    world_cols[1].metric("Deaths", f"{metrics.get('deaths', 0):,}")
    world_cols[2].metric("Recovered", f"{metrics.get('recovered', 0):,}")
    world_cols[3].metric("Countries", f"{len(get_countries(df)):,}")

    st.markdown("---")
    st.subheader("Global confirmed cases over time")
    st.plotly_chart(line_chart_overview(df, "confirmed"), use_container_width=True, theme="streamlit")

    st.markdown("---")
    st.subheader("Top 10 countries by confirmed cases")
    st.plotly_chart(bar_top_countries(df, "confirmed", top_n=10), use_container_width=True, theme="streamlit")

    st.markdown("---")
    st.subheader("Notes")
    st.write(
        "The charts above update automatically when `data/covid_2025.csv` is refreshed. Use the Country Analysis page to compare trends for a specific nation."
    )


if __name__ == "__main__":
    main()
