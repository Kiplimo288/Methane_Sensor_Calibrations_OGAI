import pandas as pd
import matplotlib.pyplot as plt

# Load the data
file_path = r"C:\Users\kiplimo\Desktop\METEC\Projects\SENSOR DATA APR'24\Analysis\MOx and Aeris\ML\ML-UPGRADE\TGS2600&2611_Trained_Predicted.csv"
data = pd.read_csv(file_path)

# Assuming there's a timestamp column named 'Timestamp'
if 'Timestamp' in data.columns:
    data['Timestamp'] = pd.to_datetime(data['Timestamp'])
else:
    data['Timestamp'] = pd.date_range(start='2024-01-01', periods=len(data), freq='T')  # Example fallback

# Set the 'Timestamp' column as the index
timestamps = data['Timestamp']

# Create a single scatter plot with all three series
plt.figure(figsize=(10, 6))

# Scatter plot for Aeris CH4 (ppm) - Only plot values >= 0, color = distinct, marker = 'o'
plt.scatter(timestamps[data['CH4 (ppm)'] >= 0], data['CH4 (ppm)'][data['CH4 (ppm)'] >= 0], 
            marker='o', color='#1f77b4', label='Aeris CH4 (ppm)', edgecolor='black', linewidth=0.6)

# Scatter plot for TGS2600 Predicted CH4 values - Only plot values >= 0, color = distinct, marker = 's'
plt.scatter(timestamps[data['TGS2600CH4_RandomForest'] >= 0], data['TGS2600CH4_RandomForest'][data['TGS2600CH4_RandomForest'] >= 0], 
            marker='s', color='#ff7f0e', label='TGS2600 CH4 (ppm)', edgecolor='black', linewidth=0.6)

# Scatter plot for TGS2611 Predicted CH4 values - Only plot values >= 0, color = distinct, marker = 'd'
plt.scatter(timestamps[data['TGS2611CH4_RandomForest'] >= 0], data['TGS2611CH4_RandomForest'][data['TGS2611CH4_RandomForest'] >= 0], 
            marker='d', color='#2ca02c', label='TGS2611 CH4 (ppm)', edgecolor='black', linewidth=0.6)

# Set y-axis limits to focus between 0 and 20, with a slight buffer
plt.ylim(-1, 22)

# Add a shaded region between 0 and 20 to highlight the area of interest
plt.axhspan(0, 20, facecolor='yellow', alpha=0.1, label='Focus Area (0-20 ppm)')

# Add titles and labels
plt.title('')
plt.xlabel('Time')
plt.ylabel('CH4 (ppm)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

