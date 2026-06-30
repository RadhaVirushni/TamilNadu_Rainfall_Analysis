from pathlib import Path
import pandas as pd

# Read dataset
project_folder = Path(__file__).resolve().parent.parent
data = pd.read_csv(project_folder / "Data" / "Tamilnadu.csv")

# Seasonal columns
seasons = ["JF", "MAM", "JJAS", "OND"]

results = []

for season in seasons:
    mean = data[season].mean()
    std = data[season].std()
    cv = (std / mean) * 100

    results.append([season, mean, std, cv])

season_stats = pd.DataFrame(
    results,
    columns=["Season", "Mean (mm)", "Standard Deviation (mm)", "CV (%)"]
)

print(season_stats)

# Save to Excel
season_stats.to_excel(
    project_folder / "Excel" / "Seasonal_Statistics.xlsx",
    index=False
)

print("\nSeasonal statistics saved successfully!")