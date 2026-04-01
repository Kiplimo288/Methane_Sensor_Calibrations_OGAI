import pandas as pd

# Function to convert degrees and minutes to decimal degrees
def convert_to_decimal_degrees(degrees_minutes, direction):
    # Check if the input is a string
    degrees_minutes_str = str(degrees_minutes)
    
    # Handle cases where the value might be in an unexpected format
    if not degrees_minutes_str or '.' not in degrees_minutes_str:
        return None
    
    # Convert degrees and minutes
    try:
        degrees = int(degrees_minutes_str[:2])
        minutes = float(degrees_minutes_str[2:])
    except ValueError:
        return None
    
    decimal_degrees = degrees + (minutes / 60.0)
    
    # Adjust for direction
    if direction in ['S', 'W']:
        decimal_degrees = -decimal_degrees
    
    return decimal_degrees

# Path to the CSV file
file_path = 'C:\\Users\\kiplimo\\Desktop\\SABER\\Airmar\\Preprocessed\\$GPGGA.csv'

# Try reading the CSV file with different encodings
try:
    df = pd.read_csv(file_path, encoding='utf-8')
except UnicodeDecodeError:
    try:
        df = pd.read_csv(file_path, encoding='ISO-8859-1')
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, encoding='utf-16', errors='replace')

# Ensure that latitude and longitude columns are treated as strings
df[' Latitude.'] = df[' Latitude.'].astype(str)
df[' Longitude.'] = df[' Longitude.'].astype(str)

# Convert Latitude and Longitude
df['Latitude_decimal'] = df.apply(lambda row: convert_to_decimal_degrees(row[' Latitude.'], row[' Latitude direction (N/S).']), axis=1)
df['Longitude_decimal'] = df.apply(lambda row: convert_to_decimal_degrees(row[' Longitude.'], row[' Longitude direction (E/W).']), axis=1)

# Save the modified DataFrame to a new CSV file
output_file_path = 'C:\\Users\\kiplimo\\Desktop\\SABER\\Airmar\\Preprocessed\\$GPGGA_converted.csv'
df.to_csv(output_file_path, index=False)

print(f"Converted
