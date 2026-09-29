import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------
# 1. Load Dataset
# -----------------------------------

df = pd.read_csv("books_dataset.csv")

print("Dataset loaded successfully!")

# -----------------------------------
# 2. Basic Information
# -----------------------------------

print("\n===== DATASET INFORMATION =====")

print("Rows and Columns:", df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nFirst 5 Records:")
print(df.head())

print("\nData Types:")
print(df.dtypes)

# -----------------------------------
# 3. Missing Values
# -----------------------------------

print("\n===== MISSING VALUES =====")

print(df.isnull().sum())

# -----------------------------------
# 4. Duplicate Records
# -----------------------------------

print("\n===== DUPLICATE RECORDS =====")

print("Duplicate rows:", df.duplicated().sum())

# -----------------------------------
# 5. Convert Price to Numeric
# -----------------------------------

df["Price"] = pd.to_numeric(
    df["Price"],
    errors="coerce"
)

# -----------------------------------
# 6. Statistical Summary
# -----------------------------------

print("\n===== STATISTICAL SUMMARY =====")

print(df.describe())

# -----------------------------------
# 7. Price Analysis
# -----------------------------------

print("\n===== PRICE ANALYSIS =====")

print("Average Price:", round(df["Price"].mean(), 2))
print("Median Price:", round(df["Price"].median(), 2))
print("Minimum Price:", df["Price"].min())
print("Maximum Price:", df["Price"].max())
print("Standard Deviation:",
      round(df["Price"].std(), 2))

# -----------------------------------
# 8. Cheapest Book
# -----------------------------------

print("\n===== CHEAPEST BOOK =====")

cheapest = df.loc[df["Price"].idxmin()]

print(cheapest)

# -----------------------------------
# 9. Most Expensive Book
# -----------------------------------

print("\n===== MOST EXPENSIVE BOOK =====")

expensive = df.loc[df["Price"].idxmax()]

print(expensive)

# -----------------------------------
# 10. Rating Analysis
# -----------------------------------

print("\n===== RATING ANALYSIS =====")

print(df["Rating"].value_counts().sort_index())

print(
    "Most common rating:",
    df["Rating"].mode()[0]
)

# -----------------------------------
# 11. Availability Analysis
# -----------------------------------

print("\n===== AVAILABILITY =====")

print(df["Availability"].value_counts())

# -----------------------------------
# 12. Availability Percentage
# -----------------------------------

print("\n===== AVAILABILITY PERCENTAGE =====")

availability_percentage = (
    df["Availability"]
    .value_counts(normalize=True) * 100
)

print(availability_percentage.round(2))

# -----------------------------------
# 13. Average Price by Rating
# -----------------------------------

print("\n===== AVERAGE PRICE BY RATING =====")

avg_price = df.groupby("Rating")["Price"].mean()

print(avg_price.round(2))

# -----------------------------------
# 14. Correlation
# -----------------------------------

print("\n===== CORRELATION =====")

correlation = df["Price"].corr(df["Rating"])

print(
    "Price-Rating Correlation:",
    round(correlation, 3)
)

# -----------------------------------
# 15. Outlier Detection
# -----------------------------------

print("\n===== OUTLIER DETECTION =====")

Q1 = df["Price"].quantile(0.25)
Q3 = df["Price"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[
    (df["Price"] < lower) |
    (df["Price"] > upper)
]

print("Lower Limit:", round(lower, 2))
print("Upper Limit:", round(upper, 2))
print("Number of Outliers:", len(outliers))

# -----------------------------------
# 16. Histogram
# -----------------------------------

plt.figure(figsize=(8, 5))

plt.hist(df["Price"], bins=20)

plt.title("Distribution of Book Prices")
plt.xlabel("Price")
plt.ylabel("Number of Books")

plt.tight_layout()
plt.show()

# -----------------------------------
# 17. Rating Bar Chart
# -----------------------------------

rating_counts = (
    df["Rating"]
    .value_counts()
    .sort_index()
)

plt.figure(figsize=(8, 5))

plt.bar(
    rating_counts.index,
    rating_counts.values
)

plt.title("Number of Books by Rating")
plt.xlabel("Rating")
plt.ylabel("Number of Books")

plt.tight_layout()
plt.show()

# -----------------------------------
# 18. Availability Pie Chart
# -----------------------------------

availability = (
    df["Availability"]
    .value_counts()
)

plt.figure(figsize=(6, 6))

plt.pie(
    availability.values,
    labels=availability.index,
    autopct="%1.1f%%"
)

plt.title("Book Availability")

plt.show()

# -----------------------------------
# 19. Price vs Rating
# -----------------------------------

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Rating"],
    df["Price"]
)

plt.title("Book Price vs Rating")
plt.xlabel("Rating")
plt.ylabel("Price")

plt.tight_layout()
plt.show()

# -----------------------------------
# 20. Box Plot
# -----------------------------------

plt.figure(figsize=(8, 5))

plt.boxplot(df["Price"])

plt.title("Book Price Distribution")
plt.ylabel("Price")

plt.tight_layout()
plt.show()

print("\n===== ANALYSIS COMPLETED =====")