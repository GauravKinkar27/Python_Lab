students = {}
n = int(input("Enter number of students: "))
for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    marks = float(input(f"Enter marks of {name}: "))
    students[name] = marks
print(f"\nStudent records: {students}")
topper = max(students, key=students.get)
print(f"Student with highest marks: {topper}")
print(f"Marks: {students[topper]}")
