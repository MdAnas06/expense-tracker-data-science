import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page config
st.set_page_config(page_title="Expense Tracker Dashboard", layout="wide")

# Title
st.title("💰 Expense Tracker Dashboard")

# Load data
df = pd.read_csv("data/cleaned_expenses.csv")

# Convert date
df["Date"] = pd.to_datetime(df["Date"])

# Sidebar filters
st.sidebar.header("🔍 Filters")

category_filter = st.sidebar.multiselect(
    "Select Category",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

payment_filter = st.sidebar.multiselect(
    "Select Payment Method",
    options=df["Payment Method"].unique(),
    default=df["Payment Method"].unique()
)

# Apply filters
filtered_df = df[
    (df["Category"].isin(category_filter)) &
    (df["Payment Method"].isin(payment_filter))
]

# -----------------------------
# KPIs
# -----------------------------
total_spending = filtered_df["Amount"].sum()
avg_spending = filtered_df["Amount"].mean()

col1, col2 = st.columns(2)

col1.metric("💰 Total Spending", f"₹{total_spending}")
col2.metric("📊 Average Spending", f"₹{round(avg_spending,2)}")

# -----------------------------
# Category-wise Spending
# -----------------------------
st.subheader("📂 Category-wise Spending")

category_spending = filtered_df.groupby("Category")["Amount"].sum()

fig1, ax1 = plt.subplots()
category_spending.plot(kind='bar', ax=ax1)
st.pyplot(fig1)

# -----------------------------
# Monthly Trend
# -----------------------------
st.subheader("📈 Monthly Spending Trend")

filtered_df["Month"] = filtered_df["Date"].dt.to_period("M")
monthly_spending = filtered_df.groupby("Month")["Amount"].sum()

fig2, ax2 = plt.subplots()
monthly_spending.plot(marker='o', ax=ax2)
st.pyplot(fig2)

# -----------------------------
# Payment Method
# -----------------------------
st.subheader("💳 Payment Method Usage")

fig3, ax3 = plt.subplots()
sns.countplot(x="Payment Method", data=filtered_df, ax=ax3)
st.pyplot(fig3)

# -----------------------------
# Data Table
# -----------------------------
st.subheader("📄 Raw Data")
st.dataframe(filtered_df)