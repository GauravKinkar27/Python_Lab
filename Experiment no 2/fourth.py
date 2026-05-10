num = int(input("Enter a number: "))
if num <= 1:
    print(f"{num} is not Prime")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} is Prime")
    else:
        print(f"{num} is not Prime")
