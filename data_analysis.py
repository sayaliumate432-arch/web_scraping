import pandas as pd

# Read scraped dataset
df = pd.read_csv("books_dataset.csv")

print("========== BOOK DATASET ==========\n")

# Display dataset
print(df)

# Number of books
print("\nTotal Books:", len(df))

# Convert Price column into numeric value
df["Price Numeric"] = (
    df["Price"]
    .astype(str)
    .str.replace("Â", "", regex=False)
    .str.replace("£", "", regex=False)
    .str.strip()
    .astype(float)
)

# Average price
average_price = df["Price Numeric"].mean()

print("\nAverage Book Price: £", round(average_price, 2))

# Maximum price
maximum_price = df["Price Numeric"].max()

print("Maximum Book Price: £", maximum_price)

# Minimum price
minimum_price = df["Price Numeric"].min()

print("Minimum Book Price: £", minimum_price)

# Rating distribution
print("\n========== RATING DISTRIBUTION ==========")
print(df["Rating"].value_counts())

# Save cleaned dataset
df.to_csv("cleaned_books_dataset.csv", index=False)

print("\n========================================")
print("Analysis completed successfully!")
print("Cleaned dataset saved as:")
print("cleaned_books_dataset.csv")
print("========================================")