numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
search = int(input("Enter element to search: "))
if search in numbers:
    print(f"Element {search} found at index {numbers.index(search)}")
else:
    print(f"Element {search} not found")
