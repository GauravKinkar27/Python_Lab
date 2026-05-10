student = {
    "name": "John Doe",
    "roll_no": 101,
    "branch": "Computer Science",
    "year": 2,
    "marks": 85.5
}
print("Student Details:")
print("=" * 30)
for key, value in student.items():
    print(f"{key}: {value}")
