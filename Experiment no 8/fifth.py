class Father:
    def __init__(self):
        self.father_skill = "Cooking"
    def skills(self):
        print(f"Father's skills: {self.father_skill}, Driving")
class Mother:
    def __init__(self):
        self.mother_hobby = "Reading"
    def hobbies(self):
        print(f"Mother's hobbies: {self.mother_hobby}, Gardening")
class Child(Father, Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)
        self.talent = "Singing"
    def talents(self):
        print(f"Child's talents: {self.talent}, Dancing")
c = Child()
print("Child inherits from both Father and Mother:")
c.skills()
c.hobbies()
c.talents()
