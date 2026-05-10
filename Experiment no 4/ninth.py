numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
unique = list(set(numbers))
unique.sort()
if len(unique) >= 2:
    print(f"Second largest: {unique[-2]}")
else:
    print("Not enough unique elements")
