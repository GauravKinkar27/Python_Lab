numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
even = sum(1 for n in numbers if n % 2 == 0)
odd = len(numbers) - even
print(f"Even numbers: {even}")
print(f"Odd numbers: {odd}")
