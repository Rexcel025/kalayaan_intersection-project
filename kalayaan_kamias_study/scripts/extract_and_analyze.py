import os
import xml.etree.ElementTree as ET
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def extract_readable_tripinfo(tripinfo_path):
    tree = ET.parse(tripinfo_path)
    root = tree.getroot()

    trips = []
    for trip in root.findall("tripinfo"):
        try:
            trips.append({
                "Trip ID": trip.get("id"),
                "Depart Time (s)": float(trip.get("depart")),
                "Arrival Time (s)": float(trip.get("arrival")),
                "Trip Duration (s)": float(trip.get("duration")),
                "Route Length (m)": float(trip.get("routeLength")),
                "Waiting Time (s)": float(trip.get("waitingTime")),
                "Vehicle Type": trip.get("vType"),
                "Speed Factor": float(trip.get("speedFactor")),
            })
        except (TypeError, ValueError):
            continue  

    df = pd.DataFrame(trips)
    return df

def summarize_and_transform(df, output_dir):
    # Initial plot (before transformation)
    plt.figure(figsize=(8, 5))
    sns.histplot(df["Trip Duration (s)"], bins=20, kde=True)
    plt.title("Trip Duration Distribution")
    plt.xlabel("Trip Duration (s)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "trip_duration_before.png"))
    plt.close()

    # Compute congestion % per trip
    df["Congestion %"] = (df["Waiting Time (s)"] / df["Trip Duration (s)"]) * 100

    # Add summary row
    avg_wait = df["Waiting Time (s)"].mean()
    avg_dur = df["Trip Duration (s)"].mean()
    congestion = (avg_wait / avg_dur) * 100 if avg_dur > 0 else 0

    summary = {
        "Trip ID": "AVERAGE",
        "Depart Time (s)": "",
        "Arrival Time (s)": "",
        "Trip Duration (s)": avg_dur,
        "Route Length (m)": "",
        "Waiting Time (s)": avg_wait,
        "Vehicle Type": "",
        "Speed Factor": "",
        "Congestion %": congestion
    }

    df = pd.concat([df, pd.DataFrame([summary])], ignore_index=True)

    # Plot after transformation
    plt.figure(figsize=(8, 5))
    sns.histplot(df[df["Trip ID"] != "AVERAGE"]["Congestion %"], bins=20, kde=True, color='orange')
    plt.title("Congestion % Distribution")
    plt.xlabel("Congestion %")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "congestion_after.png"))
    plt.close()

    return df

# Set base paths
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
input_dir = os.path.join(base_dir, "input")
output_dir = os.path.join(base_dir, "output")

# Input and output paths
tripinfo_file = os.path.join(input_dir, "tripinfo_traci.xml")
output_csv = os.path.join(output_dir, "tripinfo_data_traci.csv")

# Main execution
if __name__ == "__main__":
    print("🔄 Extracting trip data...")
    df = extract_readable_tripinfo(tripinfo_file)

    if df.empty:
        print("⚠️ No valid trips found.")
    else:
        print(f"✅ Extracted {len(df)} trips.")
        df = summarize_and_transform(df, output_dir)
        df.to_csv(output_csv, index=False)
        print(f"\n✅ Cleaned and transformed dataset saved to: {output_csv}")
        print(f"Plots saved in output/: trip_duration_before.png and congestion_after.png")
