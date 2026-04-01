
import pandas as pd

# Path to the updated CSV file
file_path = r"C:\Users\kiplimo\Desktop\METEC\Projects\SENSOR DATA APR'24\Analysis\MOx and Aeris\ML\ML-UPGRADE\ML_DATA_UPDATED.csv"

# Read the CSV file
df = pd.read_csv(file_path)

# Check the columns in your DataFrame to find the exact names of the columns to delete
print(df.columns)

# Assuming the last two columns are 'TGS2600Concentration A' and 'TGS2611Concentration A', you can delete them
columns_to_delete = ['TGS2600Concentration A', 'TGS2611Concentration A']

# Delete the columns from the DataFrame
df.drop(columns=columns_to_delete, inplace=True)

# Print the updated DataFrame to verify the columns are deleted
print(df.head())

# Write back to CSV with updated columns
df.to_csv(file_path, index=False)

# Optionally, you can print or save the entire DataFrame without these columns
# print(df)
# df.to_csv(file_path, index=False)
