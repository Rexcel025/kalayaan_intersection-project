import pandas as pd
import matplotlib.pyplot as plt
import os

# Paths to the output CSVs
base_csv = os.path.join("output", "tripinfo_data_old.csv")
traci_csv = os.path.join("output", "tripinfo_data_traci.csv")

# Load both datasets
df_base = pd.read_csv(base_csv)
df_traci = pd.read_csv(traci_csv)

# Extract average values from the summary row (where Trip ID == 'AVERAGE')
avg_base = df_base[df_base["Trip ID"] == "AVERAGE"].iloc[0]
avg_traci = df_traci[df_traci["Trip ID"] == "AVERAGE"].iloc[0]

# Get congestion %
base_congestion = avg_base["Congestion %"]
traci_congestion = avg_traci["Congestion %"]

# Calculate improvement
difference = base_congestion - traci_congestion
improvement = (difference / base_congestion) * 100 if base_congestion > 0 else 0

# Print summary
print(f"📊 Base Congestion: {base_congestion:.2f}%")
print(f"⚙️ TraCI Congestion: {traci_congestion:.2f}%")
print(f"📉 Congestion Improvement: {improvement:.2f}%")

# Plot comparison
plt.figure(figsize=(8, 6))
plt.bar(["Base", "Adaptive (TraCI)"], [base_congestion, traci_congestion], color=["red", "green"])
plt.title("Congestion Comparison")
plt.ylabel("Congestion (%)")

# Annotate values
plt.text(0, base_congestion + 0.5, f"{base_congestion:.2f}%", ha='center')
plt.text(1, traci_congestion + 0.5, f"{traci_congestion:.2f}%", ha='center')

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
