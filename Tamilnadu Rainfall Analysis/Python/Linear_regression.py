from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Read dataset
project_folder = Path(__file__).resolve().parent.parent
data = pd.read_csv(project_folder / "Data" / "Tamilnadu.csv")

# Linear regression
result = linregress(data["YEAR"], data["ANNUAL"])

print("LINEAR REGRESSION RESULTS")
print("-------------------------")
print(f"Slope       : {result.slope:.4f} mm/year")
print(f"Intercept   : {result.intercept:.2f}")
print(f"R-value     : {result.rvalue:.4f}")
print(f"R²          : {result.rvalue**2:.4f}")
print(f"P-value     : {result.pvalue:.4f}")

# Plot
plt.figure(figsize=(12,6))

plt.plot(data["YEAR"], data["ANNUAL"],
         label="Annual Rainfall",
         linewidth=1.5)

plt.plot(
    data["YEAR"],
    result.intercept + result.slope * data["YEAR"],
    color="red",
    linestyle="--",
    linewidth=2,
    label="Linear Trend"
)

plt.title("Annual Rainfall Trend (1901–2017)")
plt.xlabel("Year")
plt.ylabel("Annual Rainfall (mm)")
plt.grid(True)
plt.legend()

plt.savefig(
    project_folder / "Figures" / "Linear_Regression.png",
    dpi=300
)

plt.show()