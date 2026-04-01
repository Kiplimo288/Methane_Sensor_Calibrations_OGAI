
import pandas as pd

# Path to the updated CSV file
file_path = r"C:\Users\kiplimo\Desktop\METEC\Projects\SENSOR DATA APR'24\Analysis\MOx and Aeris\ML\ML-UPGRADE\ML_DATA_UPDATED.csv"

# Read the CSV file
df = pd.read_csv(file_path)

# Define equations
def calculate_TGS2600Concentration_A(TGS2600Corr):
    return 0.01721 * TGS2600Corr + 2.0982

def calculate_TGS2611Concentration_A(TGS2611Corr):
    return 0.1926 * TGS2611Corr + 2.0700

# Apply equations to create new columns
df['TGS2600Concentration A'] = df['TGS2600Corr'].apply(calculate_TGS2600Concentration_A)
df['TGS2611Concentration A'] = df['TGS2611Corr'].apply(calculate_TGS2611Concentration_A)

# Print first few rows to verify
print(df.head())

# Write back to CSV with updated columns
df.to_csv(file_path, index=False)

# Optionally, you can print or save the entire DataFrame with these new columns
# print(df)
# df.to_csv(file_path, index=False)
