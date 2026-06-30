import pandas as pd

# Read the dataset
data = pd.read_csv("../Data/Tamilnadu.csv")

# Display basic information
print("Dataset Shape:", data.shape)
print("\nColumn Names:")
print(data.columns)

print("\nFirst 5 Rows:")
print(data.head())

print("\nMissing Values:")
print(data.isnull().sum())