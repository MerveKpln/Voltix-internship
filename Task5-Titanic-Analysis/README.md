# 📊 Titanic Passenger Analysis Dashboard

An end-to-end data analysis project on the classic Titanic passenger dataset — from raw data to a fully interactive Python dashboard. Built as part of a Data Analysis & Dashboard internship task.

---

## 📁 Dataset

- **Source:** Titanic passenger dataset (Kaggle), 418 passengers, 12 original columns.
- **Columns:** PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked.
- **Note:** In this dataset, the `Survived` column matches `Sex` with 100% overlap (all women survived, no men did), mirroring a known Kaggle baseline assumption rather than a genuine historical outcome. Survival-based findings are shown for reference only throughout this project.

---

## 🛠️ Tools

- **Python** — Pandas, NumPy
- **Kaggle Notebook** — data cleaning, missing value imputation, feature engineering, KPI calculation
- **Streamlit** — interactive dashboard
- **Plotly** — interactive charts (funnel, donut, treemap, histogram, box, bar)
- **ReportLab** — Key Insights PDF

---

## 🧹 Cleaning

- **Missing values:**
  - `Fare` (1 missing) → filled with the median fare of the same `Pclass`.
  - `Age` (86 missing) → filled with the median age of the same `Pclass` + `Sex` group.
  - `Cabin` (327 missing, 78%) → converted into a `Has_Cabin` missingness indicator; a `Deck` feature was extracted from the first letter, then the raw `Cabin` column was dropped.
- **Duplicates:** checked, none found.
- **Outliers:** checked with the IQR method on `Age`, `Fare`, `SibSp`, `Parch` — no rows removed, since all extreme values represent real passengers (infants, elderly, large families, high 1st-class fares) rather than data errors.
- **Feature engineering:** `FamilySize` (SibSp + Parch + 1), `IsAlone`, `AgeGroup` (Child / Teen / Adult / Senior).

---

## 📊 Dashboard

Built with Streamlit + Plotly, featuring:

- Live filters (Passenger Class, Sex, Embarked, Age Group) with instant KPI/chart updates
- Overview KPI cards (Total Passengers, Average Age, Median Fare, Avg. Family Size)
- Demographic charts: Sex (donut), Pclass (funnel), Embarked × Pclass (stacked bar), Age (histogram), Fare by Class (box plot), Family Size (area chart)
- Survived breakdown section (clearly flagged as reference-only, given the Data Note above)
- Dark theme with a custom purple gradient design

**Screenshots:**

![Dashboard view 1](images/dashboard1.png)
![Dashboard view 2](images/dashboard2.png)
![Dashboard view 3](images/dashboard3.png)

**Run it locally:**

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 💡 Insights

- 52.2% of passengers traveled 3rd class, only 25.6% in 1st class — the ship's population skews toward the economy segment.
- Cherbourg (C) had the wealthiest passenger mix (54.9% 1st class), while Queenstown (Q) was almost entirely 3rd class (89.1%).
- 60.5% of passengers traveled alone; large families were rare.
- Full breakdown available in [`Titanic_Key_Insight.pdf`](Titanic_Key_Insight.pdf).

---

## 📂 Structure

```
titanic-analysis-dashboard/
├── titanic-analysis-dashboard.ipynb   # Data cleaning, imputation, KPI analysis
├── cleaned_titanic.csv                # Cleaned dataset
├── app.py                             # Interactive Streamlit dashboard
├── requirements.txt                   # Dependencies
├── Titanic_Key_Insight.pdf            # Key insights summary
├── .streamlit/
│   └── config.toml                    # Dashboard theme
└── images/
    ├── dashboard1.png
    ├── dashboard2.png
    └── dashboard3.png
```

---

## ✍️ Author

**Merve**
