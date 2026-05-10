print("=== Lambda Function Demonstrations ===")
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

add = lambda a, b: a + b
print(f"Sum of 10 and 20: {add(10, 20)}")
# Lambda with filter (get even numbers)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {evens}")
# Lambda with map (square all numbers)
squares = list(map(lambda x: x ** 2, numbers))
print(f"Squares: {squares}")
# Lambda with sorted (sort by second element)
pairs = [(1, 'one'), (3, 'three'), (2, 'two')]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(f"Sorted by word: {sorted_pairs}")
