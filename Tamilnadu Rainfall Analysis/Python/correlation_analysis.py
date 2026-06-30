from pathlib import Path
import pandas as pd

# Project folder
project_folder = Path(__file__).resolve().parent.parent

# Read dataset
data = pd.read_csv(project_folder / "Data" / "Tamilnadu.csv")

# Monthly columns
months = [
    "JAN","FEB","MAR","APR","MAY","JUN",
    "JUL","AUG","SEP","OCT","NOV","DEC"
]

# Calculate correlation with annual rainfall
correlation = []

for month in months:
    r = data[month].corr(data["ANNUAL"])
    correlation.append([month, r])

# Create DataFrame
corr_df = pd.DataFrame(
    correlation,
    columns=["Month", "Correlation with Annual Rainfall"]
)

# Display
print("\nCORRELATION ANALYSIS")
print("----------------------------")
print(corr_df)

# Save to Excel
corr_df.to_excel(
    project_folder / "Excel" / "Correlation_Analysis.xlsx",
    index=False
)

print("\nCorrelation analysis saved successfully!")
