"""
Fund Recommender Script
Bluestock Fintech - Mutual Fund Analytics Capstone
Day 6: Advanced Analytics
"""

import pandas as pd
from pathlib import Path

PROCESSED = Path("C:/Users/deepi/OneDrive/Documents/Internship/bluestock_mf_capstone/data/processed")

def recommend_funds(risk_appetite):
    """
    Recommends top 3 mutual funds based on investor risk appetite.
    
    Input: risk_appetite (str) — 'Low', 'Moderate', or 'High'
    Output: DataFrame with top 3 fund recommendations
    """
    fund_master = pd.read_csv(PROCESSED / "01_fund_master_clean.csv")
    sharpe_df = pd.read_csv(PROCESSED / "sharpe_values.csv")

    risk_map = {
        'Low': ['Low'],
        'Moderate': ['Moderate', 'Moderately High'],
        'High': ['High', 'Very High']
    }

    grades = risk_map.get(risk_appetite, [])
    filtered = fund_master[fund_master['risk_category'].isin(grades)]
    merged = filtered.merge(sharpe_df[['amfi_code', 'sharpe_ratio']], on='amfi_code', how='left')
    top3 = merged.nlargest(3, 'sharpe_ratio')[['scheme_name', 'fund_house', 'risk_category', 'sharpe_ratio', 'expense_ratio_pct']]

    return top3


if __name__ == "__main__":
    for risk in ['Low', 'Moderate', 'High']:
        print(f"\nTop 3 funds for {risk} risk appetite:")
        print(recommend_funds(risk).to_string(index=False))