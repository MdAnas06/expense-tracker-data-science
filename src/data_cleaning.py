import pandas as pd

# -----------------------------
# STEP 1: Load Data
# -----------------------------
df = pd.read_csv("data/expenses.csv")

print("🔹 Raw Data Preview:")
print(df.head())

# -----------------------------
# STEP 2: Check Data Info
# -----------------------------
print("\n🔹 Data Info:")
print(df.info())

# -----------------------------
# STEP 3: Check Missing Values
# -----------------------------
print("\n🔹 Missing Values:")
print(df.isnull().sum())

# -----------------------------
# STEP 4: Fix Data Types
# -----------------------------
df["Date"] = pd.to_datetime(df["Date"])

# -----------------------------
# STEP 5: Remove Duplicates
# -----------------------------
df = df.drop_duplicates()

# -----------------------------
# STEP 6: Feature Engineering
# -----------------------------
df["Month"] = df["Date"].dt.to_period("M")
df["Day"] = df["Date"].dt.day_name()

# -----------------------------
# STEP 7: Basic Cleaning Checks
# -----------------------------
# Remove negative or zero amounts (if any)
df = df[df["Amount"] > 0]

# -----------------------------
# STEP 8: Save Clean Data
# -----------------------------
df.to_csv("data/cleaned_expenses.csv", index=False)

print("\n✅ Data cleaned successfully!")
print("\n🔹 Cleaned Data Preview:")
print(df.head())