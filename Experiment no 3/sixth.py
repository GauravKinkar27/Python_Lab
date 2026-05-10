s = input("Enter a string: ")
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print("Character frequency:")
for char, count in freq.items():
    print(f"'{char}': {count}")
