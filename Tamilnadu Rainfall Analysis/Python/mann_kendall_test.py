from pathlib import Path
import pandas as pd
import pymannkendall as mk

# Read dataset
project_folder = Path(__file__).resolve().parent.parent
data = pd.read_csv(project_folder / "Data" / "Tamilnadu.csv")

# Perform Mann-Kendall Test
result = mk.original_test(data["ANNUAL"])

print("MANN-KENDALL TREND TEST")
print("------------------------")
print(f"Trend         : {result.trend}")
print(f"Hypothesis    : {'Reject H0' if result.h else 'Fail to Reject H0'}")
print(f"P-value       : {result.p:.4f}")
print(f"Z-statistic   : {result.z:.4f}")
print(f"Kendall Tau   : {result.Tau:.4f}")
print(f"Sen's Slope   : {result.slope:.4f} mm/year")
print(f"Intercept     : {result.intercept:.2f}")