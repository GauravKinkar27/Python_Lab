def factorial_recursive(n):
    # Base case
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)
num = int(input("Enter a number: "))
if num < 0:
    print("Factorial is not defined for negative numbers")
else:
    result = factorial_recursive(num)
    print(f"Factorial of {num} (recursive) is {result}")
