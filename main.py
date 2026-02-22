import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("All libraries imported successfully!")

# Load dataset
df = pd.read_csv("data/sales_data.csv")

# Show first rows
print("\nFirst 5 rows:")
print(df.head())

# Show column names
print("\nColumns:")
print(df.columns)

# Dataset info
print("\nDataset Info:")
print(df.info())

# Convert date column
df["Date"] = pd.to_datetime(df["Date"])

# Ensure Sales is numeric
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Summary statistics
print("\nSummary stats:")
print(df.describe())