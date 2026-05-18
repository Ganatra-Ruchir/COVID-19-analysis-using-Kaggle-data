# COVID Streamlit Dashboard

A professional Streamlit dashboard for COVID-19 analytics, built to present pandemic recovery trends, global totals, and country-level insights.

## Project background

This dashboard was developed as a polished demo analytics product for a fictional pandemic response team. It simulates a real-world data science delivery pipeline: ingesting a cleaned CSV dataset, standardizing schema fields, and displaying interactive visualizations for global and country-specific COVID-19 trends.

The dashboard is designed for GitHub publication and stakeholder review, with a clean repository structure, documentation, and governance files that make it production-ready.

## Demo

Live App: [Streamlit link]

## Screenshots

- Overview page
- Country analysis page

## Dataset

Source: [Kaggle dataset link]

## Tech Stack

- Python
- Pandas
- Streamlit
- Plotly

## Data Processing

- Renamed inconsistent columns
- Parsed dates
- Filled/handled missing values
- Standardized country-level schema

## Insights

- Global case trends over time
- Top affected countries
- Country-wise comparison of confirmed, deaths, recovered

## Future Improvements

- Add vaccination analysis
- Add mortality/recovery rate KPIs
- Add download/export options

## Key features

- Global overview with confirmed cases, deaths, recovered totals, and country count
- Time series visualization for confirmed cases and top-10 affected countries
- Country-level trend analysis for confirmed, deaths, and recovered series
- Robust CSV preprocessing that handles inconsistent source column names
- Streamlit multi-page layout for easy navigation

## Repository structure

```
covid-streamlit-dashboard/
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── .gitignore
├── data/
│   └── covid_2025.csv
├── src/
│   ├── data.py
│   └── charts.py
└── pages/
    ├── 1_Overview.py
    └── 2_Country_Analysis.py
```

## Installation

1. Create and activate a Python virtual environment

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the dashboard

```bash
streamlit run app.py
```

## Data schema

The dashboard expects a dataset with the following normalized fields:

- `country` — country name
- `date` — observation date
- `confirmed` — cumulative confirmed cases
- `deaths` — cumulative deaths
- `recovered` — cumulative recoveries
- `active` — active case count
- `tests` — total tests performed

The loader also supports source columns such as `total_cases`, `total_deaths`, `recovered_cases`, `active_cases`, and `total_tests`.

## Contribution guidelines

See [CONTRIBUTING.md](CONTRIBUTING.md) for repository standards, branching guidance, and code review expectations.

## License

This project is licensed under the MIT License. See `LICENSE` for details.
