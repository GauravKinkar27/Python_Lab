my_tuple = (10, 20, 30, 40, 50)
element = int(input("Enter element to check: "))
if element in my_tuple:
    print(f"{element} is present in tuple at index {my_tuple.index(element)}")
else:
    print(f"{element} is not present in tuple")
