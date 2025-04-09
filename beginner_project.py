# Student Grade Tracker
# Created by: [ Nicheal Hickson]
# Description: This program collects a student's name, age, and subject grades.
# It calculates the total grade points and average GPA based on letter grades.
# The user can input multiple students' data in one session.


# Function to collect student's name, age, and their subject grades
def grab_student_info(): 
	student_info ={
		"user_name": input("Enter student name: "),
		"user_age": int(input("Enter student age: ")),
		"user_grade": []
	}
	number_of_subjects = int(input("Enter the number of subjects: "))
	for i in range(number_of_subjects):
		new_sub = input(f"Enter the name of the subject {i + 1}: ")
		student_grade = input(f"Enter the letter grade for {new_sub}: ").upper()

		while student_grade not in ["A", "B", "C", "D", "F"]:
			print("Invalid grade. Please enter a grade from A, B, C, D, F.")
			student_grade = input(f"Enter the letter grade for {new_sub}: ").upper()

		student_info["user_grade"].append({
			"subject": new_sub,
			"grade": student_grade
			})
	return student_info

# Function to calculate total points and average GPA from letter grades
def t_n_a(user_grade, num_subjects):
	grade_points = {
		"A": 4,
		"B": 3,
		"C": 2,
		"D": 1,
		"F": 0
	}

	result = 0
	for grade in user_grade:
		letter = grade["grade"]
		numerical_grade = grade_points[letter]
		result += numerical_grade

	average = result / num_subjects
	return result, average

# Function to display the collected information in a formatted summary
def display_student_information(student_info, total, average):
	print("\nStudent Information Summary:")
	print("Name:", student_info["user_name"])
	print("Age:", student_info["user_age"])
	print("Subjects and Grades:")
	for subject in student_info["user_grade"]:
		print(f"- {subject['subject']}: {subject['grade']}")
	print(f"Total Points: {total}")
	print(f"Average: {average:.2f}")

# Main loop to control user flow: input, calculation, and display
def main():
	while True:
		student_info = grab_student_info()
		total, average = t_n_a(student_info["user_grade"], len(student_info["user_grade"]))
		display_student_information(student_info, total, average)

		#Ask if user wants to enter another student
		again = input("\nDo you want to enter another student's data? (yes/no): ").lower()
		if again != "yes":
			print("Goodbye!")
			break

# This ensures the main program runs only when this file is executed directly
if __name__ == "__main__":
	main()
	