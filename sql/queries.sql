-- Bluestock MF Capstone - 10 Analytical Queries
-- Day 2

-- Q1: Top 5 funds by AUM
SELECT scheme_name, fund_house, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- Q2: Average NAV per month for SBI Bluechip
SELECT strftime('%Y-%m', date) AS month, ROUND(AVG(nav), 2) AS avg_nav
FROM fact_nav
WHERE amfi_code = 119551
GROUP BY month
ORDER BY month;

-- Q3: SIP inflow YoY growth
SELECT month, sip_inflow_crore, yoy_growth_pct
FROM fact_sip_industry
WHERE yoy_growth_pct IS NOT NULL
ORDER BY month;

-- Q4: Total transactions by state
SELECT state, COUNT(*) AS total_transactions, SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;

-- Q5: Funds with expense_ratio less than 1%
SELECT scheme_name, fund_house, expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1.0
ORDER BY expense_ratio_pct;

-- Q6: Top 5 funds by Sharpe ratio
SELECT scheme_name, fund_house, sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;

-- Q7: SIP vs Lumpsum vs Redemption split
SELECT transaction_type, COUNT(*) AS count, SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY transaction_type;

-- Q8: AUM by fund house latest quarter
SELECT fund_house, aum_lakh_crore
FROM fact_aum
WHERE date = (SELECT MAX(date) FROM fact_aum)
ORDER BY aum_lakh_crore DESC;

-- Q9: Top 5 funds by 3 year return
SELECT scheme_name, fund_house, return_3yr_pct
FROM fact_performance
ORDER BY return_3yr_pct DESC
LIMIT 5;

-- Q10: Transaction count by age group
SELECT age_group, COUNT(*) AS total_transactions, ROUND(AVG(amount_inr), 0) AS avg_amount
FROM fact_transactions
GROUP BY age_group
ORDER BY avg_amount DESC;