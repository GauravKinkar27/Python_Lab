# Program to draw line plot
import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([2, 4, 6, 8, 10, 12, 14, 16])

# Create line plot
plt.figure(figsize=(8, 5))
plt.plot(x, y, marker='o', linestyle='-', color='b', linewidth=2, markersize=8)

# Add labels and title
plt.title("Line Plot Example", fontsize=14)
plt.xlabel("X-axis (Values)", fontsize=12)
plt.ylabel("Y-axis (Values)", fontsize=12)
plt.grid(True, alpha=0.3)

# Show plot
plt.show()