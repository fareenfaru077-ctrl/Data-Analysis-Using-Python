#  Sales Data Analysis using Python

##  Project Description

This project analyzes a sales dataset using **Python, Pandas, and Matplotlib**.
It performs data inspection, cleaning, analysis, and visualization to extract meaningful business insights such as:

* Product-wise sales
* Region-wise sales
* Monthly trends
* Highest selling product
* Overall sales

---

## Technologies Used

* Python 3
* Pandas
* Matplotlib

---

## Dataset Required

The script expects a CSV file named:

```
sales_dataset.csv
```

The dataset should contain at least these columns:

```
Product, Quantity, Price, Date
```

If the dataset does not contain **Sales** or **Area** columns, the script automatically generates them.

---

## Features

✔ Displays dataset preview
✔ Shows dataset info & statistics
✔ Detects missing values
✔ Auto-creates missing columns
✔ Calculates product sales
✔ Calculates region sales
✔ Finds highest selling product
✔ Calculates monthly sales
✔ Generates charts

---

##  How to Run

### Step 1 — Install dependencies

```bash
pip install pandas matplotlib
```

### Step 2 — Place dataset

Put `sales_dataset.csv` in the same folder as the script.

### Step 3 — Run script

```bash
python filename.py
```

---

## Output Generated

The program prints:

* Dataset summary
* Product sales report
* Region sales report
* Highest selling product
* Monthly sales report

And displays:

*  Bar chart → Product Sales
*  Line chart → Monthly Sales Trend

---

## Logic Highlights

* Uses `groupby()` for aggregation
* Uses `datetime conversion` for monthly analysis
* Uses conditional checks to avoid column errors
* Uses visualization for trend analysis

---

## Future Improvements

Possible enhancements:

* Add yearly trend analysis
* Export report to Excel/CSV
* Add dashboard visualization
* GUI interface

---

##  Final Status

✔ Fully automated
✔ Error-handled
✔ Beginner friendly
✔ Production-safe logic


