import pandas as pd
import matplotlib.pyplot as plt

# Load the data
file_path = r"C:\Users\kiplimo\Desktop\METEC\Projects\SENSOR DATA APR'24\Analysis\MOx and Aeris\ML\ML-UPGRADE\Review\Final_Predictions.csv"
data = pd.read_csv(file_path)

# Assuming there's a timestamp column named 'Timestamp'
if 'Timestamp' in data.columns:
    data['Timestamp'] = pd.to_datetime(data['Timestamp'])
else:
    data['Timestamp'] = pd.date_range(start='2024-01-01', periods=len(data), freq='T')  # Example fallback

# Set the 'Timestamp' column as the index
timestamps = data['Timestamp']

# Create a figure with two subplots (one for zoomed-in view and one for full view)
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(10, 10), gridspec_kw={'height_ratios': [1, 1]})

# Top Panel: Zoomed-in view for the focus area (0 to 40 ppm)
ax1.scatter(timestamps[data['CH4 (ppm)'] >= 0], data['CH4 (ppm)'][data['CH4 (ppm)'] >= 0], 
            marker='o', color='#1f77b4', edgecolor='black', linewidth=0.6)

ax1.scatter(timestamps[data['TGS2600_Predicted_CH4'] >= 0], data['TGS2600_Predicted_CH4'][data['TGS2600_Predicted_CH4'] >= 0], 
            marker='s', color='#ff7f0e', edgecolor='black', linewidth=0.6)

ax1.scatter(timestamps[data['TGS2611_Predicted_CH4'] >= 0], data['TGS2611_Predicted_CH4'][data['TGS2611_Predicted_CH4'] >= 0], 
            marker='d', color='#2ca02c', edgecolor='black', linewidth=0.6)

# Set y-axis limits for the zoomed-in view
ax1.set_ylim(0, 40)
ax1.axhspan(0, 40, facecolor='yellow', alpha=0.1)  # Highlight focus area
ax1.set_title('Zoomed-In View of Aeris CH\u2084 Measurements and TGS Predictions (0-40 ppm)')
ax1.set_ylabel('CH\u2084 (ppm)')
ax1.grid(True)

# Bottom Panel: Full view of the dataset
ax2.scatter(timestamps[data['CH4 (ppm)'] >= 0], data['CH4 (ppm)'][data['CH4 (ppm)'] >= 0], 
            marker='o', color='#1f77b4', label='Aeris CH\u2084 (ppm)', edgecolor='black', linewidth=0.6)

ax2.scatter(timestamps[data['TGS2600_Predicted_CH4'] >= 0], data['TGS2600_Predicted_CH4'][data['TGS2600_Predicted_CH4'] >= 0], 
            marker='s', color='#ff7f0e', label='TGS2600 CH\u2084 (ppm)', edgecolor='black', linewidth=0.6)

ax2.scatter(timestamps[data['TGS2611_Predicted_CH4'] >= 0], data['TGS2611_Predicted_CH4'][data['TGS2611_Predicted_CH4'] >= 0], 
            marker='d', color='#2ca02c', label='TGS2611 CH\u2084 (ppm)', edgecolor='black', linewidth=0.6)

# Set y-axis limits for the full view
max_value = data[['CH4 (ppm)', 'TGS2600_Predicted_CH4', 'TGS2611_Predicted_CH4']].max().max()
ax2.set_ylim(-1, max_value * 1.1)  # Adding a buffer of 10% above the max value

# Add titles and labels for the bottom panel
ax2.set_title('Full View of Aeris CH\u2084 Measurements and TGS Predictions')
ax2.set_xlabel('Time')
ax2.set_ylabel('CH\u2084 (ppm)')
ax2.legend()  # Only keep the legend here
ax2.grid(True)

plt.tight_layout()
plt.show()
