import pandas as pd

# Load the CSV file
file_path = r"C:\Users\kiplimo\Desktop\METEC\Projects\SENSOR DATA APR'24\Analysis\MOx and Aeris\ML\Sensor Raw & Computed data.csv"
data = pd.read_csv(file_path)

# Print column names
print("Column names in the CSV file:")
print(data.columns.tolist())
