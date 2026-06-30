import pandas as pd

# Read the dataset
data = pd.read_csv("../Data/Tamilnadu.csv")

# Descriptive statistics for Annual Rainfall
annual = data["ANNUAL"]

print("DESCRIPTIVE STATISTICS FOR ANNUAL RAINFALL")
print("------------------------------------------")
print(f"Number of Observations : {annual.count()}")
print(f"Mean                   : {annual.mean():.2f}")
print(f"Median                 : {annual.median():.2f}")
print(f"Minimum                : {annual.min():.2f}")
print(f"Maximum                : {annual.max():.2f}")
print(f"Range                  : {annual.max() - annual.min():.2f}")
print(f"Standard Deviation     : {annual.std():.2f}")
print(f"Variance               : {annual.var():.2f}")
print(f"Coefficient of Variation (%) : {(annual.std()/annual.mean())*100:.2f}")