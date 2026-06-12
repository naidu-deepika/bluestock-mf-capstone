# Bluestock MF Capstone — Presentation Outline
## 12 Slides

---

### Slide 1 — Title
**Mutual Fund Analytics Platform**
Bluestock Fintech | Data Analyst Internship | June 2026
Naidu Deepika Reddy

---

### Slide 2 — Problem & Objective
**Problem:**
- NAV, AUM, SIP data scattered across different sources
- No unified platform to compare 40+ funds
- Investors can't easily compute risk-adjusted returns

**Objective:**
- Build end-to-end analytics platform
- ETL + SQL + EDA + Dashboard

---

### Slide 3 — Data Sources
- 10 CSV datasets from AMFI India
- Live NAV from mfapi.in API
- 40 schemes, 87K+ rows, 4.5 years
- Benchmark indices from NSE/BSE

---

### Slide 4 — Architecture
Extract → Transform → Load → Analyse → Visualise
- Python ETL pipeline
- SQLite star schema (10 tables)
- Jupyter notebooks
- Power BI dashboard

---

### Slide 5 — EDA Highlights 1
- SIP inflows grew 3x (₹11,517 Cr to ₹31,002 Cr)
- SBI dominates AUM at ₹12.5 lakh crore
- Folios doubled from 13.26 Cr to 26.12 Cr
[Chart: SIP Inflow Trend + AUM Growth]

---

### Slide 6 — EDA Highlights 2
- Age group 26-35 invests the most
- T30 cities contribute 70%+ of investments
- Banking sector = 30%+ of equity fund holdings
[Chart: Demographics + Sector Allocation]

---

### Slide 7 — Performance Metrics 1
- CAGR computed for 1yr, 3yr, 5yr
- Sharpe Ratio: Top funds > 1.0
- Sortino Ratio: Penalizes only downside risk
[Chart: Fund Scorecard Table]

---

### Slide 8 — Performance Metrics 2
- Alpha: Top funds beat Nifty 100
- Beta: Debt funds near 0, Equity near 1
- Max Drawdown: Small cap worst at -35%
[Chart: Benchmark Comparison Chart]

---

### Slide 9 — Dashboard Screenshots 1
Page 1: Industry Overview
Page 2: Fund Performance
[Insert Power BI screenshots]

---

### Slide 10 — Dashboard Screenshots 2
Page 3: Investor Analytics
Page 4: SIP & Market Trends
[Insert Power BI screenshots]

---

### Slide 11 — Key Findings
1. SIP culture growing rapidly in India
2. Direct plans consistently outperform Regular
3. Mid Cap funds best returns but highest risk
4. Banking sector dominates equity portfolios
5. 26-35 age group is core MF investor demographic

---

### Slide 12 — Thank You
**Naidu Deepika Reddy**
Data Analyst Intern | Bluestock Fintech
GitHub: github.com/naidu-deepika/bluestock-mf-capstone
June 2026