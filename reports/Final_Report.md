# Bluestock Fintech — Mutual Fund Analytics Platform
## Final Project Report | June 2026
**Intern:** Naidu Deepika Reddy | **Role:** Data Analyst Intern

---

## 1. Executive Summary
This project builds an end-to-end Mutual Fund Analytics Platform for Bluestock Fintech using publicly available AMFI India data. The platform ingests, cleans, and analyses data from 40 mutual fund schemes across 10 fund houses, covering 4.5 years of NAV history (Jan 2022 – May 2026). Key outputs include an ETL pipeline, SQLite database, EDA notebooks with 15+ charts, performance metrics (Sharpe, Alpha, Beta, CAGR), and an interactive Power BI dashboard.

---

## 2. Data Sources
| Source | Data Type | Rows |
|--------|-----------|------|
| AMFI India | Fund master, NAV, AUM, SIP | 87K+ |
| mfapi.in API | Live NAV (JSON) | 19K+ |
| NSE/BSE | Benchmark indices | 8,050 |
| Simulated | Investor transactions | 32,778 |

---

## 3. ETL Design
The ETL pipeline follows Extract → Transform → Load → Analyse → Visualise architecture.

**Extract:** 10 CSV datasets + live NAV from mfapi.in API

**Transform:**
- Parsed dates to datetime format
- Forward-filled missing NAV for weekends/holidays
- Standardized transaction types
- Validated AMFI codes
- Removed duplicates

**Load:** All cleaned data loaded into SQLite star schema with 10 tables

---

## 4. EDA Findings
1. SIP inflows grew 3x from ₹11,517 Cr to ₹31,002 Cr (2022-2025)
2. SBI Mutual Fund dominates AUM at ₹12.5 lakh crore
3. Total folios doubled from 13.26 Cr to 26.12 Cr
4. Large Cap funds receive highest consistent net inflows
5. Age group 26-35 has highest transaction count
6. T30 cities contribute 70%+ of total investment value
7. Banking sector accounts for 30%+ weight in equity funds
8. Direct plans have 0.3-0.9% lower expense ratio vs Regular
9. Mid Cap funds show highest 3yr returns but highest volatility
10. Large cap funds show 0.85+ correlation with each other

---

## 5. Performance Analysis
| Metric | Best Fund | Value |
|--------|-----------|-------|
| Highest 3yr CAGR | Top ranked fund | 20%+ |
| Highest Sharpe | Large Cap Direct | >1.0 |
| Lowest Max Drawdown | Liquid/Debt funds | <5% |
| Highest Alpha | Mid Cap funds | Positive |
| Lowest Expense | Direct Index funds | <0.5% |

---

## 6. Risk Metrics
- **VaR 95%:** Small cap funds show worst daily VaR (-2% to -3%)
- **CVaR:** Average loss beyond VaR threshold is -3% to -4% for equity funds
- **Rolling Sharpe:** HDFC Top 100 and SBI Bluechip consistently above 1.0
- **Sector HHI:** Several funds show high Banking sector concentration

---

## 7. Dashboard Summary
Built 4-page interactive Power BI dashboard:
- **Page 1:** Industry Overview — AUM, SIP, Folio KPIs
- **Page 2:** Fund Performance — Scorecard, NAV vs Benchmark
- **Page 3:** Investor Analytics — State, Age, Transaction type
- **Page 4:** SIP & Market Trends — SIP inflow vs Nifty 50

---

## 8. Limitations
- Investor transaction data is simulated (not real investor data)
- NAV data anchored to real values but forward-simulated
- Dashboard requires Power BI Desktop to open
- SQLite used instead of PostgreSQL (development only)

---

## 9. Recommendations
1. Schedule ETL pipeline to auto-fetch NAV daily at 8 PM
2. Build Streamlit web app for browser-based dashboard access
3. Add Monte Carlo simulation for NAV projection
4. Implement Markowitz Efficient Frontier for portfolio optimization
5. Create automated weekly email report for stakeholders

---

## 10. Conclusion
This project successfully built a complete Mutual Fund Analytics Platform covering all 8 objectives set by Bluestock Fintech. The platform demonstrates end-to-end data engineering skills from raw data ingestion to interactive dashboard delivery.

---
*Report prepared by Naidu Deepika Reddy | Bluestock Fintech Data Analyst Intern | June 2026*