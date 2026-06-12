# Bluestock Fintech — Mutual Fund Analytics Capstone

## Overview
End-to-end Mutual Fund Analytics Platform built during Data Analyst internship at Bluestock Fintech. Covers ETL pipeline, SQL database, EDA, performance analytics, risk metrics, and Power BI dashboard using real AMFI India data.

## Tech Stack
Python, Pandas, NumPy, Matplotlib, Seaborn, Plotly, SQLite, SQLAlchemy, SciPy, Power BI

## Data Source
- AMFI India (public) — amfiindia.com
- mfapi.in REST API — live NAV data
- 40 schemes, 87K+ rows, 4.5 years of NAV history

## Project Structure
- `data/raw/` — Original 10 CSV datasets + 6 live NAV files
- `data/processed/` — Cleaned datasets and computed metrics
- `data/db/` — SQLite database (bluestock_mf.db)
- `notebooks/` — Jupyter analysis notebooks
- `scripts/` — ETL and analytics Python scripts
- `sql/` — Schema and 10 analytical queries
- `dashboard/` — Power BI dashboard file
- `reports/` — Final report, presentation, charts

## How to Run
### Step 1 — Install dependencies
pip install -r requirements.txt

### Step 2 — Run full pipeline
cd bluestock_mf_capstone
python scripts/run_pipeline.py

### Step 3 — Open dashboard
Open dashboard/bluestock_mf_dashboard.pbix in Power BI Desktop

## Dataset Descriptions
| File | Rows | Description |
|------|------|-------------|
| 01_fund_master.csv | 40 | Master list of 40 fund schemes |
| 02_nav_history.csv | 46,000 | Daily NAV 2022-2026 |
| 03_aum_by_fund_house.csv | 90 | Quarterly AUM by AMC |
| 04_monthly_sip_inflows.csv | 48 | Monthly SIP data |
| 05_category_inflows.csv | 144 | Inflows by category |
| 06_industry_folio_count.csv | 21 | Total folios over time |
| 07_scheme_performance.csv | 40 | Risk metrics per fund |
| 08_investor_transactions.csv | 32,778 | Investor transactions |
| 09_portfolio_holdings.csv | 322 | Stock holdings per fund |
| 10_benchmark_indices.csv | 8,050 | Nifty 50, Nifty 100 daily |

## Key Findings
- SIP inflows grew 3x from ₹11,517 Cr to ₹31,002 Cr (2022-2025)
- SBI Mutual Fund dominates with ₹12.5 lakh crore AUM
- Total folios doubled from 13.26 Cr to 26.12 Cr
- Direct plans consistently outperform Regular plans
- Banking sector accounts for 30%+ weight in equity funds

## Deliverables
- ETL Pipeline Script (etl_pipeline.py)
- SQLite Database (bluestock_mf.db)
- EDA Notebook (03_eda_analysis.ipynb)
- Performance Analytics (04_performance_analytics.ipynb)
- Power BI Dashboard (bluestock_mf_dashboard.pbix)
- Advanced Analytics (05_advanced_analytics.ipynb)
- Final Report (Final_Report.pdf)
- Presentation (Bluestock_MF_Presentation.pptx)

## Internship Details
- Company: Bluestock Fintech Pvt. Ltd.
- Role: Data Analyst Intern
- Duration: June 2026 (7-day capstone)
- Intern: Naidu Deepika 
