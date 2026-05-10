def factorial(n):
    """Calculate factorial iteratively"""
    if n < 0:
        return "Undefined (negative number)"
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
num = int(input("Enter a number: "))
result = factorial(num)
print(f"Factorial of {num} is {result}")
