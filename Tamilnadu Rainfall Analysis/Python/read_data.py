from pathlib import Path
import pandas as pd

print("Current working directory:")
print(Path.cwd())

print("\nLocation of this script:")
print(Path(__file__).resolve())

project_folder = Path(__file__).resolve().parent.parent

print("\nProject folder:")
print(project_folder)

csv_file = project_folder / "Data" / "Tamilnadu.csv"

print("\nCSV path:")
print(csv_file)

print("\nDoes the file exist?")
print(csv_file.exists())

data = pd.read_csv(csv_file)

print("\nSuccess! Dataset loaded.")
print(data.head())