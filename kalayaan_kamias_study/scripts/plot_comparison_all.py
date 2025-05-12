import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV files (simulated base and traci-controlled outputs)
base_path = "output/tripinfo_data_old.csv"
traci_path = "output/tripinfo_data_traci.csv"

base_df = pd.read_csv(base_path)
traci_df = pd.read_csv(traci_path)

# Drop the summary row (last row with 'AVERAGE') if present
base_df_clean = base_df[base_df["Trip ID"] != "AVERAGE"].copy()
traci_df_clean = traci_df[traci_df["Trip ID"] != "AVERAGE"].copy()

# Compute mean statistics
base_avg = {
    "Waiting Time": base_df_clean["Waiting Time (s)"].mean(),
    "Trip Duration": base_df_clean["Trip Duration (s)"].mean(),
    "Congestion %": (base_df_clean["Waiting Time (s)"].mean() / base_df_clean["Trip Duration (s)"].mean()) * 100
}

traci_avg = {
    "Waiting Time": traci_df_clean["Waiting Time (s)"].mean(),
    "Trip Duration": traci_df_clean["Trip Duration (s)"].mean(),
    "Congestion %": (traci_df_clean["Waiting Time (s)"].mean() / traci_df_clean["Trip Duration (s)"].mean()) * 100
}

# Compute difference %
diff_percent = {
    "Waiting Time": ((base_avg["Waiting Time"] - traci_avg["Waiting Time"]) / base_avg["Waiting Time"]) * 100,
    "Trip Duration": ((base_avg["Trip Duration"] - traci_avg["Trip Duration"]) / base_avg["Trip Duration"]) * 100,
    "Congestion %": ((base_avg["Congestion %"] - traci_avg["Congestion %"]) / base_avg["Congestion %"]) * 100
}

# Prepare DataFrame for plotting
comparison_df = pd.DataFrame({
    "Metric": ["Average Waiting Time", "Average Trip Duration", "Congestion %"],
    "Base Simulation": [base_avg["Waiting Time"], base_avg["Trip Duration"], base_avg["Congestion %"]],
    "Adaptive (TraCI)": [traci_avg["Waiting Time"], traci_avg["Trip Duration"], traci_avg["Congestion %"]],
    "Difference (%)": [diff_percent["Waiting Time"], diff_percent["Trip Duration"], diff_percent["Congestion %"]]
})

# Melt for plotting
melted_df = comparison_df.melt(id_vars="Metric", value_vars=["Base Simulation", "Adaptive (TraCI)"], var_name="Simulation", value_name="Value")

# Plot
plt.figure(figsize=(10, 6))
sns.barplot(data=melted_df, x="Metric", y="Value", hue="Simulation")
plt.title("Comparison of Base vs Adaptive (TraCI) Traffic Light Control")
plt.ylabel("Value (seconds or %)")
plt.xticks(rotation=15)
plt.tight_layout()
plt.grid(axis='y')

plt.show(), comparison_df.round(2)
