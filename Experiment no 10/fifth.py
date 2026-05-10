# Program to draw bar chart
import matplotlib.pyplot as plt

# Data
subjects = ['Python', 'Java', 'C++', 'JavaScript', 'HTML/CSS']
scores = [88, 75, 82, 90, 85]
colors = ['skyblue', 'lightgreen', 'lightcoral', 'gold', 'plum']

# Create bar chart
plt.figure(figsize=(10, 6))
plt.bar(subjects, scores, color=colors, edgecolor='black', linewidth=1.5)

# Add labels and title
plt.title("Student Scores by Subject", fontsize=14, fontweight='bold')
plt.xlabel("Subjects", fontsize=12)
plt.ylabel("Scores (%)", fontsize=12)
plt.ylim(0, 100)

# Add values on bars
for i, score in enumerate(scores):
    plt.text(i, score + 1, str(score), ha='center', fontsize=11)

plt.grid(axis='y', alpha=0.3)
plt.show()