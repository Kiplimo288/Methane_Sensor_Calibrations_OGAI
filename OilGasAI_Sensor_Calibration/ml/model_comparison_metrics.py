import pandas as pd
import numpy as np

# Load the data
file_path = r"C:\Users\kiplimo\Desktop\METEC\Projects\SENSOR DATA APR'24\Analysis\MOx and Aeris\ML\ML-UPGRADE\TGS2600&2611_Trained_Predicted.csv"

data = pd.read_csv(file_path)

# Filtered data for TGS2600 and TGS2611 between specified ranges
filtered_data_tgs2600_r2 = data[(data['TGS2600CH4_RandomForest'] >= 1.85) & (data['TGS2600CH4_RandomForest'] <= 2)]
filtered_data_tgs2600_acc_1_85_5_85 = data[(data['TGS2600CH4_RandomForest'] >= 1.85) & (data['TGS2600CH4_RandomForest'] <= 5.85)]
filtered_data_tgs2600_rmse_2_7 = data[(data['TGS2600CH4_RandomForest'] >= 2) & (data['TGS2600CH4_RandomForest'] <= 7)]
filtered_data_tgs2611_acc_2_9 = data[(data['TGS2611CH4_RandomForest'] >= 2) & (data['TGS2611CH4_RandomForest'] <= 9)]
filtered_data_tgs2611_acc_2_500 = data[(data['TGS2611CH4_RandomForest'] >= 2) & (data['TGS2611CH4_RandomForest'] <= 500)]

# Function to compute R-squared
def calculate_r_squared(actual, predicted):
    y_mean = np.mean(actual)
    ss_tot = np.sum((actual - y_mean)**2)
    ss_res = np.sum((actual - predicted)**2)
    r2 = 1 - (ss_res / ss_tot)
    return r2

# Function to compute accuracy (plus or minus)
def calculate_accuracy(actual, predicted):
    accuracy = np.mean(np.abs(actual - predicted))
    return accuracy

# Function to compute RMSE
def calculate_rmse(actual, predicted):
    rmse = np.sqrt(np.mean((actual - predicted)**2))
    return rmse

# Compute metrics for TGS2600
r2_tgs2600 = calculate_r_squared(filtered_data_tgs2600_r2['CH4 (ppm)'], filtered_data_tgs2600_r2['TGS2600CH4_RandomForest'])
accuracy_tgs2600_1_85_5_85 = calculate_accuracy(filtered_data_tgs2600_acc_1_85_5_85['CH4 (ppm)'], filtered_data_tgs2600_acc_1_85_5_85['TGS2600CH4_RandomForest'])
rmse_tgs2600_2_7 = calculate_rmse(filtered_data_tgs2600_rmse_2_7['CH4 (ppm)'], filtered_data_tgs2600_rmse_2_7['TGS2600CH4_RandomForest'])

# Compute metrics for TGS2611
accuracy_tgs2611_2_9 = calculate_accuracy(filtered_data_tgs2611_acc_2_9['CH4 (ppm)'], filtered_data_tgs2611_acc_2_9['TGS2611CH4_RandomForest'])
accuracy_tgs2611_2_500 = calculate_accuracy(filtered_data_tgs2611_acc_2_500['CH4 (ppm)'], filtered_data_tgs2611_acc_2_500['TGS2611CH4_RandomForest'])

# Print results
print(f"TGS2600 Metrics:")
print(f"R-squared for TGS2600 between 1.85 to 2 ppm: {r2_tgs2600}")
print(f"Accuracy (plus or minus) of TGS2600 between 1.85 to 5.85 ppm: {accuracy_tgs2600_1_85_5_85}")
print(f"RMSE of TGS2600 between 2 and 7 ppm: {rmse_tgs2600_2_7}")
print()
print(f"TGS2611 Metrics:")
print(f"Accuracy (plus or minus) of TGS2611 between 2 and 9 ppm: {accuracy_tgs2611_2_9}")
print(f"Accuracy (plus or minus) of TGS2611 between 2 and 500 ppm: {accuracy_tgs2611_2_500}")
