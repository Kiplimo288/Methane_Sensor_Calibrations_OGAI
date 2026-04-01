
import pandas as pd
import matplotlib.pyplot as plt

# Path to the updated CSV file
file_path = r"C:\Users\kiplimo\Desktop\METEC\Projects\SENSOR DATA APR'24\Analysis\MOx and Aeris\ML\ML-UPGRADE\ML_DATA_UPDATED.csv"

# Read the CSV file
df = pd.read_csv(file_path)

# Convert Timestamp column to datetime format
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Create a figure and subplots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 10), sharex=True)

# Plot CH4 (ppm) vs Timestamp
ax1.scatter(df['Timestamp'], df['CH4 (ppm)'], color='white', edgecolors='blue', marker='o')
ax1.set_ylabel('CH4 (ppm)')
ax1.set_title('Timeseries Scatter Plots')
ax1.grid(True)

# Plot TGS2600Concentration A vs Timestamp
ax2.scatter(df['Timestamp'], df['TGS2600Concentration A'], color='white', edgecolors='green', marker='o')
ax2.set_ylabel('TGS2600Concentration A')
ax2.grid(True)

# Plot TGS2611Concentration A vs Timestamp
ax3.scatter(df['Timestamp'], df['TGS2611Concentration A'], color='white', edgecolors='red', marker='o')
ax3.set_ylabel('TGS2611Concentration A')
ax3.set_xlabel('Timestamp')
ax3.grid(True)

# Adjust layout and display the plot
plt.tight_layout()
plt.show()
