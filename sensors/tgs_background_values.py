
import pandas as pd

# Path to the CSV file
file_path = r"C:\Users\kiplimo\Desktop\METEC\Projects\SENSOR DATA APR'24\Analysis\MOx and Aeris\ML\ML-UPGRADE\ML_DATA.csv"

# Read the CSV file
df = pd.read_csv(file_path)

# Filter the DataFrame for the specified CH4 (ppm) range
filtered_df = df[(df['CH4 (ppm)'] >= 1.90) & (df['CH4 (ppm)'] <= 1.999)]

# Calculate the average values
TGS2600Background = filtered_df['TGS2600'].mean()
TGS2611Background = filtered_df['TGS2611'].mean()

# Print the results
print(f"TGS2600Background: {TGS2600Background}")
print(f"TGS2611Background: {TGS2611Background}")
