import pandas as pd
import matplotlib.pyplot as plt

# Define the file path
file_path = r"C:\Users\kiplimo\Desktop\METEC\Projects\SENSOR DATA APR'24\Analysis\MOx and Aeris\ML\ML-UPGRADE\ML_DATA_UPDATED2.csv"

# Load your CSV file
data = pd.read_csv(file_path)

# Convert the 'Timestamp' column to datetime
data['Timestamp'] = pd.to_datetime(data['Timestamp'])

# Create subplots
fig, axs = plt.subplots(3, 1, figsize=(15, 10), sharex=True)

# Plot CH4 (ppm)
axs[0].scatter(data['Timestamp'], data['CH4 (ppm)'], label='CH4 (ppm)', color='b', s=10)
axs[0].set_ylabel('CH4 (ppm)')
axs[0].legend()
axs[0].grid(True)

# Plot TGS2600ppmConv
axs[1].scatter(data['Timestamp'], data['TGS2600ppmConv'], label='TGS2600ppmConv', color='r', s=10)
axs[1].set_ylabel('TGS2600ppmConv')
axs[1].legend()
axs[1].grid(True)

# Plot TGS2611ppmConv
axs[2].scatter(data['Timestamp'], data['TGS2611ppmConv'], label='TGS2611ppmConv', color='g', s=10)
axs[2].set_ylabel('TGS2611ppmConv')
axs[2].legend()
axs[2].grid(True)

# Set common labels
axs[2].set_xlabel('Timestamp')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Set the main title
plt.suptitle('Time Series Scatter Plots of CH4 (ppm), TGS2600ppmConv, and TGS2611ppmConv')

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.96])

# Show the plot
plt.show()
