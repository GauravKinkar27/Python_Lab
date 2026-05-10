student = {"name": "Bob", "age": 19}
print(f"Original: {student}")
student["city"] = "Mumbai"
print(f"After adding city: {student}")
student["age"] = 20
print(f"After updating age: {student}")
student.update({"course": "Python", "marks": 88})
print(f"After adding multiple: {student}")
