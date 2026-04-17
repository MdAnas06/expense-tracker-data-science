import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create images folder
os.makedirs("images", exist_ok=True)

# Load data
df = pd.read_csv("data/cleaned_expenses.csv")

# -----------------------------
# 1. Category-wise Spending
# -----------------------------
category_spending = df.groupby("Category")["Amount"].sum()

plt.figure(figsize=(8,8))
category_spending.plot(kind='pie', autopct='%1.1f%%')
plt.title("Category-wise Spending Distribution")
plt.ylabel("")
plt.savefig("images/category_pie.png")
plt.close()

# -----------------------------
# 2. Bar Chart
# -----------------------------
plt.figure(figsize=(10,5))
category_spending.sort_values().plot(kind='bar')
plt.title("Category-wise Spending Comparison")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.savefig("images/category_bar.png")
plt.close()

# -----------------------------
# 3. Monthly Trend
# -----------------------------
df["Month"] = pd.to_datetime(df["Month"].astype(str))
monthly_spending = df.groupby("Month")["Amount"].sum()

plt.figure(figsize=(10,5))
monthly_spending.plot(marker='o')
plt.title("Monthly Spending Trend")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.grid()
plt.savefig("images/monthly_trend.png")
plt.close()

# -----------------------------
# 4. Payment Method Usage
# -----------------------------
plt.figure(figsize=(6,4))
sns.countplot(x="Payment Method", data=df)
plt.title("Payment Method Usage")
plt.savefig("images/payment_methods.png")
plt.close()

print("✅ All visualizations created successfully!")