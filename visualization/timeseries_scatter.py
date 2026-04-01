import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
file_path = r"C:\Users\kiplimo\Desktop\METEC\Projects\SENSOR DATA APR'24\Analysis\MOx and Aeris\ML\ML-UPGRADE\TGS2600&2611_Trained_Predicted.csv"

data = pd.read_csv(file_path)

# Assuming there's a timestamp column named 'Timestamp'
# If there isn't, you can use the index or any other appropriate time-related column
if 'Timestamp' in data.columns:
    timestamps = pd.to_datetime(data['Timestamp'])
else:
    timestamps = data.index

# Create subplots for each data series
fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, figsize=(8, 16))

# Scatter plot for CH4 (ppm)
ax1.scatter(timestamps, data['CH4 (ppm)'], marker='o', color='black', label='Aeris CH4 (ppm)', facecolor='none', edgecolor='green')
ax1.set_title('Aeris')
ax1.set_xlabel('')
ax1.set_ylabel('Aeris CH4 (ppm)')
ax1.legend()
ax1.grid(True)

# Scatter plot for Predicted CH4 values from TGS2600
ax2.scatter(timestamps, data['TGS2600CH4_RandomForest'], marker='s', color='blue', label='Predicted CH4 (ppm) - TGS2600', facecolor='none', edgecolor='blue')
ax2.set_title('TGS2600')
ax2.set_xlabel('')
ax2.set_ylabel('TGS2600 CH4 (ppm)')
ax2.legend()
ax2.grid(True)

# Scatter plot for Predicted CH4 values from TGS2611
ax3.scatter(timestamps, data['TGS2611CH4_RandomForest'], marker='d', color='green', label='Predicted CH4 (ppm) - TGS2611', facecolor='none', edgecolor='red')
ax3.set_title('TGS2611 ')
ax3.set_xlabel('')
ax3.set_ylabel('TGS2611 CH4 (ppm)')
ax3.legend()
ax3.grid(True)

plt.tight_layout()
plt.show()
