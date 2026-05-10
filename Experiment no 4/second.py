numbers = input("Enter numbers separated by space: ").strip()

if numbers:
    numbers = [int(x) for x in numbers.split()]
    total = sum(numbers)
    average = total / len(numbers)
    print(f"Sum: {total}")
    print(f"Average: {average}")
else:
    print("No numbers entered.")