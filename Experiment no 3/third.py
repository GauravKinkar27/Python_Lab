s = input("Enter a string: ").lower().replace(" ", "")
if s == s[::-1]:
    print("String is Palindrome")
else:
    print("String is not Palindrome")
