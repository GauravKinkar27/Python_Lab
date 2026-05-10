class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")
class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")
    def eat(self):
        print(f"{self.name} is eating dog food")
print("=== Single Inheritance ===")
animal = Animal("Generic Animal")
dog = Dog("Buddy")
print("\nAnimal actions:")
animal.eat()
animal.sleep()
print("\nDog actions:")
dog.eat()     # Overridden method
dog.sleep()   # Inherited method
dog.bark()    # Child's own method
