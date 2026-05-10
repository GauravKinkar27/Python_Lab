print("=== Tuple Packing ===")
name, age, city = "Alice", 25, "New York"
person = name, age, city
print(f"Packed tuple: {person}")
print("\n=== Tuple Unpacking ===")
a, b, c = person
print(f"Unpacked: a={a}, b={b}, c={c}")
print("\n=== Swapping using tuple unpacking ===")
x, y = 10, 20
print(f"Before swap: x={x}, y={y}")
x, y = y, x
print(f"After swap: x={x}, y={y}")
