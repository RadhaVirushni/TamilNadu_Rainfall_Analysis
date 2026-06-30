import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the dataset
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

project_folder = Path(__file__).resolve().parent.parent

data = pd.read_csv(project_folder / "Data" / "Tamilnadu.csv")

# Create figure
plt.figure(figsize=(12,6))

# Plot annual rainfall
plt.plot(data["YEAR"], data["ANNUAL"], label="Annual Rainfall", linewidth=1.5)

# Calculate linear trend
z = np.polyfit(data["YEAR"], data["ANNUAL"], 1)
p = np.poly1d(z)

# Plot trend line
plt.plot(data["YEAR"], p(data["YEAR"]),
         color="red",
         linestyle="--",
         linewidth=2,
         label="Linear Trend")

# Labels
plt.title("Annual Rainfall in Tamil Nadu (1901–2017)")
plt.xlabel("Year")
plt.ylabel("Annual Rainfall (mm)")

# Legend
plt.legend()

# Grid
plt.grid(True)

# Save figure
plt.savefig(project_folder / "Figures" / "Annual_Rainfall_with_Trend.png", dpi=300)

# Show figure
plt.show()