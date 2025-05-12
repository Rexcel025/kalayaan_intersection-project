import pandas as pd
import matplotlib.pyplot as plt

# Load both datasets: one from base simulation, one from TraCI (adaptive TL) simulation
base_csv = "output/tripinfo_data_old.csv"
traci_csv = "output/tripinfo_data_traci.csv"

# Load CSVs
df_base = pd.read_csv(base_csv)
df_traci = pd.read_csv(traci_csv)

# Remove average summary row if it exists
df_base = df_base[df_base["Trip ID"] != "AVERAGE"]
df_traci = df_traci[df_traci["Trip ID"] != "AVERAGE"]

# Convert relevant columns to numeric
df_base["Waiting Time (s)"] = pd.to_numeric(df_base["Waiting Time (s)"], errors="coerce")
df_traci["Waiting Time (s)"] = pd.to_numeric(df_traci["Waiting Time (s)"], errors="coerce")

df_base["Trip Duration (s)"] = pd.to_numeric(df_base["Trip Duration (s)"], errors="coerce")
df_traci["Trip Duration (s)"] = pd.to_numeric(df_traci["Trip Duration (s)"], errors="coerce")

# Calculate averages
avg_base_wait = df_base["Waiting Time (s)"].mean()
avg_traci_wait = df_traci["Waiting Time (s)"].mean()

avg_base_duration = df_base["Trip Duration (s)"].mean()
avg_traci_duration = df_traci["Trip Duration (s)"].mean()

# Plot comparison
fig, axs = plt.subplots(1, 2, figsize=(12, 5))
axs[0].bar(["Base", "TraCI"], [avg_base_wait, avg_traci_wait], color=["steelblue", "seagreen"])
axs[0].set_title("Average Waiting Time")
axs[0].set_ylabel("Seconds")

axs[1].bar(["Base", "TraCI"], [avg_base_duration, avg_traci_duration], color=["steelblue", "seagreen"])
axs[1].set_title("Average Trip Duration")
axs[1].set_ylabel("Seconds")

plt.suptitle("Comparison: Base vs Adaptive Traffic Light (TraCI)")
plt.tight_layout()
plt.show()
