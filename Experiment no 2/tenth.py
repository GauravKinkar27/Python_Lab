num = int(input("Enter a number: "))
reverse = 0
temp = abs(num)
while temp > 0:
    reverse = reverse * 10 + temp % 10
    temp //= 10
if num < 0:
    reverse = -reverse
print(f"Reversed number: {reverse}")
