import pandas as pd
import matplotlib.pyplot as plt

# Read the traffic data
traffic_data = pd.read_csv("data/traffic_counts.csv")

# Create Total Traffic column
traffic_data["Total"] = (
    traffic_data["Cars"]
    + traffic_data["Bikes"]
    + traffic_data["Buses"]
    + traffic_data["Trucks"]
)
# Save the updated data to Excel
traffic_data.to_excel("traffic_analysis.xlsx", index=False)

print("Excel file created successfully!")

## Find the peak hour
peak_hour = traffic_data.loc[traffic_data["Total"].idxmax()]

print("Traffic Statistics")
print("--------------------------")
print(f"Peak Hour: {peak_hour['Time']}")
print(f"Maximum Traffic: {traffic_data['Total'].max()} vehicles")
print(f"Minimum Traffic: {traffic_data['Total'].min()} vehicles")
print(f"Average Traffic: {traffic_data['Total'].mean():.2f} vehicles")

# Create graph
plt.figure(figsize=(10,5))

# Plot traffic line
plt.plot(
    traffic_data["Time"],
    traffic_data["Total"],
    marker="o",
    label="Traffic Volume"
)

# Highlight peak hour
plt.scatter(
    peak_hour["Time"],
    peak_hour["Total"],
    color="red",
    s=120,
    label="Peak Hour"
)

# Add label to the peak point
plt.text(
    peak_hour["Time"],
    peak_hour["Total"] + 10,
    f'{peak_hour["Total"]}',
    ha="center"
)

plt.title("Hourly Traffic Volume")
plt.xlabel("Time")
plt.ylabel("Number of Vehicles")

plt.grid(True)
plt.legend()

plt.savefig("images/traffic_volume.png")

plt.show()