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

# Task 1: Matplotlib Fundamentals
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



# Task 2: Seaborn & Statistical Analysis
# --- Part A: Distribution Analaysis ---

# 1. Distribution Plot: GPA Distribution by Gender
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Current_GPA', hue='Gender', kde=True, multiple='stack')
plt.title('Distribution of GPA by Gender', fontsize=14)
plt.xlabel('Current GPA')
plt.ylabel('Count')
# plt.show() # Uncomment to view individually


# 2. Violin Plot: Final Average across Majors
plt.figure(figsize=(12, 6))
sns.violinplot(data=df, x='Major', y='Final_Average', palette='Set2', inner='point')
plt.title('Distribution of Final Averages across Majors', fontsize=14)
plt.xlabel('Major')
plt.ylabel('Final Average')
plt.xticks(rotation=15)
# plt.show() # Uncomment to view individually


# 3. Box Plot with Seaborn: Study Hours across Academic Status
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Academic_Status', y='Study_Hours_Per_Week', hue='Academic_Status', palette='viridis')
sns.swarmplot(data=df, x='Academic_Status', y='Study_Hours_Per_Week', color='0.25', size=3, alpha=0.6)

means = df.groupby('Academic_Status')['Study_Hours_Per_Week'].mean()
sns.boxplot(data=df, x='Academic_Status', y='Study_Hours_Per_Week', 
            showmeans=True, meanprops={"marker":"o", "markerfacecolor":"white", "markeredgecolor":"black", "markersize":"10"},
            boxprops={'alpha': 0.4})

plt.title('Study Hours by Academic Status', fontsize=14)
plt.xlabel('Academic Status')
plt.ylabel('Study Hours Per Week')
plt.legend(title='Status', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
# plt.show() # Uncomment to view individually


# --- Part B: Relationship Analysis ---

# 1. Correlation Heatmap
plt.figure(figsize=(12, 10))
numerical_cols = df.select_dtypes(include=[np.number]).columns
corr_matrix = df[numerical_cols].corr()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5, annot_kws={"size": 8})
plt.title("Correlation Heatmap of Numerical Variables", fontsize=14)
plt.tight_layout()
# plt.show() # Uncomment to view individually

# 2. Pair Plot
selected_vars = ['Current_GPA', 'Study_Hours_Per_Week', 'Attendance_Rate', 'Sleep_Hours', 'Previous_GPA', 'Gender']
sns.pairplot(df[selected_vars], hue='Gender', diag_kind='kde', plot_kws={'alpha': 0.6})
plt.suptitle('Pair Plot of Key Variables', y=1.02, fontsize=16)
# plt.show() # Uncomment to view individually

# 3. Regression Plot: Study Hours vs Current GPA
plt.figure(figsize=(10, 6))
sns.regplot(data=df, x='Study_Hours_Per_Week', y='Current_GPA', scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
plt.title('Regression: Study Hours vs Current GPA', fontsize=14)
plt.xlabel('Study Hours Per Week')
plt.ylabel('Current GPA')

x = df['Study_Hours_Per_Week']
y = df['Current_GPA']
correlation_matrix = np.corrcoef(x, y)
correlation_xy = correlation_matrix[0,1]
r_squared = correlation_xy**2

plt.text(0.05, 0.95, f'R² = {r_squared:.3f}', transform=plt.gca().transAxes, 
         fontsize=12, verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

plt.tight_layout()
# plt.show() # Uncomment to view individually


# --- Part C: Categorical Analysis ---

# 1. Count Plot: Distributio of students across Majors
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='Major', order=df['Major'].value_counts().index, palette='viridis')
plt.title('Distribution of Students Across Majors', fontsize=14)
plt.xlabel('Major')
plt.ylabel('Count')
plt.xticks(rotation=15)

ax = plt.gca()
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', fontsize=11, color='black', xytext=(0, 5),
                textcoords='offset points')
plt.tight_layout()
# plt.show() # Uncomment to view individually

