# Program to draw histogram
import matplotlib.pyplot as plt
import numpy as np

# Generate random data
np.random.seed(42)
data = np.random.normal(loc=70, scale=15, size=1000)  # Mean=70, Std=15

# Calculate statistics
mean_val = np.mean(data)
median_val = np.median(data)

# Create histogram
plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, color='skyblue', edgecolor='black', alpha=0.7)

# Add labels and title
plt.title("Distribution of Exam Scores", fontsize=14, fontweight='bold')
plt.xlabel("Scores", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.grid(axis='y', alpha=0.3)

# Add mean and median lines
plt.axvline(mean_val, color='red', linestyle='dashed', linewidth=2,
            label=f'Mean: {mean_val:.1f}')
plt.axvline(median_val, color='green', linestyle='dashed', linewidth=2,
            label=f'Median: {median_val:.1f}')

# Show legend
plt.legend()

# Adjust layout and display
plt.tight_layout()
plt.show()