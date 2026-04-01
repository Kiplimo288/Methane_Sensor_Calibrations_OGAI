
import pandas as pd

# File path
file_path = r"C:\Users\kiplimo\Desktop\METEC\Projects\SENSOR DATA APR'24\Analysis\MOx and Aeris\ML\ML-UPGRADE\TGS2600&2611_Trained_Predicted.csv"

# Read the CSV file
print("Reading the CSV file...")
df = pd.read_csv(file_path)
print("File read successfully!")

# Exclude the 'Timestamp' column from calculations
columns_to_analyze = df.columns[df.columns != 'Timestamp']

# Print column names
print("Columns to be analyzed:")
print(columns_to_analyze.tolist())

# Calculate the averages, max, and min for each column
print("\nCalculating statistics...")
averages = df[columns_to_analyze].mean()
max_values = df[columns_to_analyze].max()
min_values = df[columns_to_analyze].min()

# Print the results
print("\nAverages:\n", averages)
print("\nMaximum values:\n", max_values)
print("\nMinimum values:\n", min_values)
