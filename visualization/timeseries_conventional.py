import pandas as pd

# Define the path to your CSV file
file_path = r"C:\Users\kiplimo\Desktop\METEC\Projects\SENSOR DATA APR'24\Analysis\MOx and Aeris\ML\ML-UPGRADE\ML_DATA__CONV.csv"

# Read the CSV file into a pandas DataFrame
data = pd.read_csv(file_path)

# Find the highest values in each column
highest_values = data.max()

# Print the highest values for each column
print("Highest values in each column:")
print(highest_values)
