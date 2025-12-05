"""
Project 3: Data Visualization & EDA
Name: Nikoloz Rusishvili
Date: 2025-12-05
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

try:
    df = pd.read_csv('student_performance.csv')
except FileNotFoundError:
    print("Error: student_performance.csv not found. Please run generate_project3_data.py first.")
    exit()


# --- Part A: Individual Plot Types ---

# 1. Line Plot: Relationship between Study Hours and GPA
plt.figure(figsize=(10, 6))
df_sorted_study = df.sort_values(by='Study_Hours_Per_Week')
plt.plot(df_sorted_study['Study_Hours_Per_Week'], df_sorted_study['Current_GPA'], 
         color='teal', linestyle='-', linewidth=1, marker='o', markersize=3, alpha=0.7)
plt.title('Relationship Between Study Hours and GPA', fontsize=14)
plt.xlabel('Study Hours Per Week')
plt.ylabel('Current GPA')
plt.grid(True)
plt.tight_layout()
# plt.show() # Uncomment to view individually



# 2. Scatter Plot: Attenance Rate vs Final Average
plt.figure(figsize=(10, 6))
majors = df['Major'].unique()
colors = plt.cm.tab10(np.linspace(0, 1, len(majors)))

for i, major in enumerate(majors):
    subset = df[df['Major'] == major]
    plt.scatter(subset['Attendance_Rate'], subset['Final_Average'], 
                label=major, alpha=0.6, color=colors[i])

plt.title('Attendance Rate vs Final Average by Major', fontsize=14)
plt.xlabel('Attendance Rate (%)')
plt.ylabel('Final Average')
plt.legend(title='Major')
plt.grid(True)
plt.tight_layout()
# plt.show() # Uncomment to view individually



# 3. Bar Chart: Average GPA by Majorრ
plt.figure(figsize=(10, 6))
avg_gpa_major = df.groupby('Major')['Current_GPA'].mean().sort_values(ascending=True)
bars = plt.barh(avg_gpa_major.index, avg_gpa_major.values, color='skyblue')
plt.title('Average GPA by Major', fontsize=14)
plt.xlabel('Average GPA')
plt.ylabel('Major')
# Add value labels
for bar in bars:
    width = bar.get_width()
    plt.text(width, bar.get_y() + bar.get_height()/2, f'{width:.2f}', 
             va='center', ha='left', fontsize=10)
plt.tight_layout()
# plt.show() # Uncomment to view individually





# 4. Histogram: Distribution of Current GPA
plt.figure(figsize=(10, 6))
gpa_data = df['Current_GPA'].dropna()
mean_gpa = gpa_data.mean()
median_gpa = gpa_data.median()
std_gpa = gpa_data.std()

count, bins, ignored = plt.hist(gpa_data, bins=25, density=True, alpha=0.6, color='purple', edgecolor='black')

plt.axvline(mean_gpa, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_gpa:.2f}')
plt.axvline(median_gpa, color='blue', linestyle='-', linewidth=2, label=f'Median: {median_gpa:.2f}')

xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = (1 / (std_gpa * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean_gpa) / std_gpa)**2)
plt.plot(x, p, 'k', linewidth=2, label='Normal Distribution')

plt.title('Distribution of Current GPA', fontsize=14)
plt.xlabel('Current GPA')
plt.ylabel('Density')
plt.legend()
plt.tight_layout()
# plt.show() # Uncomment to view individually



# 5. Box Plot: Compare course scores
plt.figure(figsize=(12, 6))
course_cols = ['Mathematics_Score', 'Programming_Score', 'Statistics_Score', 'English_Score', 'Science_Score']
plt.boxplot([df[col] for col in course_cols], labels=course_cols)
plt.title('Comparison of Course Scores', fontsize=14)
plt.ylabel('Score')
plt.xticks(rotation=15)
plt.grid(axis='y')
plt.tight_layout()
# plt.show() # Uncomment to view individually


# --- Part B: Subplots and Layout ---

# 2x2 Subplot Grid
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Student Performance Overview', fontsize=20)

# Top-left: GPA Distributon
axes[0, 0].hist(gpa_data, bins=20, color='lightgreen', edgecolor='black')
axes[0, 0].set_title('GPA Distribution')
axes[0, 0].set_xlabel('GPA')
axes[0, 0].set_ylabel('Count')

# Top-right: Study Hours vs GPA scatter
axes[0, 1].scatter(df['Study_Hours_Per_Week'], df['Current_GPA'], alpha=0.5, color='orange')
axes[0, 1].set_title('Study Hours vs GPA')
axes[0, 1].set_xlabel('Study Hours')
axes[0, 1].set_ylabel('GPA')

# Bottom-left: Average scores by Year
avg_score_year = df.groupby('Year')['Final_Average'].mean()
axes[1, 0].bar(avg_score_year.index, avg_score_year.values, color='salmon')
axes[1, 0].set_title('Average Final Score by Year')
axes[1, 0].set_xlabel('Year')
axes[1, 0].set_ylabel('Average Score')

# Bottom-right: Attendance distribution
axes[1, 1].hist(df['Attendance_Rate'], bins=20, color='lightblue', edgecolor='black')
axes[1, 1].set_title('Attendance Rate Distribution')
axes[1, 1].set_xlabel('Attendance Rate (%)')
axes[1, 1].set_ylabel('Count')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
# plt.show() # Uncomment to view individually


# --- Part C: Customization & Design ---

# 1. Extensive Cusomization: Detailed Scatter Plot
plt.figure(figsize=(12, 8)) 

custom_colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33F6', '#F6FF33']
majors = df['Major'].unique()

for i, major in enumerate(majors):
    subset = df[df['Major'] == major]
    plt.scatter(subset['Attendance_Rate'], subset['Final_Average'], 
                label=major, color=custom_colors[i % len(custom_colors)],
                s=70, alpha=0.7, edgecolor='white')

plt.title('Impact of Attendance on Final Performance', fontsize=18, fontweight='bold')
plt.xlabel('Attendance Rate (%)', fontsize=14)
plt.ylabel('Final Average', fontsize=14)
plt.legend(title='Major', fontsize=12, title_fontsize=14, shadow=True)
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)

# Anotation for the highest score
max_idx = df['Final_Average'].idxmax()
max_score = df.loc[max_idx, 'Final_Average']
max_att = df.loc[max_idx, 'Attendance_Rate']

plt.annotate(f'Highest Score: {max_score}', xy=(max_att, max_score), 
             xytext=(max_att - 15, max_score - 5),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=12, color='darkred')

# Text box with statistics
corr = df['Attendance_Rate'].corr(df['Final_Average'])
stats_text = f'Correlation: {corr:.2f}\nN = {len(df)}'
plt.text(0.95, 0.05, stats_text, transform=plt.gca().transAxes, 
         fontsize=12, verticalalignment='bottom', horizontalalignment='right',
         bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

plt.tight_layout()

# Savfig to file
plt.savefig('task1_customized_scatter.png', dpi=300)
# plt.show()

# 2. Save the Subplot from Part B
fig.savefig('task1_subplot_overview.png', dpi=300)
