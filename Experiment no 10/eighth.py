# Program to draw box-and-whisker plot
import matplotlib.pyplot as plt
import numpy as np

# Generate data for multiple groups
np.random.seed(42)
data_group1 = np.random.normal(50, 10, 100)
data_group2 = np.random.normal(60, 12, 100)
data_group3 = np.random.normal(45, 8, 100)
data_group4 = np.random.normal(70, 15, 100)

data = [data_group1, data_group2, data_group3, data_group4]
labels = ['Group A', 'Group B', 'Group C', 'Group D']

# Create box plot
plt.figure(figsize=(10, 6))
bp = plt.boxplot(data, labels=labels, patch_artist=True, notch=True)

# Customize colors
colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightyellow']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Add labels and title
plt.title("Box-and-Whisker Plot by Group", fontsize=14, fontweight='bold')
plt.xlabel("Groups", fontsize=12)
plt.ylabel("Values", fontsize=12)
plt.grid(axis='y', alpha=0.3)

# Show plot
plt.show()