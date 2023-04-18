class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def make_sound(self):
        return "Woof"


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, species="Cat")

    def make_sound(self):
        return "Meow"
