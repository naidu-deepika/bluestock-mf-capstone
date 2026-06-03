"""
Day 2: ETL Pipeline - Data Cleaning
Bluestock Fintech - Mutual Fund Analytics Capstone
"""

import pandas as pd
import numpy as np
from pathlib import Path

RAW = Path("data/raw")
PROCESSED = Path("data/processed")

# ── 1. CLEAN NAV HISTORY ──────────────────────────────────────────
print("Cleaning nav_history.csv...")
nav = pd.read_csv(RAW / "02_nav_history.csv")
nav['date'] = pd.to_datetime(nav['date'])
nav = nav.sort_values(['amfi_code', 'date'])
nav = nav.drop_duplicates()
nav = nav[nav['nav'] > 0]

# forward fill missing NAV for weekends/holidays
nav = nav.set_index('date')
nav = nav.groupby('amfi_code').apply(
    lambda x: x.reindex(
        pd.date_range(x.index.min(), x.index.max(), freq='D')
    ).ffill()
)
nav = nav.drop(columns='amfi_code').reset_index()
nav.columns = ['amfi_code', 'date', 'nav']
nav.to_csv(PROCESSED / "02_nav_history_clean.csv", index=False)
print(f"  NAV History: {nav.shape} saved")

# ── 2. CLEAN INVESTOR TRANSACTIONS ───────────────────────────────
print("Cleaning investor_transactions.csv...")
tx = pd.read_csv(RAW / "08_investor_transactions.csv")
tx['transaction_date'] = pd.to_datetime(tx['transaction_date'])
tx['transaction_type'] = tx['transaction_type'].str.strip().str.title()
tx = tx[tx['amount_inr'] > 0]
tx['kyc_status'] = tx['kyc_status'].str.strip()
tx = tx.drop_duplicates()
tx.to_csv(PROCESSED / "08_investor_transactions_clean.csv", index=False)
print(f"  Transactions: {tx.shape} saved")

# ── 3. CLEAN SCHEME PERFORMANCE ──────────────────────────────────
print("Cleaning scheme_performance.csv...")
perf = pd.read_csv(RAW / "07_scheme_performance.csv")
numeric_cols = ['return_1yr_pct', 'return_3yr_pct', 'return_5yr_pct',
                'sharpe_ratio', 'alpha', 'beta', 'expense_ratio_pct']
for col in numeric_cols:
    perf[col] = pd.to_numeric(perf[col], errors='coerce')
anomalies = perf[(perf['expense_ratio_pct'] < 0.1) | (perf['expense_ratio_pct'] > 2.5)]
print(f"  Expense ratio anomalies: {len(anomalies)}")
perf.to_csv(PROCESSED / "07_scheme_performance_clean.csv", index=False)
print(f"  Scheme Performance: {perf.shape} saved")

# ── 4. CLEAN REMAINING 7 DATASETS ────────────────────────────────
other_files = [
    "01_fund_master.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv",
]

for file in other_files:
    df = pd.read_csv(RAW / file)
    df = df.drop_duplicates()
    df = df.dropna(how='all')
    out = file.replace(".csv", "_clean.csv")
    df.to_csv(PROCESSED / out, index=False)
    print(f"  {file}: {df.shape} saved")

print("\n ALL DATASETS CLEANED AND SAVED TO data/processed/")