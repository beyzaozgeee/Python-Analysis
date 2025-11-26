import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv("sales_data.csv")

# Basic info
print("Head of data:")
print(df.head())

# Summary statistics
print("\nSummary statistics:")
print(df.describe())

# Monthly sales chart
monthly = df.groupby("Month")["Revenue"].sum()

plt.figure(figsize=(8, 4))
monthly.plot(kind="line")
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("monthly_revenue.png")
print("\nChart saved as monthly_revenue.png")
