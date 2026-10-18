# 📊 Customer Data Analysis

An end-to-end analysis of a customer purchase dataset: data cleaning, exploratory analysis, interactive visualizations, and a Power BI dashboard summarizing the main KPIs and business insights.

---

## 📁 Dataset

- **File:** `Customers_Fakedata.csv`
- **Raw size:** 2,150 rows × 12 columns (2,100 rows after cleaning)
- **Period:** October 2022 – July 2025
- **Main fields:** CustomerID, Age, Gender, PurchaseAmount, PurchaseDate, ProductCategory, Rating
- **Note:** The data appears synthetic (purchase amounts and ratings are spread almost uniformly), so few strong patterns are expected.

---

## 🛠️ Tools

- **Python** (pandas, NumPy) for cleaning and analysis
- **Plotly** for interactive charts
- **Kaggle Notebooks** for the analysis and visualizations
- **Power BI** for the final dashboard
- **DAX** for KPI measures

---

## 🧹 Cleaning

- Removed an empty column, a duplicated `Gender` column, and `Phone` / `Email` (not useful for the analysis)
- Removed **50 duplicate rows** (2,150 → 2,100)
- Standardized `Gender` into Male / Female / Unknown
- Treated invalid ages (`-1`, `200`) as missing instead of deleting rows or filling them with an average (only **495 customers**, about 24%, have a valid age)
- Treated ratings of `10` (291 records) as invalid, since they fall outside the 1–5 scale
- Treated the impossible date `32/13/2020` as missing (excluded only from time-based analysis)
- Kept missing product categories as **Unknown** to avoid losing a large share of purchase data
- Each analysis filters only the columns it needs, instead of dropping every row with a missing value

---

## 📊 Dashboard

A single-page Power BI dashboard with a soft green and cream theme, plus a second page for insights and summary.

**KPIs:** Total Revenue (1.02M), Purchases (2,003), Avg Purchase (509.90), Avg Rating (3.03), Customers (2,100)

**Visuals:**
- Monthly revenue trend (line chart, partial months excluded)
- Revenue by product category (bar chart)
- Gender distribution (donut chart)
- Average purchase by age group (column chart, known age only)
- Rating vs average purchase by category (bubble chart)
- Average purchase by weekday and category (heatmap matrix)
- Slicers for Year, Gender, Product Category and Age Group

---

## 💡 Insights

- **Stable, not growing:** Revenue totals 1.02M with no clear trend or seasonality from Nov 2022 to Jun 2025. Apparent dips in the first/last months and in August/September come from partial data.
- **Similar segments:** Spending is similar across gender (women 521.82, men 499.03) and age groups. Group sizes are small, so differences are not reliable.
- **Balanced categories:** Revenue shares are close (Clothing 16.0%, Electronics 15.1%, Books 14.7%, Home 14.1%, Toys 13.8%), but about 26% of revenue has an unknown category.
- **Neutral ratings:** The average rating is 3.03, spread evenly across 1–5, and unrelated to spending (correlation ≈ -0.03).
- **Weekday effect:** Saturday has the highest average basket (550), Tuesday to Thursday the lowest (487–495). The effect is modest.

**Recommendations:** test weekend promotions, improve data collection (age, category and gender are often missing), and run a follow-up survey to understand satisfaction.

---

## 📂 Structure

```
.
├── images/
│   ├── 01_gender_distribution.png
│   ├── 02_avg_purchase_by_age_group.png
│   ├── 03_revenue_by_category.png
│   ├── 04_purchase_amount_distribution.png
│   ├── 05_rating_distribution.png
│   ├── 06_monthly_revenue_trend.png
│   ├── 07_avg_purchase_by_weekday.png
│   └── Dashboard1.png
├── customers_clean.csv              # cleaned data used in Power BI
├── Customers_Fakedata.csv           # raw data
├── Customer-Sales-Dashboard.pbix    # Power BI dashboard
├── SUMMARY.pdf                      # short summary of findings
└── README.md
```

---

## ✍️ Author

**Merve**
