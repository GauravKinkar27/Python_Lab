squares = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares}")
evens = {x: "even" for x in range(1, 11) if x % 2 == 0}
print(f"Even numbers: {evens}")
original = {"a": 1, "b": 2, "c": 3, "d": 4}
swapped = {v: k for k, v in original.items()}
print(f"Original: {original}")
print(f"Swapped (value:key): {swapped}")
words = ["apple", "banana", "cherry", "date"]
word_lengths = {word: len(word) for word in words}
print(f"Word lengths: {word_lengths}")
