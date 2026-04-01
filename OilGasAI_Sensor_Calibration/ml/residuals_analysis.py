import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
file_path = r"C:\Users\kiplimo\Desktop\METEC\Projects\SENSOR DATA APR'24\Analysis\MOx and Aeris\ML\ML-UPGRADE\TGS2600&2611_Trained_Predicted.csv"

data = pd.read_csv(file_path)

# Extract actual and predicted values
actual_ch4 = data['CH4 (ppm)']
predicted_ch4_tgs2600 = data['TGS2600CH4_RandomForest']
predicted_ch4_tgs2611 = data['TGS2611CH4_RandomForest']

# Assuming there's a timestamp column named 'Timestamp'
# If there isn't, you can use the index or any other appropriate time-related column
if 'Timestamp' in data.columns:
    timestamps = pd.to_datetime(data['Timestamp'])
else:
    timestamps = data.index

# Plot the scatter plot
plt.figure(figsize=(12, 8))
plt.scatter(timestamps, actual_ch4, marker='o', label='Actual CH4 (ppm)', color='black', s=50)
plt.scatter(timestamps, predicted_ch4_tgs2600, marker='s', label='Predicted CH4 (ppm) - TGS2600', color='blue', s=50)
plt.scatter(timestamps, predicted_ch4_tgs2611, marker='d', label='Predicted CH4 (ppm) - TGS2611', color='green', s=50)

plt.title('Actual vs Predicted CH4 Values Over Time')
plt.xlabel('Time')
plt.ylabel('CH4 (ppm)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
