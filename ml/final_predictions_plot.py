import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data
file_path = r"C:\Users\kiplimo\Desktop\METEC\Projects\SENSOR DATA APR'24\Analysis\MOx and Aeris\ML\ML-UPGRADE\Review\Final_Predictions.csv"
data = pd.read_csv(file_path)

# Function to calculate R-squared
def calculate_r_squared(y, y_pred):
    ss_res = np.sum((y - y_pred) ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    return 1 - (ss_res / ss_tot)

# Plot 1: CH4 (ppm) vs TGS2600Corr with line of best fit
plt.figure(figsize=(8, 6))
plt.scatter(data['TGS2600Corr'], data['CH4 (ppm)'], color='blue', label='Data Points')

# Line of best fit
m1, b1 = np.polyfit(data['TGS2600Corr'], data['CH4 (ppm)'], 1)
line1 = m1 * data['TGS2600Corr'] + b1
plt.plot(data['TGS2600Corr'], line1, linestyle=':', color='red', linewidth=2, label='Line of Best Fit')

# Calculate and display R-squared
r2_1 = calculate_r_squared(data['CH4 (ppm)'], line1)
plt.legend(loc="upper right")  # Changed to upper right
plt.text(0.95, 0.85, f"$R^2 = {r2_1:.4f}$", transform=plt.gca().transAxes, 
         fontsize=12, verticalalignment='top', horizontalalignment='right')

# Labels and title
plt.xlabel("TGS2600Corr")
plt.ylabel("CH\u2084 (ppm)")
plt.title("")
plt.show()

# Plot 2: CH4 (ppm) vs TGS2611Corr with line of best fit
plt.figure(figsize=(8, 6))
plt.scatter(data['TGS2611Corr'], data['CH4 (ppm)'], color='blue', label='Data Points')

# Line of best fit
m2, b2 = np.polyfit(data['TGS2611Corr'], data['CH4 (ppm)'], 1)
line2 = m2 * data['TGS2611Corr'] + b2
plt.plot(data['TGS2611Corr'], line2, linestyle=':', color='red', linewidth=2, label='Line of Best Fit')

# Calculate and display R-squared
r2_2 = calculate_r_squared(data['CH4 (ppm)'], line2)
plt.legend(loc="upper right")  # Changed to upper right
plt.text(0.95, 0.85, f"$R^2 = {r2_2:.4f}$", transform=plt.gca().transAxes, 
         fontsize=12, verticalalignment='top', horizontalalignment='right')

# Labels and title
plt.xlabel("TGS2611Corr")
plt.ylabel("CH\u2084 (ppm)")
plt.title("")
plt.show()
