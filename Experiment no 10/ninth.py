# Program to customize plots with labels and legends
import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) * np.cos(x)

# Create plot with customization
plt.figure(figsize=(12, 6))

# Plot multiple lines
plt.plot(x, y1, 'b-', linewidth=2, label='sin(x)')
plt.plot(x, y2, 'r--', linewidth=2, label='cos(x)')
plt.plot(x, y3, 'g-.', linewidth=2, label='sin(x)*cos(x)')

# Customize appearance
plt.title("Trigonometric Functions", fontsize=16, fontweight='bold', pad=15)
plt.xlabel("X-axis (radians)", fontsize=12, labelpad=10)
plt.ylabel("Y-axis (values)", fontsize=12, labelpad=10)

# Legend customization
plt.legend(loc='upper right', fontsize=11, frameon=True, shadow=True, fancybox=True)

# Grid customization
plt.grid(True, alpha=0.3, linestyle='--')

# Axis limits and ticks
plt.xlim(0, 10)
plt.ylim(-1.5, 1.5)
plt.xticks(np.arange(0, 11, 1))
plt.yticks(np.arange(-1.5, 1.6, 0.5))

# Add annotations
plt.annotate('Maximum', xy=(np.pi/2, 1), xytext=(3, 0.8),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Add text box
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
plt.text(0.5, -1.2, 'Plot showing sin(x), cos(x), and their product', 
         fontsize=10, bbox=props)

plt.tight_layout()
plt.show()