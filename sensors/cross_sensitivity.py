

import pandas as pd

# Load the data
file_path = r"C:\Users\kiplimo\Desktop\METEC\Projects\SENSOR DATA APR'24\Analysis\MOx and Aeris\ML\ML-UPGRADE\Review\Final_Predictions.csv"

data = pd.read_csv(file_path)

# Define background values
background_values = {
    'TGS2600': 29076.8499,
    'TGS2611': 4714.29215,
    'CH4(ppm)': 2.2  # Average of 2.1 to 2.3
}

# Define temperature and humidity thresholds for filtering
temp_threshold = 0.5  # Adjust this threshold as needed
humidity_threshold = 5  # Adjust this threshold as needed

# Function to find similar conditions in initial and final stages
def find_similar_conditions(data, condition='initial'):
    if condition == 'initial':
        # Filter for initial conditions (first 10% of data)
        subset = data.iloc[:int(len(data) * 0.1)]
    else:
        # Filter for final conditions (last 10% of data)
        subset = data.iloc[int(len(data) * 0.9):]

    # Get average temperature and humidity
    avg_temp = subset['DHT22_Temperature'].mean()
    avg_humidity = subset['DHT22_Humidity'].mean()
    
    # Filter the full dataset for similar conditions
    filtered_data = data[
        (data['DHT22_Temperature'].between(avg_temp - temp_threshold, avg_temp + temp_threshold)) &
        (data['DHT22_Humidity'].between(avg_humidity - humidity_threshold, avg_humidity + humidity_threshold))
    ]
    
    return filtered_data

# Get initial and final condition datasets
initial_data = find_similar_conditions(data, condition='initial')
final_data = find_similar_conditions(data, condition='final')

# Calculate drift for each sensor
initial_avg = initial_data[['TGS2600', 'TGS2611']].mean()
final_avg = final_data[['TGS2600', 'TGS2611']].mean()

drift = {
    'TGS2600': final_avg['TGS2600'] - initial_avg['TGS2600'],
    'TGS2611': final_avg['TGS2611'] - initial_avg['TGS2611'],
}

# Calculate cross-sensitivity index
cross_sensitivity_index = {
    'TGS2600': drift['TGS2600'] / (background_values['TGS2600'] - background_values['CH4(ppm)']),
    'TGS2611': drift['TGS2611'] / (background_values['TGS2611'] - background_values['CH4(ppm)']),
}

# Display the results
print("Drift from Background Values:")
print("TGS2600 Drift:", drift['TGS2600'])
print("TGS2611 Drift:", drift['TGS2611'])
print("\nCross-Sensitivity Index:")
print("TGS2600 CSI:", cross_sensitivity_index['TGS2600'])
print("TGS2611 CSI:", cross_sensitivity_index['TGS2611'])
