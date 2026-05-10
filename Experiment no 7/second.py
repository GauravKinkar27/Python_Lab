def add_numbers(a, b):
    result = a + b
    print(f"Sum of {a} and {b} is {result}")
    return result
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
result = add_numbers(x, y)
print(f"Returned value: {result}")
