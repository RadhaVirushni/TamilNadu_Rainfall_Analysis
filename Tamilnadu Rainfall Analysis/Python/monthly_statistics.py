from pathlib import Path
import pandas as pd

# Read the dataset
project_folder = Path(__file__).resolve().parent.parent
data = pd.read_csv(project_folder / "Data" / "Tamilnadu.csv")

# List of monthly columns
months = ["JAN","FEB","MAR","APR","MAY","JUN",
          "JUL","AUG","SEP","OCT","NOV","DEC"]

results = []

for month in months:
    mean = data[month].mean()
    std = data[month].std()
    cv = (std / mean) * 100

    results.append([month, mean, std, cv])

# Create a new table
monthly_stats = pd.DataFrame(
    results,
    columns=["Month", "Mean (mm)", "Standard Deviation (mm)", "CV (%)"]
)

print(monthly_stats)

# Save to Excel
monthly_stats.to_excel(
    project_folder / "Excel" / "Monthly_Statistics.xlsx",
    index=False
)

print("\nMonthly statistics saved successfully!")