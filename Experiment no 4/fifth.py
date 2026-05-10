numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)
print(f"List after removing duplicates: {unique}")
