from pathlib import Path
import pandas as pd

# Read the dataset
project_folder = Path(__file__).resolve().parent.parent
data = pd.read_csv(project_folder / "Data" / "Tamilnadu.csv")

# Wettest year
wettest = data.loc[data["ANNUAL"].idxmax()]

# Driest year
driest = data.loc[data["ANNUAL"].idxmin()]

print("WETTEST YEAR")
print("----------------")
print(f"Year : {int(wettest['YEAR'])}")
print(f"Annual Rainfall : {wettest['ANNUAL']} mm")

print()

print("DRIEST YEAR")
print("----------------")
print(f"Year : {int(driest['YEAR'])}")
print(f"Annual Rainfall : {driest['ANNUAL']} mm")