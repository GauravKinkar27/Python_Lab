numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
numbers.sort()
print(f"Ascending order: {numbers}")
numbers.sort(reverse=True)
print(f"Descending order: {numbers}")
