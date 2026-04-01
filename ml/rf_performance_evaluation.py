import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# File path to your CSV file containing actual and predicted labels
file_path = r"C:\Users\kiplimo\Desktop\METEC\Projects\SENSOR DATA APR'24\Analysis\MOx and Aeris\ML\ML-UPGRADE\TGS2600&2611_Trained_Predicted.csv"

# Read data from CSV
data = pd.read_csv(file_path)

# Assuming your data structure has columns for actual and predicted labels
actual_labels = data['Actual_Labels']  # Replace 'Actual_Labels' with your actual column name
predicted_labels = data['Predicted_Labels']  # Replace 'Predicted_Labels' with your predicted column name

# Function to calculate Cohen's Kappa
def cohen_kappa(actual, predicted):
    N = len(actual)
    unique_labels = np.unique(np.concatenate((actual, predicted)))
    confusion_matrix = np.zeros((len(unique_labels), len(unique_labels)))

    for i in range(N):
        confusion_matrix[actual[i], predicted[i]] += 1

    observed_agreement = np.trace(confusion_matrix) / N
    expected_agreement = np.sum(np.sum(confusion_matrix, axis=0) * np.sum(confusion_matrix, axis=1)) / (N * N)
    
    kappa = (observed_agreement - expected_agreement) / (1 - expected_agreement)
    
    return kappa, confusion_matrix

# Calculate Cohen's Kappa
kappa, cm = cohen_kappa(actual_labels, predicted_labels)

# Plot confusion matrix
plt.figure(figsize=(8, 6))
plt.imshow(cm, interpolation='nearest', cmap='Blues')
plt.title('Confusion Matrix')
plt.colorbar()

# Define labels based on unique values in actual_labels
tick_marks = np.arange(len(np.unique(actual_labels)))
plt.xticks(tick_marks, sorted(np.unique(actual_labels)))
plt.yticks(tick_marks, sorted(np.unique(actual_labels)))

# Add annotations for each cell in the confusion matrix
for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        plt.text(j, i, format(cm[i, j], 'd'),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > cm.max() / 2 else "black")

plt.ylabel('Actual Labels')
plt.xlabel('Predicted Labels')
plt.title(f'Confusion Matrix\nCohen\'s Kappa: {kappa:.4f}')
plt.tight_layout()
plt.show()

print(f"Cohen's Kappa: {kappa:.4f}")
