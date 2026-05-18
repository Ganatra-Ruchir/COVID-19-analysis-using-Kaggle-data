import streamlit as st
from src.data import load_data, get_countries
from src.charts import line_chart_country_trends


def main():
    st.set_page_config(page_title="Country Analysis", page_icon="🌍", layout="wide")
    st.title("Country Analysis")
    st.write("Analyze COVID-19 trends for a single country with key metrics and time-series charts.")

    with st.spinner("Loading data..."):
        df = load_data()

    countries = get_countries(df)
    country = st.selectbox("Select a country", options=countries, index=0 if countries else None)

    if country:
        chart = line_chart_country_trends(df, country)
        if chart is not None:
            st.plotly_chart(chart, use_container_width=True, theme="streamlit")

            country_data = df[df["country"] == country]
            latest = country_data.sort_values("date").iloc[-1]
            latest_date = latest.get("date", "-")

            metric_cols = st.columns(3)
            metric_cols[0].metric("Latest confirmed", f"{int(latest.get('confirmed', 0)):,}")
            metric_cols[1].metric("Latest deaths", f"{int(latest.get('deaths', 0)):,}")
            metric_cols[2].metric("Latest recovered", f"{int(latest.get('recovered', 0)):,}")

            st.markdown("---")
            st.write(f"**Latest data available for:** {latest_date}")
            st.write(
                "Use this view to compare how confirmed cases, deaths, and recoveries evolve over time for the selected country."
            )
        else:
            st.warning("No data available for the selected country.")


if __name__ == "__main__":
    main()
