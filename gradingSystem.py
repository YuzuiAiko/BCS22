


#from tabulate import tabulate

class GradingSystem:

    def __init__(self, name, q1, q2, q3, cp):
        self.name = name
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.cp = cp
        self.fe = self.calculate_FinalGrade()
        self.grade = self.calculate_grade()
        self.status = self.calculate_status()

    def calculate_grade(self):
        # Calculate Grades: "A" to "F"
        total_score = self.q1 + self.q2 + self.q3 + self.cp + self.fe

        if total_score >= 90:
            return "A"
        elif total_score >= 80:
            return "B"
        elif total_score >= 70:
            return "C"
        elif total_score >= 60:
            return "D"
        else:
            return "F"

    def calculate_status(self):
        # Determine the status based on your grades
        if self.grade == "F":
            return "Failed"
        else:
            return "Passed"

    def calculate_FinalGrade(self):
        total_Score = (self.q1 + self.q2 + self.q3 + self.cp) / 4
        return total_Score


# Create a list to store instances of GradingSystem
students = []

while True:
    name = input("Name: ")
    q1 = int(input("Score Quiz 1: "))
    q2 = int(input("Score Quiz 2: "))
    q3 = int(input("Score Quiz 3: "))
    cp = int(input("Class Participation: "))
    fe = int(input("Final Exam: "))

    # Create an instance of GradingSystem and append it to the list
    student = GradingSystem(name, q1, q2, q3, cp)
    students.append(student)

    another_user = input("Do you want to input grades for another user? (yes/no): ").lower()
    if another_user != 'yes':
        break

# Display the information for all users
for student in students:
    print("\nStudent Information:")
    print(f"Name: {student.name}")
    print(f"Q1: {student.q1}")
    print(f"Q2: {student.q2}")
    print(f"Q3: {student.q3}")
    print(f"CP: {student.cp}")
    print(f"FE: {student.fe}")
    print(f"Grade: {student.grade}")
    print(f"Status: {student.status}")