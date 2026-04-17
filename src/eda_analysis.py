import pandas as pd

# -----------------------------
# STEP 1: Load Clean Data
# -----------------------------
df = pd.read_csv("data/cleaned_expenses.csv")

print("🔹 Data Preview:")
print(df.head())

# -----------------------------
# STEP 2: Total Spending
# -----------------------------
total_spending = df["Amount"].sum()
print("\n💰 Total Spending:", total_spending)

# -----------------------------
# STEP 3: Average Spending
# -----------------------------
avg_spending = df["Amount"].mean()
print("\n📊 Average Spending:", round(avg_spending, 2))

# -----------------------------
# STEP 4: Category-wise Spending
# -----------------------------
category_spending = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)

print("\n📂 Category-wise Spending:")
print(category_spending)

# -----------------------------
# STEP 5: Monthly Spending
# -----------------------------
monthly_spending = df.groupby("Month")["Amount"].sum()

print("\n📅 Monthly Spending:")
print(monthly_spending)

# -----------------------------
# STEP 6: Payment Method Analysis
# -----------------------------
payment_usage = df["Payment Method"].value_counts()

print("\n💳 Payment Method Usage:")
print(payment_usage)

# -----------------------------
# STEP 7: Top Spending Day
# -----------------------------
top_day = df.groupby("Day")["Amount"].sum().sort_values(ascending=False)

print("\n📆 Spending by Day:")
print(top_day)

print("\n🔥 Highest Spending Day:", top_day.idxmax())
