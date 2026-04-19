
import pandas as pd
import matplotlib.pyplot as plt

# Path to the updated CSV file
file_path = r"C:\Users\kiplimo\Desktop\METEC\Projects\SENSOR DATA APR'24\Analysis\MOx and Aeris\ML\ML-UPGRADE\ML_DATA_UPDATED2.csv"

# Read the CSV file
df = pd.read_csv(file_path)

# Convert Timestamp column to datetime format
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Filter data for the given date range
start_date = '2024-03-21'
end_date = '2024-03-22'
mask = (df['Timestamp'] >= start_date) & (df['Timestamp'] <= end_date)
filtered_df = df[mask]

# Create a figure and subplots for TGS2600Corr and TGS2611Corr
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

# Plot TGS2600Corr vs Timestamp
ax1.scatter(filtered_df['Timestamp'], filtered_df['TGS2600Corr'], color='white', edgecolors='green', marker='o', label='TGS2600Corr')
ax1.set_ylabel('TGS2600Corr')
ax1.legend()
ax1.grid(True)

# Plot TGS2611Corr vs Timestamp
ax2.scatter(filtered_df['Timestamp'], filtered_df['TGS2611Corr'], color='white', edgecolors='red', marker='o', label='TGS2611Corr')
ax2.set_ylabel('TGS2611Corr')
ax2.set_xlabel('Timestamp')
ax2.legend()
ax2.grid(True)

# Adjust layout and display the plot
plt.tight_layout()
plt.show()
