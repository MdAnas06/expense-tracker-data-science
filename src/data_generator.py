import pandas as pd
import numpy as np
import os

# Create data folder if not exists
os.makedirs("data", exist_ok=True)

# Set seed for reproducibility
np.random.seed(42)

# Generate random dates (6 months)
dates = pd.date_range(start="2024-01-01", periods=180)

# Categories
categories = ["Food", "Travel", "Rent", "Shopping", "Entertainment", "Bills"]

# Payment methods
payment_methods = ["Cash", "Card", "UPI"]

# Generate synthetic data
num_records = 400

data = pd.DataFrame({
    "Date": np.random.choice(dates, num_records),
    "Category": np.random.choice(categories, num_records),
    "Amount": np.random.randint(100, 5000, num_records),
    "Payment Method": np.random.choice(payment_methods, num_records)
})

# Sort by date (important for analysis later)
data = data.sort_values(by="Date")

# Save dataset
data.to_csv("data/expenses.csv", index=False)

print("✅ Dataset created successfully!")
print(data.head())