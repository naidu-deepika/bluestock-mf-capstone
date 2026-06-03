# Data Dictionary
## Bluestock MF Capstone — Column Reference

### 01_fund_master.csv
| Column | Type | Description |
|--------|------|-------------|
| amfi_code | TEXT | Unique AMFI scheme code |
| fund_house | TEXT | AMC name (e.g. SBI Mutual Fund) |
| scheme_name | TEXT | Full official scheme name |
| category | TEXT | Equity or Debt |
| sub_category | TEXT | Large Cap, Mid Cap, Small Cap etc |
| plan | TEXT | Regular or Direct |
| benchmark | TEXT | Index the fund is compared against |
| expense_ratio_pct | REAL | Annual fee charged by fund (%) |
| risk_category | TEXT | Low / Moderate / High / Very High |

### 02_nav_history.csv
| Column | Type | Description |
|--------|------|-------------|
| amfi_code | TEXT | Foreign key to fund_master |
| date | DATE | NAV date (business days only) |
| nav | REAL | Net Asset Value in Rs. |

### 03_aum_by_fund_house.csv
| Column | Type | Description |
|--------|------|-------------|
| date | DATE | Quarter end date |
| fund_house | TEXT | AMC name |
| aum_lakh_crore | REAL | AUM in Rs. lakh crore |
| aum_crore | REAL | AUM in Rs. crore |
| num_schemes | INTEGER | Number of schemes |

### 04_monthly_sip_inflows.csv
| Column | Type | Description |
|--------|------|-------------|
| month | TEXT | YYYY-MM format |
| sip_inflow_crore | REAL | Total SIP inflows in Rs. crore |
| active_sip_accounts_crore | REAL | Active SIP accounts in crore |
| new_sip_accounts_lakh | REAL | New SIP registrations in lakh |
| sip_aum_lakh_crore | REAL | SIP AUM in Rs. lakh crore |
| yoy_growth_pct | REAL | Year on year growth % |

### 08_investor_transactions.csv
| Column | Type | Description |
|--------|------|-------------|
| investor_id | TEXT | Unique investor ID |
| transaction_date | DATE | Date of transaction |
| amfi_code | TEXT | Fund invested in |
| transaction_type | TEXT | SIP / Lumpsum / Redemption |
| amount_inr | INTEGER | Transaction amount in Rs. |
| state | TEXT | Investor's state |
| city_tier | TEXT | T30 or B30 city |
| age_group | TEXT | 18-25 / 26-35 / 36-45 etc |
| gender | TEXT | Male / Female |