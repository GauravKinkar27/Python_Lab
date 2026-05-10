dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"d": 4, "e": 5, "f": 6}
print(f"Dictionary 1: {dict1}")
print(f"Dictionary 2: {dict2}")
# Method 1: Using unpacking operator (Python 3.5+)
merged1 = {**dict1, **dict2}
print(f"Merged using unpacking: {merged1}")
# Method 2: Using update() method
dict1.update(dict2)
print(f"Merged using update(): {dict1}")
