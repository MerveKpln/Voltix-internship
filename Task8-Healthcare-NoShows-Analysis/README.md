# 📊 Healthcare Appointment No-Shows: Excel Dashboard

An interactive Excel dashboard that turns raw medical appointment data into clear insights about **who misses appointments, and what is linked to it**.

![Dashboard](images/Dashboard.png)

---

## 📁 Dataset

**File:** `healthcare_noshows.csv`
**Size:** 106,987 appointment records originally, **106,982** after cleaning
**Source:** Public medical appointment no-show data from Brazil (Vitória)

Each row is one appointment. The goal is to understand which factors are associated with a patient **not showing up**.

| Column | Description |
|---|---|
| `PatientId` | Unique patient identifier |
| `AppointmentID` | Unique appointment identifier |
| `Gender` | F = Female, M = Male |
| `ScheduledDay` | Date the appointment was booked |
| `AppointmentDay` | Date of the appointment |
| `Age` | Patient age |
| `Neighbourhood` | Neighbourhood of the clinic |
| `Scholarship` | Enrolled in the Bolsa Família welfare programme (TRUE/FALSE) |
| `Hipertension` | Patient has hypertension (TRUE/FALSE) |
| `Diabetes` | Patient has diabetes (TRUE/FALSE) |
| `Alcoholism` | Alcoholism recorded (TRUE/FALSE) |
| `Handcap` | Handicap status |
| `SMS_received` | Reminder SMS sent (TRUE/FALSE) |
| `Showed_up` | **Target:** patient attended (TRUE) or not (FALSE) |
| `Date.diff` | Days between booking and appointment |

---

## 🛠️ Tools

- **Microsoft Excel**
- Excel Tables (named table as the single source)
- Formulas: `IF`, `TEXT`, `COUNTA`, `COUNTBLANK`, `COUNTIF`, `SUM`, `AVERAGE`, `ROUND`
- PivotTables and PivotCharts
- Slicers for interactive filtering

---

## 🧹 Cleaning

| Check | Result | Action |
|---|---|---|
| Blank cells in all columns | None found | None needed |
| `Age` below 0 | None | None needed |
| `Age` above 100 | 7 rows, plausible real ages | Kept |
| `Date.diff` below 0 | 5 rows (4 with a 1-day gap, 1 with a 6-day gap) | Removed, since the correct dates could not be confirmed |
| `Gender` values | Only F and M | None needed |

The checks are documented in the `Data Quality Check` sheet. Final dataset: **106,982 rows**.

**Helper columns added to the table:**

| Column | Logic |
|---|---|
| `AgeGroup` | Child (≤12), Teen (13–19), Adult (20–59), Senior (60+) |
| `Weekday` | Day name from `AppointmentDay` |
| `WaitCategory` | Same Day, Short Wait (1–7 Days), Long Wait (>7 Days) |
| `NoShow` | 1 if the patient did not show up, 0 otherwise, so its average equals the no-show rate |
| `SMS_Status` | "SMS Sent" or "No SMS" for readable charts |

---

## 📊 Dashboard

**KPI cards**

| KPI | Value |
|---|---|
| Total Appointments | 106,982 |
| Show-up Rate | 79.74% |
| No-Show Rate | 20.26% |
| No-Show Count | 21,676 |
| Avg Wait Days | 10.2 |

**Charts**

1. No-Show Rate by Age Group
2. No-Show Rate by Wait Time
3. No-Show Rate by SMS Reminder
4. No-Show Rate by Weekday

**Slicers:** SMS Status, Gender, Age Group, Scholarship

**Design:** warm cream background (`#FAF2ED`) with orange accents (`#E65100`) and dark brown text (`#2C221E`).

---

## 💡 Insights

![Key Insights](images/KeyInsight.png)

1. **Overall:** about 1 in 5 appointments is missed (20.26%).
2. **Waiting time is the strongest factor:** no-show rises from 4.7% (same day) to 24.1% (1–7 days) and 32.2% (more than 7 days). Bookings made more than 7 days ahead are 36% of appointments but 57% of all no-shows.
3. **Age matters:** teens miss most often (26.0%), seniors least (15.3%). Adults produce the most missed visits in absolute numbers because they are the largest group.
4. **Weekday has a weak effect:** Monday to Friday stay between 19.5% and 21.3%. Saturday (23.1%) has only 39 appointments, too few to conclude anything.
5. **SMS looks worse than it is:** the raw gap (27.7% with SMS vs 16.7% without) is misleading, because no SMS was sent for same-day appointments. Excluding them, both groups are roughly similar, so the SMS effect cannot be measured cleanly from this data.

### Recommendations and Limitations

![Recommendations and Limitations](images/RecommendationsAndLimitations.png)

- Focus reminders or confirmation calls on appointments booked more than 7 days ahead.
- Shorten lead times where possible, or keep a waitlist to refill missed slots.
- Test targeted reminders for teenagers.
- Run a controlled SMS test on comparable appointments.
- Findings are associations, not proven causes, and SMS and waiting time overlap.

---

## 📂 Structure

```
📁 Healthcare-NoShows-Dashboard
│
├── 📁 images
│   ├── Dashboard.png
│   ├── KeyInsight.png
│   └── RecommendationsAndLimitations.png
│
├── healthcare_noshows _DASHBOARD.xlsb
├── healthcare_noshows _DASHBOARD.xlsx
├── healthcare_noshows.csv
└── README.md
```

**Workbook sheets:** main data table, `Data Quality Check`, `Pivots`, `Dashboard`.

---

## ✍️ Author

**Merve**
Internship project: Excel Dashboard task

[Add your LinkedIn / GitHub / Kaggle link here]