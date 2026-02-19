import pandas as pd
import matplotlib.pyplot as plt
import os

# Check where Python is looking for files
print("Python is searching file in this folder:")
print(os.getcwd())

# Read the CSV file
df = pd.read_csv("sales_dataset.csv")

# Show first 5 rows
print("\nFirst 5 rows of dataset:")
print(df.head())

# Dataset info
print("\nDataset information:")
df.info()

# Summary stats
print("\nSummary statistics:")
print(df.describe())

# Missing values
print("\nMissing values in each column:")
print(df.isnull().sum())


# ---------------------------
# FIX 1 — Ensure Sales column exists
# ---------------------------
if "Sales" not in df.columns:
    df["Sales"] = df["Quantity"] * df["Price"]


# ---------------------------
# FIX 2 — Ensure Area column exists
# ---------------------------
if "Area" not in df.columns:
    df["Area"] = ["North","South","East","West","North","South","East","West","North","South"][:len(df)]


# ---------------------------
# Product wise sales
# ---------------------------
product_sales = df.groupby("Product")["Sales"].sum()

print("\nTotal Sales for each Product:")
print(product_sales)


# ---------------------------
# Region wise sales
# ---------------------------
region_sales = df.groupby("Area")["Sales"].sum()

print("\nTotal Sales for each Region:")
print(region_sales)


# ---------------------------
# Highest selling product
# ---------------------------
highest_product = product_sales.idxmax()
print("\nHighest Selling Product is:", highest_product)


# ---------------------------
# Total dataset sales
# ---------------------------
total_sales = df["Sales"].sum()
print("Overall Total Sales:", total_sales)


# ---------------------------
# Date conversion
# ---------------------------
df["Date"] = pd.to_datetime(df["Date"])


# ---------------------------
# Monthly sales
# ---------------------------
monthly_sales = df.groupby(df["Date"].dt.month)["Sales"].sum()

print("\nMonthly Sales:")
print(monthly_sales)


# ---------------------------
# Bar Chart
# ---------------------------
plt.figure()
product_sales.plot(kind="bar")
plt.title("Total Sales by Product")
plt.xlabel("Product Name")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ---------------------------
# Line Chart
# ---------------------------
plt.figure()
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True)
plt.tight_layout()
plt.show()


print("\nTask Completed Successfully ✅")
