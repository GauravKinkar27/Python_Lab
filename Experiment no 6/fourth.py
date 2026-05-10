student = {"name": "Charlie", "age": 21, "city": "Delhi", "course": "Python", "marks": 90}
print(f"Original: {student}")
removed = student.pop("city")
print(f"Removed 'city': {removed}")
print(f"After pop: {student}")
del student["course"]
print(f"After del: {student}")
last = student.popitem()
print(f"Removed last item: {last}")
print(f"After popitem: {student}")
student.clear()
print(f"After clear: {student}")
