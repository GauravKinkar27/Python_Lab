class GrandParent:
    def __init__(self):
        self.grandparent_property = "House"
    def grandparent_method(self):
        print("This is GrandParent class")
        print(f"Grandparent property: {self.grandparent_property}")
class Parent(GrandParent):
    def __init__(self):
        GrandParent.__init__(self)
        self.parent_property = "Car"
    def parent_method(self):
        print("This is Parent class")
        print(f"Parent property: {self.parent_property}")
class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        self.child_property = "Laptop"
    def child_method(self):
        print("This is Child class")
        print(f"Child property: {self.child_property}")
c = Child()
c.grandparent_method()
c.parent_method()
c.child_method()
print(f"\nAll properties: {c.grandparent_property}, {c.parent_property}, {c.child_property}")
