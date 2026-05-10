def fibonacci(n):
    # Base cases
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
terms = int(input("Enter number of terms: "))
print("Fibonacci series:")
for i in range(terms):
    print(fibonacci(i), end=" ")
print()
