import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file (make sure the path is correct)
file_path = r"C:\Users\kiplimo\Desktop\METEC\Projects\SENSOR DATA APR'24\Analysis\MOx and Aeris\ML\ML-UPGRADE\TGS2600&2611_Trained_Predicted.csv"
df = pd.read_csv(file_path)

# Background resistance values (clean air baseline)
baseline_TGS2600 = 29076.8499
baseline_TGS2611 = 4714.29215

# Calculate deviation from baseline for both sensors
df['TGS2600_Deviation'] = df['TGS2600'] - baseline_TGS2600
df['TGS2611_Deviation'] = df['TGS2611'] - baseline_TGS2611

# Calculate statistics for TGS2600
tgs2600_mean = df['TGS2600_Deviation'].mean()
tgs2600_std = df['TGS2600_Deviation'].std()
tgs2600_max_dev = df['TGS2600_Deviation'].max()
tgs2600_min_dev = df['TGS2600_Deviation'].min()

# Calculate statistics for TGS2611
tgs2611_mean = df['TGS2611_Deviation'].mean()
tgs2611_std = df['TGS2611_Deviation'].std()
tgs2611_max_dev = df['TGS2611_Deviation'].max()
tgs2611_min_dev = df['TGS2611_Deviation'].min()

# Display statistics
print("TGS2600 Sensor (Baseline to Air) Stats:")
print(f"Mean Deviation: {tgs2600_mean}")
print(f"Standard Deviation: {tgs2600_std}")
print(f"Max Deviation: {tgs2600_max_dev}")
print(f"Min Deviation: {tgs2600_min_dev}")

print("\nTGS2611 Sensor (Baseline to Air) Stats:")
print(f"Mean Deviation: {tgs2611_mean}")
print(f"Standard Deviation: {tgs2611_std}")
print(f"Max Deviation: {tgs2611_max_dev}")
print(f"Min Deviation: {tgs2611_min_dev}")

# Plotting the sensor resistances with the baseline
plt.figure(figsize=(12, 6))

# TGS2600 plot
plt.subplot(2, 1, 1)
plt.plot(df['Timestamp'], df['TGS2600'], label='TGS2600 Resistance', color='blue')
plt.axhline(baseline_TGS2600, color='red', linestyle='--', label='Baseline (Clean Air)')
plt.fill_between(df['Timestamp'], baseline_TGS2600 - 0.1 * baseline_TGS2600, baseline_TGS2600 + 0.1 * baseline_TGS2600, 
                 color='red', alpha=0.1, label='±10% Baseline Range')
plt.title('TGS2600 Resistance vs. Baseline (Clean Air)')
plt.xlabel('Timestamp')
plt.ylabel('Resistance (Ω)')
plt.legend()

# TGS2611 plot
plt.subplot(2, 1, 2)
plt.plot(df['Timestamp'], df['TGS2611'], label='TGS2611 Resistance', color='green')
plt.axhline(baseline_TGS2611, color='red', linestyle='--', label='Baseline (Clean Air)')
plt.fill_between(df['Timestamp'], baseline_TGS2611 - 0.1 * baseline_TGS2611, baseline_TGS2611 + 0.1 * baseline_TGS2611, 
                 color='red', alpha=0.1, label='±10% Baseline Range')
plt.title('TGS2611 Resistance vs. Baseline (Clean Air)')
plt.xlabel('Timestamp')
plt.ylabel('Resistance (Ω)')
plt.legend()

plt.tight_layout()
plt.show()