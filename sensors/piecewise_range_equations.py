import pandas as pd

# Define the path to your CSV file
file_path = r"C:\Users\kiplimo\Desktop\METEC\Projects\SENSOR DATA APR'24\Analysis\MOx and Aeris\ML\ML-UPGRADE\ML_DATA_UPDATED2.csv"

# Read the CSV file
data = pd.read_csv(file_path)

# Define the equations and ranges for TGS2600
ranges_TGS2600 = [
    (-0.69, 17.85),
    (17.85, 36.39),
    (36.39, 54.92),
    (54.92, 73.46),
    (73.46, 91.99),
    (91.99, 110.53),
    (110.53, 129.07),
    (129.07, 147.60)
]
coeff_TGS2600 = [
    (0.2383, 1.935),
    (-1.2115, 25.1833),
    (-0.2868, 43.9224),
    (0.8606, 52.2032),
    (1.5845, 69.6627),
    (14.9584, 66.6627),
    (10.6062, 89.5655),
    (-14.9997, 100.3139)
]

# Define the equations and ranges for TGS2611
ranges_TGS2611 = [
    (-0.69, 17.85),
    (17.85, 36.39),
    (36.39, 54.92),
    (54.92, 73.46),
    (73.46, 91.99),
    (91.99, 110.53),
    (110.53, 129.07),
    (129.07, 147.60)
]
coeff_TGS2611 = [
    (0.2138, 1.9682),
    (-0.0627, 24.9641),
    (-0.0412, 43.5359),
    (1.2133, 61.6019),
    (3.2076, 67.1471),
    (17.7277, 89.4460),
    (10.3744, 89.5655),
    (-14.2658, 157.97)
]

def apply_equation(value, ranges, coefficients):
    for (lower, upper), (slope, intercept) in zip(ranges, coefficients):
        if lower <= value < upper:
            return slope * value + intercept
    return None

# Apply the equations to create new columns
data['TGS2600_Conv'] = data['CH4 (ppm)'].apply(apply_equation, args=(ranges_TGS2600, coeff_TGS2600))
data['TGS2611_Conv'] = data['CH4 (ppm)'].apply(apply_equation, args=(ranges_TGS2611, coeff_TGS2611))

# Save the updated dataframe to a new CSV file
output_path = r"C:\Users\kiplimo\Desktop\METEC\Projects\SENSOR DATA APR'24\Analysis\MOx and Aeris\ML\ML-UPGRADE\ML_DATA_UPDATED2_CONV.csv"
data.to_csv(output_path, index=False)