# 2. Grouped Analysis: Average GPA by Major and Year
plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='Major', y='Current_GPA', hue='Year', palette='muted', errorbar='sd')
plt.title('Average GPA by Major and Year', fontsize=14)
plt.xlabel('Major')
plt.ylabel('Average GPA')
plt.legend(title='Year', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
# plt.show() # Uncomment to view individually

# 3. Facet Grid: Attendance vs GPA by Gender and Scholarship
facet_grid = sns.FacetGrid(df, row='Gender', col='Has_Scholarship', margin_titles=True, height=4, aspect=1.2)
facet_grid.map(sns.scatterplot, 'Attendance_Rate', 'Current_GPA', alpha=0.6, edgecolor='w')
# plt.show() # Uncomment to view individually


# Task 3: Comprehensive Visual Story
# --- Part A: Research Questions ---
"""
Research Questions:
1. What factors most strongly predict student GPA (Study Hours, Attendance, etc.)?
2. How do study habits (Study Hours) differ across academic performance levels (GPA ranges)?
3. Does having a scholarship correlate with better performance (GPA) and higher attendance?
4. Are there significant differences in performance across different majors?
"""

# --- Part B: Visual Dashboard ---


fig = plt.figure(figsize=(20, 15))
gs = fig.add_gridspec(3, 3)
fig.suptitle('Comprehensive Student Performance Analysis Dashboard', fontsize=24, weight='bold')

# 1. Overview Section: Overall GPA Distribution
ax1 = fig.add_subplot(gs[0, 0])
sns.histplot(data=df, x='Current_GPA', kde=True, color='skyblue', ax=ax1)
ax1.set_title('Overall GPA Distribution', fontsize=14)
ax1.axvline(df['Current_GPA'].mean(), color='red', linestyle='--', label=f'Mean: {df["Current_GPA"].mean():.2f}')
ax1.legend()

# 2. Performance Factors Analysis: Study Hours vs Performance (with Regression)
ax2 = fig.add_subplot(gs[0, 1])
sns.regplot(data=df, x='Study_Hours_Per_Week', y='Current_GPA', ax=ax2, scatter_kws={'alpha':0.3}, line_kws={'color':'green'})
ax2.set_title('Study Hours vs GPA', fontsize=14)

# 3. Performance Factors Analysis: Attendance vs Performance (Hexbin for density)
ax3 = fig.add_subplot(gs[0, 2])
hb = ax3.hexbin(df['Attendance_Rate'], df['Current_GPA'], gridsize=20, cmap='Blues')
ax3.set_title('Attendance vs GPA (Density)', fontsize=14)
ax3.set_xlabel('Attendance Rate')
ax3.set_ylabel('GPA')
cb = fig.colorbar(hb, ax=ax3)
cb.set_label('Count')

# 4. Comparative Analysis: Performance by Major (Boxplot)
ax4 = fig.add_subplot(gs[1, :])
sns.boxplot(data=df, x='Major', y='Current_GPA', palette='Set3', ax=ax4)
ax4.set_title('GPA Distribution by Major', fontsize=14)

# 5. Comparative Analysis: Scholarship Impact on GPA and Attendance
ax5 = fig.add_subplot(gs[2, 0])
sns.violinplot(data=df, x='Has_Scholarship', y='Current_GPA', palette='pastel', ax=ax5)
ax5.set_title('Scholarship vs GPA', fontsize=14)

ax6 = fig.add_subplot(gs[2, 1])
sns.boxplot(data=df, x='Has_Scholarship', y='Attendance_Rate', palette='pastel', ax=ax6)
ax6.set_title('Scholarship vs Attendance', fontsize=14)

# 6. Summary Statistics / Insights Box
ax7 = fig.add_subplot(gs[2, 2])
ax7.axis('off')
summary_text = (
    "Key Findings:\n"
    "- Strong positive correlation between Study Hours and GPA.\n"
    "- Attendance is a crucial factor; higher attendance correlates with higher GPA.\n"
    "- Scholarship students tend to have slightly higher median GPAs and better attendance.\n"
    "- GPA distributions vary by major, but most centers around 2.5 - 3.0.\n"
    "\n"
    "Recommendations:\n"
    "- Encourage consistent study habits (>15 hrs/week).\n"
    "- Monitor attendance as an early warning sign.\n"
    "- Investigate support needed for majors with lower average GPAs."
)
ax7.text(0.5, 0.5, summary_text, ha='center', va='center', fontsize=12, wrap=True,
         bbox=dict(boxstyle='round,pad=1', facecolor='lightyellow', alpha=0.5))

plt.tight_layout(rect=[0, 0.03, 1, 0.96])
plt.savefig('task3_dashboard.png', dpi=300)
plt.show()

# --- Part C: Insights & Recommendations (Text Analysis) ---
"""

INSIGHTS & RECOMMENDATIONS
1.	Main Findings:
	•	Study Hours: it’s super clear that the more you study, the higher GPA you end up having. It’s kinda linear — people who put in hours get results.
	•	Attendance: if someone attends >80% classes, their GPA is usually high too. Low attendance is basically a red flag.
	•	Scholarship Kids: students with scholarships have more “tight” GPA range and usually higher attendance. Probably they’re more motivated or maybe scholarships already pick strong students.
	•	Majors: overall GPA between majors is kinda similar, but majors like Math/Science have more spread (some ppl do super good, some do bad).

2.	Patterns / Interpretation:
	•	The “Study Hours vs GPA” plot pretty much confirms that the main factor of good grades is just effort/time.
	•	In the “Attendance vs GPA” plot, the weird points (high attendance but low GPA) maybe mean students do attend but the material is too hard or not clicking for them.

3.	Recommendations (practical stuff):
	•	Students: try to do like 15–20 hours of studying per week at minimum. Also, going to classes helps a lot, don’t skip if possible.
	•	University: they should check on students whose attendance falls below like 75%. Maybe give them help earlier. Also, majors like Math/Science probably need some extra tutoring or support, cause many students struggle.
	•	At-risk groups: students without scholarships + those who also work part-time might need help like flexible class schedules or maybe info/aid about financial support.

4.	Limitations:
	•	Not causation: Yeah, study hours correlate with GPA but that doesn’t automatically prove one causes the other.
	•	Missing factors: stuff like mental health, prior school quality, or if a student actually likes their major can affect GPA too, but we don’t have that data here.
"""