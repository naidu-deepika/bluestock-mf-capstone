# Bluestock Fintech — Mutual Fund Analytics Capstone

## Overview
End-to-end data analytics platform for Indian mutual funds built during my internship at Bluestock Fintech.

## Tech Stack
Python, Pandas, NumPy, Matplotlib, Seaborn, Plotly, SQLite, SQLAlchemy, Power BI

## Data Source
AMFI India (public), mfapi.in API — 40 schemes, 87K+ rows, 4.5 years of NAV history

## Project Structure
- `data/raw/` — Original CSV datasets
- `data/processed/` — Cleaned data
- `data/db/` — SQLite database
- `notebooks/` — Jupyter analysis notebooks
- `scripts/` — ETL and analytics Python scripts
- `sql/` — Schema and queries
- `dashboard/` — Power BI file
- `reports/` — Final report and presentation

## How to Run
```bash
pip install -r requirements.txt
python scripts/live_nav_fetch.py
python scripts/etl_pipeline.py
```

## Status
🚧 In Progress — 7-day internship capstone (June 2026)