import pandas as pd
import matplotlib.pyplot as plt

# File path to your CSV file
file_path = r"C:\Users\kiplimo\Desktop\METEC\Projects\SENSOR DATA APR'24\Analysis\MOx and Aeris\ML\ML-UPGRADE\TGS2600&2611_Trained_Predicted.csv"

# Read data from CSV
data = pd.read_csv(file_path)

# Filter out humidity values above 100
filtered_data = data[data['DHT22_Humidity'] <= 100]

# Define the zoom factor for TGS2600 and TGS2611
zoom_factor = 2

# Plot TGS2600, TGS2611, DHT22 Temperature, and DHT22 Humidity in subplots
fig, axs = plt.subplots(4, 1, figsize=(10, 15), sharex=True)

# TGS2600 plot
axs[0].scatter(filtered_data.index, filtered_data['TGS2600'], color='none', edgecolor='blue', alpha=0.7, linewidth=0.5)
axs[0].set_ylabel('TGS2600')
axs[0].set_title('TGS2600')
# Zoom in
tgs2600_min = filtered_data['TGS2600'].min()
tgs2600_max = filtered_data['TGS2600'].max()
axs[0].set_ylim(tgs2600_min - (tgs2600_max - tgs2600_min) / zoom_factor, tgs2600_max + (tgs2600_max - tgs2600_min) / zoom_factor)

# TGS2611 plot
axs[1].scatter(filtered_data.index, filtered_data['TGS2611'], color='none', edgecolor='green', alpha=0.7, linewidth=0.5)
axs[1].set_ylabel('TGS2611')
axs[1].set_title('TGS2611')
# Zoom in
tgs2611_min = filtered_data['TGS2611'].min()
tgs2611_max = filtered_data['TGS2611'].max()
axs[1].set_ylim(tgs2611_min - (tgs2611_max - tgs2611_min) / zoom_factor, tgs2611_max + (tgs2611_max - tgs2611_min) / zoom_factor)

# DHT22 Temperature plot
axs[2].scatter(filtered_data.index, filtered_data['DHT22_Temperature'], color='none', edgecolor='red', alpha=0.7, linewidth=0.5)
axs[2].set_ylabel('DHT22 Temperature')
axs[2].set_title('DHT22 Temperature')

# DHT22 Humidity plot
axs[3].scatter(filtered_data.index, filtered_data['DHT22_Humidity'], color='none', edgecolor='purple', alpha=0.7, linewidth=0.5)
axs[3].set_ylabel('DHT22 Humidity')
axs[3].set_title('DHT22 Humidity')

# Set common labels
plt.xlabel('Index')
plt.tight_layout()
plt.show()
