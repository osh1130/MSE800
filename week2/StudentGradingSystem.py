# Student Grading System
# This program lets users input student names, record their grades, and display performance summaries.

# Define a Student class to manage student name and grades
class Student:
    def __init__(self, name):
        # Initialize with student name and an empty list for grades
        self.name = name
        self.grades = []

    def add_grade(self, score):
        # Add a numeric grade to the list
        self.grades.append(score)

    def average(self):
        # Calculate average grade; return 0 if no grades yet
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def display(self):
        # Display student info and grades
        print(f"\nStudent Name: {self.name}")
        print(f"Grades: {self.grades}")
        print(f"Average Score: {self.average():.2f}\n")

# Main program to interact with users
def main():
    # Dictionary to hold multiple students by name
    students = {}

    while True:
        # Menu display
        print("========= Student Grading Menu =========")
        print("1. Add New Student")
        print("2. Add Grade to Student")
        print("3. Show Student Report")
        print("4. Exit")
        print("========================================")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            # Add a new student
            name = input("Enter student name: ")
            if name in students:
                print("Student already exists.\n")
            else:
                students[name] = Student(name)
                print(f"Student '{name}' added.\n")

        elif choice == '2':
            # Add grade to a student
            name = input("Enter student name: ")
            if name not in students:
                print("Student not found.\n")
            else:
                try:
                    score = float(input("Enter grade (0-100): "))
                    if 0 <= score <= 100:
                        students[name].add_grade(score)
                        print(f"Grade {score} added to {name}.\n")
                    else:
                        print("Grade must be between 0 and 100.\n")
                except ValueError:
                    print("Invalid input. Please enter a number.\n")

        elif choice == '3':
            # Show student report
            name = input("Enter student name: ")
            if name in students:
                students[name].display()
            else:
                print("Student not found.\n")

        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Start the program
if __name__ == "__main__":
    main()
