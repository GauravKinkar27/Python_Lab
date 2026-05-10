def calculate(a, b):
    return a + b, a - b, a * b, a / b
x = 10
y = 3
print(f"Numbers: {x}, {y}")
s, d, p, q = calculate(x, y)
print(f"Sum: {s}")
print(f"Difference: {d}")
print(f"Product: {p}")
print(f"Quotient: {q:.2f}")
