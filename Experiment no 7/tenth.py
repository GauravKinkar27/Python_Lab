def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a Prime number")
else:
    print(f"{num} is not a Prime number")
print("\nPrime numbers between 1 and 50:")
for i in range(1, 51):
    if is_prime(i):
        print(i, end=" ")
print()
