from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Read dataset
project_folder = Path(__file__).resolve().parent.parent
data = pd.read_csv(project_folder / "Data" / "Tamilnadu.csv")

# Long-term mean rainfall
mean_rainfall = data["ANNUAL"].mean()

# Calculate anomaly
data["Anomaly"] = data["ANNUAL"] - mean_rainfall

print(data[["YEAR","ANNUAL","Anomaly"]].head())

# Save to Excel
data[["YEAR","ANNUAL","Anomaly"]].to_excel(
    project_folder / "Excel" / "Rainfall_Anomaly.xlsx",
    index=False
)

# Plot
plt.figure(figsize=(14,6))

colors = ["blue" if x >= 0 else "red" for x in data["Anomaly"]]

plt.bar(
    data["YEAR"],
    data["Anomaly"],
    color=colors
)

plt.axhline(0,color="black")

plt.title("Annual Rainfall Anomalies (1901–2017)")
plt.xlabel("Year")
plt.ylabel("Rainfall Anomaly (mm)")

plt.grid(axis="y")

plt.savefig(
    project_folder/"Figures"/"Rainfall_Anomaly.png",
    dpi=300
)

plt.show()