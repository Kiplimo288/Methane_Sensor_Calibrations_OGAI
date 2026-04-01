import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# Load the CSV file
file_path = r"C:\Users\kiplimo\Desktop\METEC\Projects\SENSOR DATA APR'24\Analysis\MOx and Aeris\ML\ML-UPGRADE\Review\Final_Predictions.csv"
data = pd.read_csv(file_path)

# Define the columns for each histogram
columns = ['CH4 (ppm)', 'TGS2600_Predicted_CH4', 'TGS2611_Predicted_CH4']
titles = ['Measured CH\u2084', 'TGS2600 Predicted CH\u2084', 'TGS2611 Predicted CH\u2084']

# Set up the figure and axes
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Define bin edges for 0.2 ppm increments from 2.0 to 5.0, with an additional bin for >5.0
bin_edges = [i * 0.2 for i in range(10, 26)]
bin_edges.append(float('inf'))  # Adds an upper limit bin for >5.0

# Define bin labels as ranges (e.g., "2.0-2.2") and the last one as ">5.0"
bin_labels = [f"{bin_edges[i]:.1f}-{bin_edges[i + 1]:.1f}" for i in range(len(bin_edges) - 2)]
bin_labels.append(">5.0")

# Create histograms
for i, col in enumerate(columns):
    ax = axes[i]
    # Use pd.cut to categorize data into defined bins and count occurrences
    counts = pd.cut(data[col], bins=bin_edges, labels=bin_labels, right=False).value_counts().reindex(bin_labels).fillna(0)
    
    ax.bar(bin_labels, counts, color="steelblue", edgecolor="black")
    ax.set_title(titles[i])
    ax.set_xlabel('CH\u2084 (ppm)')
    ax.set_ylabel('Frequency')
    ax.set_xticklabels(bin_labels, rotation=90)  # Set labels vertically
    
    # Format the y-axis with comma-separated values
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, pos: f'{int(x):,}'))

# Adjust layout and show the plot
plt.tight_layout()
plt.show()
