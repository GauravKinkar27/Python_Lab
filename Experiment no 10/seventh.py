# Program to draw pie chart
import matplotlib.pyplot as plt

# Data
languages = ['Python', 'Java', 'C++', 'JavaScript', 'Go']
market_share = [28, 18, 15, 14, 10]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
explode = (0.1, 0, 0, 0, 0)  # Explode first slice

# Create pie chart
plt.figure(figsize=(8, 8))
plt.pie(market_share, labels=languages, colors=colors, explode=explode,
        autopct='%1.1f%%', startangle=90, shadow=True)

plt.title("Programming Languages Market Share", fontsize=14, fontweight='bold')
plt.axis('equal')  # Equal aspect ratio ensures pie is circular
plt.show()