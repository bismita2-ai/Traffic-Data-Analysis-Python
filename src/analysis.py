import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import load_workbook

# Read the traffic data
traffic_data = pd.read_csv("data/traffic_counts.csv")

# Create Total Traffic column
traffic_data["Total"] = (
    traffic_data["Cars"]
    + traffic_data["Bikes"]
    + traffic_data["Buses"]
    + traffic_data["Trucks"]
)

# Save the updated data to Excel with headings
with pd.ExcelWriter("traffic_analysis.xlsx", engine="openpyxl") as writer:
    traffic_data.to_excel(
        writer,
        sheet_name="Traffic Analysis",
        startrow=2,
        index=False
    )

# Add headings to Excel file
workbook = load_workbook("traffic_analysis.xlsx")
sheet = workbook["Traffic Analysis"]

sheet["A1"] = "Hourly Traffic Volume Analysis"
sheet["A2"] = "Traffic Data Analysis Using Python"

workbook.save("traffic_analysis.xlsx")

print("Excel file created successfully!")

# Find the peak hour
peak_hour = traffic_data.loc[traffic_data["Total"].idxmax()]

print("Traffic Statistics")
print("--------------------------")
print(f"Peak Hour: {peak_hour['Time']}")
print(f"Maximum Traffic: {traffic_data['Total'].max()} vehicles")
print(f"Minimum Traffic: {traffic_data['Total'].min()} vehicles")
print(f"Average Traffic: {traffic_data['Total'].mean():.2f} vehicles")


# Create graph
plt.figure(figsize=(10, 5))

# Plot traffic volume
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

# Add value label on peak point
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

# Save graph
plt.savefig("images/traffic_volume.png")

# Display graph
plt.show()
