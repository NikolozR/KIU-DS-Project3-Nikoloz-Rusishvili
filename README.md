# Project 3: Data Visualization & EDA

**Name:** Nikoloz Rusishvili  
**Date:** 2025-12-05

## Project Description
This project performs an exploratory data analysis (EDA) on a student performance dataset. Using Python libraries such as Matplotlib and Seaborn, it explores relationships between various factors (study hours, attendance, scholarships, majors) and academic success (GPA).

## Instructions to Run
1. Ensure you have the required libraries installed:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the main analysis script:
   ```bash
   python Project3_Nikoloz_Rusishvili.py
   ```
   - The script will generate and display several visualizations.
   - Key figures will be saved in the `figures/` directory.

## Key Findings & Insights

### 1. Main Findings
*   **Study Hours:** It’s super clear that the more you study, the higher GPA you end up having. It’s kinda linear — people who put in hours get results.
*   **Attendance:** If someone attends >80% of classes, their GPA is usually high too. Low attendance is basically a red flag.
*   **Scholarship Kids:** Students with scholarships have a more “tight” GPA range and usually higher attendance. Probably they’re more motivated or maybe scholarships already pick strong students.
*   **Majors:** Overall GPA between majors is kinda similar, but majors like Math/Science have more spread (some people do super good, some do bad).

### 2. Patterns / Interpretation
*   The “Study Hours vs GPA” plot pretty much confirms that the main factor of good grades is just effort/time.
*   In the “Attendance vs GPA” plot, the weird points (high attendance but low GPA) maybe mean students do attend but the material is too hard or not clicking for them.

### 3. Recommendations
*   **Students:** Try to do like 15–20 hours of studying per week at minimum. Also, going to classes helps a lot, don’t skip if possible.
*   **University:** They should check on students whose attendance falls below like 75%. Maybe give them help earlier. Also, majors like Math/Science probably need some extra tutoring or support, cause many students struggle.
*   **At-risk groups:** Students without scholarships + those who also work part-time might need help like flexible class schedules or maybe info/aid about financial support.

### 4. Limitations
*   **Not causation:** Yeah, study hours correlate with GPA but that doesn’t automatically prove one causes the other.
*   **Missing factors:** Stuff like mental health, prior school quality, or if a student actually likes their major can affect GPA too, but we don’t have that data here.

