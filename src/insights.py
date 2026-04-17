import pandas as pd

# Load data
df = pd.read_csv("data/cleaned_expenses.csv")

# -----------------------------
# Basic Calculations
# -----------------------------
total_spending = df["Amount"].sum()
avg_spending = df["Amount"].mean()

category_spending = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)
monthly_spending = df.groupby("Month")["Amount"].sum()
payment_usage = df["Payment Method"].value_counts()

# -----------------------------
# Generate Insights
# -----------------------------
print("\n📊 -------- INSIGHTS REPORT --------\n")

# Insight 1
print(f"💰 Total spending is ₹{total_spending}, with an average expense of ₹{round(avg_spending,2)} per transaction.\n")

# Insight 2
top_category = category_spending.idxmax()
print(f"📂 The highest spending category is '{top_category}', indicating major expenses are concentrated here.\n")

# Insight 3
lowest_category = category_spending.idxmin()
print(f"📉 The lowest spending category is '{lowest_category}', suggesting minimal allocation.\n")

# Insight 4
top_month = monthly_spending.idxmax()
print(f"📅 The highest spending occurred in {top_month}, indicating a possible seasonal or behavioral trend.\n")

# Insight 5
top_payment = payment_usage.idxmax()
print(f"💳 Most transactions are done using '{top_payment}', showing user preference for this payment mode.\n")

# Insight 6 (Weekend behavior)
df["Day"] = pd.to_datetime(df["Date"]).dt.day_name()
day_spending = df.groupby("Day")["Amount"].sum().sort_values(ascending=False)

top_day = day_spending.idxmax()
print(f"📆 Spending is highest on '{top_day}', suggesting increased expenses on this day.\n")

# Insight 7 (Overspending detection)
if category_spending.max() > (0.4 * total_spending):
    print(f"⚠️ Warning: A large portion of spending is concentrated in '{top_category}', which may indicate overspending.\n")

print("✅ Insight generation completed!")
