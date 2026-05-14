class Dog:
    def __init__(self):
        self.bark = "Woof!"


class Cat:
    def __init__(self):
        self.meow = "Meow!"


class CatDog(Dog, Cat):
    def __init__(self):
        super().__init__()
        Cat.__init__(self)
        self.name = "CatDog"


pet = CatDog()

print(f"Character Name: {pet.name}")
print(f"Dog side says: {pet.bark}")
print(f"Cat side says: {pet.meow}")
