import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Path to the updated CSV file
file_path = r"C:\Users\kiplimo\Desktop\METEC\Projects\SENSOR DATA APR'24\Analysis\MOx and Aeris\ML\ML-UPGRADE\ML_DATA_UPDATED2.csv"

# Read the CSV file
df = pd.read_csv(file_path)

# Function to plot and fit calibration curve
def plot_calibration_curve(x, y, x_label, y_label, title):
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color='white', edgecolors='blue', marker='o', label='Data points')
    
    # Fit linear regression model manually
    x = np.array(x)
    y = np.array(y)
    A = np.vstack([x, np.ones(len(x))]).T
    m, c = np.linalg.lstsq(A, y, rcond=None)[0]
    y_pred = m * x + c
    
    # Calculate R-squared value manually
    ss_res = np.sum((y - y_pred) ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    r_squared = 1 - (ss_res / ss_tot)
    
    # Plot the dotted red line of best fit
    plt.plot(x, y_pred, color='red', linestyle='--', linewidth=2, label='Line of Best Fit')
    
    # Display equation and R-squared value
    equation = f'y = {m:.4f}x + {c:.4f}'
    r_squared_text = f'R^2 = {r_squared:.4f}'
    plt.text(0.05, 0.95, equation, transform=plt.gca().transAxes, fontsize=12, verticalalignment='top')
    plt.text(0.05, 0.90, r_squared_text, transform=plt.gca().transAxes, fontsize=12, verticalalignment='top')
    
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

# Plot 1: CH4 (ppm) against TGS2600Corr
plot_calibration_curve(df['TGS2600Corr'], df['CH4 (ppm)'], 'TGS2600Corr', 'CH4 (ppm)', 'CH4 (ppm) vs TGS2600Corr')

# Plot 2: CH4 (ppm) against TGS2611Corr
plot_calibration_curve(df['TGS2611Corr'], df['CH4 (ppm)'], 'TGS2611Corr', 'CH4 (ppm)', 'CH4 (ppm) vs TGS2611Corr')
