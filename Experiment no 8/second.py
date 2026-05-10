class Person:
    def __init__(self, name, age):
        print(f"Constructor called for {name}")
        self.name = name
        self.age = age
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
print("Creating objects...")
p1 = Person("Alice", 25)
p2 = Person("Bob", 30)
print("\nDisplaying details:")
p1.display()
p2.display()
