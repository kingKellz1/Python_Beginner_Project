# 🧮 Student Grade Tracker (Beginner Python Project)
> A simple terminal-based program to collect student data and calculate average GPA.

This beginner-friendly Python project allows users to input student information, including their name, age, and letter grades for multiple subjects. The program then calculates the total grade points and GPA based on a standard 4.0 scale. It includes data validation, clear summaries, and an option to process multiple students.

It's designed as a foundational project to reinforce basic Python skills like loops, conditionals, functions, and dictionaries.


## Features
- Collects student name, age, and subject grades
- Validates letter grades (A, B, C, D, F)
- Converts letter grades to GPA points
- Calculates total grade points and average GPA
- Allows multiple student entries in one session
- Clean and readable output summary

## How to Run
1. Make sure you have Python installed (version 3+).
2. Clone the repository or download the `.py` file.
3. Open a terminal and navigate to the project folder.
4. Follow the prompts in the terminal to:
- Enter a student's name and age
- Enter subjects and letter grades
- View a summary with total points and GPA

5. Choose to enter another student's data or exit the program.


```bash
python beginner_project.py


---

### 🔹 Example Output
```markdown
## Example Output
Enter student name: Alex
Enter student age: 17
Enter the number of subjects: 3
Enter the name of the subject 1: Math
Enter the letter grade for Math: A
Enter the name of the subject 2: English
Enter the letter grade for English: B
Enter the name of the subject 3: History
Enter the letter grade for History: C

Student Information Summary:
Name: Alex
Age: 17
Subjects and Grades:

Math: A
English: B
History: C
Total Points: 9
Average: 3.00

## 🛠 Technologies Used

- **Python 3** – Core language used to build the program.
- **Git & GitHub** – Version control and project hosting.
- **VS Code / Terminal** – Used for writing and running the script.

This project was created as part of a beginner Python curriculum, with a focus on clean code, functions, loops, conditionals, user input, and data structures like dictionaries and lists.

## 🚀 Features
- **Student Information Input**: Allows users to input multiple students' data, including name, age, subjects, and letter grades.
- **Grade Conversion**: Converts letter grades into numerical grade points for GPA calculation.
- **Total Points & Average Calculation**: Automatically calculates the total points and the average GPA for each student.
- **Repeatable Data Entry**: After completing one student's information, the program prompts the user to enter another student's data, allowing for multiple entries.
- **Input Validation**: Ensures that the user provides valid letter grades (A, B, C, D, F) for each subject.
- **Clear and Readable Output**: Displays a summary of the student's information, total points, and GPA in a well-organized format.

## 📚 What I Learned

- **User Input Handling**: I learned how to handle user input dynamically, including converting data types (e.g., strings to integers) and validating input for correctness (e.g., ensuring valid grades).
  
- **Data Structures in Python**: I gained experience working with dictionaries and lists to store and manipulate user information. I learned how to efficiently organize student data and grades within these structures.

- **Control Flow**: I practiced using loops (for loops and while loops) to repeat tasks, such as entering multiple students' data, and conditionals (if-else) to make decisions based on user input.

- **Grade Calculation Logic**: I learned how to map letter grades to numerical values using dictionaries and how to calculate a student’s GPA by summing these values and computing the average.

- **Function Definition**: I honed my skills in defining and calling functions, breaking down the project into manageable sections with clear inputs and outputs for readability and reusability.

- **Error Handling**: I incorporated basic error handling by validating the letter grades entered by the user to ensure that only valid grades are accepted, improving the program's robustness.

- **Refactoring Code for Clarity**: I focused on making the code modular and clear by separating distinct tasks into functions such as `grab_student_info()`, `t_n_a()`, and `display_student_information()` to enhance readability and maintainability.
