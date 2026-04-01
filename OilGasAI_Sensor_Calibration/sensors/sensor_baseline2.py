import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV file (make sure the path is correct)
file_path = r"C:\Users\kiplimo\Desktop\METEC\Projects\SENSOR DATA APR'24\Analysis\MOx and Aeris\ML\ML-UPGRADE\TGS2600&2611_Trained_Predicted.csv"
df = pd.read_csv(file_path)

# Background resistance values (clean air baseline)
baseline_TGS2600 = 29076.8499
baseline_TGS2611 = 4714.29215

# Calculate deviation from baseline for both sensors
df['TGS2600_Deviation'] = df['TGS2600'] - baseline_TGS2600
df['TGS2611_Deviation'] = df['TGS2611'] - baseline_TGS2611

# Extract temperature and humidity
temperature = df['DHT22_Temperature']
humidity = df['DHT22_Humidity']

# Statistical analysis for TGS2600
tgs2600_mean = df['TGS2600_Deviation'].mean()
tgs2600_std = df['TGS2600_Deviation'].std()
tgs2600_max_dev = df['TGS2600_Deviation'].max()
tgs2600_min_dev = df['TGS2600_Deviation'].min()

# Statistical analysis for TGS2611
tgs2611_mean = df['TGS2611_Deviation'].mean()
tgs2611_std = df['TGS2611_Deviation'].std()
tgs2611_max_dev = df['TGS2611_Deviation'].max()
tgs2611_min_dev = df['TGS2611_Deviation'].min()

# Manual Linear Regression (Least Squares Method)
def linear_regression(X, Y):
    X_b = np.c_[np.ones((len(X), 1)), X]  # Add a column of ones for the bias term
    theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(Y)
    return theta_best

# Prepare data for linear regression (temperature and humidity)
X = np.array(df[['DHT22_Temperature', 'DHT22_Humidity']])
y_tgs2600 = np.array(df['TGS2600_Deviation'])
y_tgs2611 = np.array(df['TGS2611_Deviation'])

# Perform linear regression for TGS2600 and TGS2611
theta_tgs2600 = linear_regression(X, y_tgs2600)
theta_tgs2611 = linear_regression(X, y_tgs2611)

# Plotting the deviations vs. time with temperature and humidity
plt.figure(figsize=(14, 8))

# TGS2600 plot
plt.subplot(2, 1, 1)
plt.plot(df['Timestamp'], df['TGS2600_Deviation'], label='TGS2600 Deviation', color='blue')
plt.axhline(0, color='red', linestyle='--', label='Baseline (Clean Air)')
plt.title('TGS2600 Deviation from Baseline with Temperature and Humidity Influence')
plt.xlabel('Timestamp')
plt.ylabel('Deviation (?)')
plt.legend()

# TGS2611 plot
plt.subplot(2, 1, 2)
plt.plot(df['Timestamp'], df['TGS2611_Deviation'], label='TGS2611 Deviation', color='green')
plt.axhline(0, color='red', linestyle='--', label='Baseline (Clean Air)')
plt.title('TGS2611 Deviation from Baseline with Temperature and Humidity Influence')
plt.xlabel('Timestamp')
plt.ylabel('Deviation (?)')
plt.legend()

plt.tight_layout()
plt.show()

# Display statistics and regression coefficients
print("TGS2600 Sensor (Baseline to Air) Stats:")
print(f"Mean Deviation: {tgs2600_mean}")
print(f"Standard Deviation: {tgs2600_std}")
print(f"Max Deviation: {tgs2600_max_dev}")
print(f"Min Deviation: {tgs2600_min_dev}")
print(f"Intercept: {theta_tgs2600[0]}")
print(f"Temperature Coefficient: {theta_tgs2600[1]}")
print(f"Humidity Coefficient: {theta_tgs2600[2]}")

print("\nTGS2611 Sensor (Baseline to Air) Stats:")
print(f"Mean Deviation: {tgs2611_mean}")
print(f"Standard Deviation: {tgs2611_std}")
print(f"Max Deviation: {tgs2611_max_dev}")
print(f"Min Deviation: {tgs2611_min_dev}")
print(f"Intercept: {theta_tgs2611[0]}")
print(f"Temperature Coefficient: {theta_tgs2611[1]}")
print(f"Humidity Coefficient: {theta_tgs2611[2]}")
