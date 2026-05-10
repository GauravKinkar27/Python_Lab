numbers = [int(x) for x in input("Enter numbers with duplicates: ").split()]
print(f"Original list: {numbers}")
unique = list(set(numbers))
print(f"List after removing duplicates: {unique}")
