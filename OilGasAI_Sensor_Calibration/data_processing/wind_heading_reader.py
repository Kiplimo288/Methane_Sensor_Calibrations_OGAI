
import pandas as pd

# Path to the CSV file
file_path = r"C:\Users\kiplimo\Desktop\METEC\Projects\SENSOR DATA APR'24\Analysis\MOx and Aeris\ML\ML-UPGRADE\ML_DATA.csv"

# Read the CSV file
df = pd.read_csv(file_path)

# Print the column headings
print(df.columns)
