import pandas as pd

# File path
file_path = r"C:\Users\kiplimo\Desktop\METEC\Projects\SENSOR DATA APR'24\Analysis\MOx and Aeris\ML\ML-UPGRADE\TGS2600&2611_Trained_Predicted.csv"

# Read the CSV file
df = pd.read_csv(file_path)

# Calculate the averages, max, and min for each column
averages = df.mean()
max_values = df.max()
min_values = df.min()

# Print the results
print("Averages:\n", averages)
print("\nMaximum values:\n", max_values)
print("\nMinimum values:\n", min_values)
