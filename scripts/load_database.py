"""
Day 2: Load cleaned data into SQLite database
Bluestock Fintech - Mutual Fund Analytics Capstone
"""

import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

PROCESSED = Path("data/processed")
DB_PATH = "data/db/bluestock_mf.db"

engine = create_engine(f"sqlite:///{DB_PATH}")

# Load all tables
tables = {
    "dim_fund":          "01_fund_master_clean.csv",
    "fact_nav":          "02_nav_history_clean.csv",
    "fact_aum":          "03_aum_by_fund_house_clean.csv",
    "fact_sip_industry": "04_monthly_sip_inflows_clean.csv",
    "fact_category":     "05_category_inflows_clean.csv",
    "fact_folio":        "06_industry_folio_count_clean.csv",
    "fact_performance":  "07_scheme_performance_clean.csv",
    "fact_transactions": "08_investor_transactions_clean.csv",
    "fact_portfolio":    "09_portfolio_holdings_clean.csv",
    "fact_benchmark":    "10_benchmark_indices_clean.csv",
}

for table, file in tables.items():
    df = pd.read_csv(PROCESSED / file)
    df.to_sql(table, engine, if_exists="replace", index=False)
    print(f"Loaded {table}: {len(df)} rows")

print("\n ALL DATA LOADED INTO bluestock_mf.db")