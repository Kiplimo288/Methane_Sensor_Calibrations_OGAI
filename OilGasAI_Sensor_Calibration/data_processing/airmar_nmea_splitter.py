import os
import pandas as pd
import re

# Define the file path
file_path = r'C:\Users\kiplimo\Desktop\SABER\Airmar\Preprocessed\timestamp_and_nmea.csv'
output_dir = r'C:\Users\kiplimo\Desktop\SABER\Airmar\Preprocessed'

# Read the CSV file
df = pd.read_csv(file_path)

# Group the data by the 'NMEA_Data' column
grouped = df.groupby('NMEA_Data')

# Function to sanitize the NMEA data values for filenames
def sanitize_filename(value):
    return re.sub(r'[\\/*?:"<>|]', "_", value)

# Iterate over each unique value in 'NMEA_Data' and create a separate file
for nmea_value, group in grouped:
    # Sanitize the NMEA value to create a valid file name
    sanitized_value = sanitize_filename(nmea_value)
    
    # Define the output file name
    output_file = os.path.join(output_dir, f"{sanitized_value}.csv")
    
    # Save the group to a new CSV file
    group.to_csv(output_file, index=False)

print("Files created successfully!")
