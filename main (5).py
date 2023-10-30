# Implement a function called sort_students that takes a list of student objects as input and sorts the list based on their CGPA (Cumulative Grade Point Average) in descending order. Each student object has the following attributes: name (string), roll_number (string), and cgpa (float). Test the function with different input lists of students
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa
def sort_students(students):
    # Your code here
    return sorted(students, key=lambda x: x.cgpa, reverse=True)
# Test the function with different input lists of students
# Example usage:
student1 = Student("John", "12345", 3.8)
student2 = Student("Jane", "67890", 3.9)
student3 = Student("Bob", "54321", 3.7)
students = [student1, student2, student3]
sorted_students = sort_students(students)
# print the sorted list of students
for student in sorted_students:
    print(f"Name:{student.name}, Roll Number:{student.roll_number}, CGPA:{student.cgpa}") 
