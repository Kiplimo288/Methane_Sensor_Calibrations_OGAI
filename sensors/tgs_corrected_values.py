import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Path to the updated CSV file
file_path = r"C:\Users\kiplimo\Desktop\METEC\Projects\SENSOR DATA APR'24\Analysis\MOx and Aeris\ML\ML-UPGRADE\ML_DATA_UPDATED.csv"

# Read the CSV file
df = pd.read_csv(file_path)

# Use qcut to divide the CH4 (ppm) column into 6 equal ranges
df['CH4_Range'] = pd.qcut(df['CH4 (ppm)'], q=6, labels=['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6'])

# Function to plot and fit calibration curve
def plot_calibration_curve(df, x_col, y_col, bin_label):
    x = df[x_col]
    y = df[y_col]
    
    plt.scatter(x, y, edgecolor='blue', facecolor='none', label='Data points')
    
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
    
    # Plot the line of best fit
    plt.plot(x, y_pred, 'b--', linewidth=2, label='Best fit line')
    
    # Display equation and R-squared value
    equation = f'y = {m:.4f}x + {c:.4f}'
    r_squared_text = f'R^2 = {r_squared:.4f}'
    plt.text(0.65, 0.95, equation, transform=plt.gca().transAxes, fontsize=10, verticalalignment='top', horizontalalignment='right')
    plt.text(0.65, 0.90, r_squared_text, transform=plt.gca().transAxes, fontsize=10, verticalalignment='top', horizontalalignment='right')
    
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f'{y_col} vs {x_col} for {bin_label}')
    plt.legend()
    plt.grid(True)

# Plotting the graphs for TGS2600Corr
fig, axes = plt.subplots(3, 2, figsize=(14, 14))
fig.tight_layout(pad=5.0)

for i, bin_label in enumerate(['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6']):
    df_bin = df[df['CH4_Range'] == bin_label]
    plt.subplot(3, 2, i+1)
    plot_calibration_curve(df_bin, 'TGS2600Corr', 'CH4 (ppm)', bin_label)

plt.suptitle('CH4 (ppm) vs TGS2600Corr by CH4 Range')
plt.show()

# Plotting the graphs for TGS2611Corr
fig, axes = plt.subplots(3, 2, figsize=(14, 14))
fig.tight_layout(pad=5.0)

for i, bin_label in enumerate(['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6']):
    df_bin = df[df['CH4_Range'] == bin_label]
    plt.subplot(3, 2, i+1)
    plot_calibration_curve(df_bin, 'TGS2611Corr', 'CH4 (ppm)', bin_label)

plt.suptitle('CH4 (ppm) vs TGS2611Corr by CH4 Range')
plt.show()
