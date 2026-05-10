class Bird:
    def sound(self):
        return "Some bird sound"
    def move(self):
        return "Flying"
class Dog:
    def sound(self):
        return "Woof!"
    def move(self):
        return "Running"
class Fish:
    def sound(self):
        return "Blub blub"
    def move(self):
        return "Swimming"
class Cat:
    def sound(self):
        return "Meow!"
    def move(self):
        return "Walking"
def demonstrate_polymorphism(animal):
    print(f"{animal.__class__.__name__}:")
    print(f"  Sound: {animal.sound()}")
    print(f"  Movement: {animal.move()}")
animals = [Bird(), Dog(), Fish(), Cat()]
for animal in animals:
    demonstrate_polymorphism(animal)
print("\n=== Duck Typing (Python's polymorphism style) ===")
print("'If it walks like a duck and quacks like a duck, it's a duck'")
print("Python focuses on behavior, not type.")
