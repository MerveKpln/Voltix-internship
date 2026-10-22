# 📊 NYC Airbnb Market Analysis (2019)

An end-to-end data analysis project on New York City Airbnb listings: from raw data and cleaning to exploratory analysis, an interactive Power BI dashboard, business insights and recommendations.

**Key questions:** How is the market structured? What drives listing prices? Where is demand strongest?

---

## 📁 Dataset

- **Source:** Airbnb New York City 2019 open data (`AB_NYC_2019.csv`), the only dataset used.
- **Size:** 48,895 rows x 16 columns (raw) → 48,870 rows x 22 columns (clean).
- **Main columns:** `neighbourhood_group`, `neighbourhood`, `room_type`, `price`, `minimum_nights`, `number_of_reviews`, `reviews_per_month`, `last_review`, `calculated_host_listings_count`, `availability_365`, `latitude`, `longitude`.
- **Note:** The dataset has no rating column, so reviews are used as a proxy for booking activity, not guest satisfaction.

---

## 🛠️ Tools

| Purpose | Tools |
|---|---|
| Analysis | Python, pandas, NumPy |
| Visualization | Plotly, Matplotlib, Seaborn |
| Environment | Kaggle Notebook |
| Dashboard | Power BI (DAX) |
| Reporting | Word / PDF, PowerPoint |

---

## 🧹 Cleaning

| Issue | Action |
|---|---|
| `reviews_per_month` missing (10,052) | Filled with 0 (all were listings with 0 reviews) |
| `name`, `host_name` missing | Filled with "Unknown", columns dropped |
| `last_review` stored as text | Converted to datetime (left empty where no review exists) |
| Price = 0 (11 rows), `minimum_nights` > 365 (14 rows) | Removed (25 rows, 0.05%) |
| Price > $500 (2.1% of listings) | Flagged as outliers, not removed |
| Duplicates | None found |

**New features:** `is_inactive`, `has_reviews`, `host_type`, `stay_type`, `price_category`, `last_review_year`, `log_price`.

---

## 📊 Dashboard

An interactive Power BI dashboard with three pages:

- **Overview:** 5 KPIs, map, room-type mix, listings by borough, top 15 neighbourhoods.
- **Pricing & Demand:** 4 KPIs, price quartiles by borough, borough x room type price heatmap, reviews by minimum stay, neighbourhood performance bubble chart, last-review trend.
- **Key Insight:** summary of the main insights and recommendations.

**Filters:** borough, room type, price category, host type (all charts cross-filter).

> Open `New York City Airbnb Dashboard.pbix` with Power BI Desktop (Windows). GitHub cannot preview `.pbix` files.

<!-- Add your dashboard screenshots here, for example:
![Overview](images/dashboard_overview.png)
![Pricing & Demand](images/dashboard_pricing_demand.png)
-->

---

## 💡 Insights

1. **Concentrated market:** Manhattan (44.3%) and Brooklyn (41.1%) hold 85.4% of listings; entire homes and private rooms make up about 98%.
2. **Location drives price:** the median entire-home price is $191 in Manhattan vs $100 in the Bronx; price has only weak correlations with reviews or availability (|r| ≤ 0.11).
3. **Outer boroughs show more activity per listing:** median reviews per month are 1.21 to 1.41 in Queens, the Bronx and Staten Island vs 0.61 to 0.66 in Manhattan and Brooklyn.
4. **Luxury demand drops:** only 60% of listings above $500 have a review, vs 82% in the $76-150 range.
5. **Shorter minimum stays are booked more often:** 1.00 reviews per month at 1-3 nights vs 0.23 to 0.40 for longer minimums.
6. **Supply is overstated:** 35.9% of listings have a fully blocked calendar, while hosts with 6+ listings keep calendars open 283 to 319 days a year.

**Recommendations:** benchmark by borough and room type, explore outer boroughs (Queens first), keep standard listings at $76-150, test shorter minimum stays, and size the market using active listings only.

**Limitations:** no rating column, single snapshot (July 2019), small samples in the Bronx and Staten Island, results show associations rather than causes.

---

## 📂 Structure

```
├── figures/                                              # Interactive Plotly charts (HTML)
│   ├── 01_price_distribution.html
│   ├── 02_room_type_donut.html
│   ├── 03_top_neighbourhoods.html
│   ├── 04_borough_share.html
│   ├── 05_price_by_borough_box.html
│   ├── 06_price_cat_vs_reviews_box.html
│   ├── 07_reviews_by_price_category.html
│   ├── 08_correlation_heatmap.html
│   ├── 09_price_heatmap_borough_room.html
│   ├── 10_room_type_price_demand.html
│   └── 15_last_review_trend.html
├── images/                                               # Static chart images (PNG)
│   ├── newplot.png
│   └── newplot (1).png ... newplot (8).png
├── AB_NYC_2019_clean.csv                                 # Cleaned dataset
├── ab-nyc-2019-analysis.ipynb                            # Analysis notebook
├── Final Project Report.pdf                              # Final report
├── New York City Airbnb Dashboard.pbix                   # Power BI dashboard
└── NYC_Airbnb_Final_Presentation.pptx                    # Final presentation
```

---

## ✍️ Author

**Merve**
Data Analysis Intern

[Kaggle](https://www.kaggle.com/code/mervebzn/ab-nyc-2019-analysis) 