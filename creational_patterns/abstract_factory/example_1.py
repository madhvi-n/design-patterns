"""
In this example, we have two classes Dog and Cat which are the concrete classes that we want to create. We also have two factory classes DogFactory and CatFactory which are the abstract classes that we want to use to create the objects. The PetStore class is the client class that uses the factory classes to create the objects.

We can see that, the PetStore class is not dependent on the concrete classes, it only cares about the interface (methods) of the factory classes. Now, if in future, we want to add more animals or change the way we create the animals, we can do it by just adding or changing the factory classes without affecting the client classes.

This way the Abstract Factory pattern can help us to create objects without specifying the exact class of object that will be created. It allows a system to be independent of how its objects are created, composed and represented.
"""

class Dog:
    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Woof!"


class Cat:
    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Meow!"


class Bird:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Chirp!"


class DogFactory:
    def get_pet(self):
        return Dog("Dog")

    def get_food(self):
        return "Dog food"


class CatFactory:
    def get_pet(self):
        return Cat("Cat")

    def get_food(self):
        return "Cat food"


class BirdFactory:
    def get_pet(self):
        return Bird("Bird")

    def get_food(self):
        return "Bird food"


class PetStore:
    def __init__(self, pet_factory=None):
        self._pet_factory = pet_factory

    def show_pet(self):
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()
        print("Our pet is '{}'!".format(pet.speak()))
        print("Our pet says hello by '{}'!".format(pet.speak()))
        print("Its food is '{}'!".format(pet_food))


def main():
    factory = DogFactory()
    shop = PetStore(factory)
    shop.show_pet()

    factory = CatFactory()
    shop = PetStore(factory)
    shop.show_pet()

    factory = BirdFactory()
    shop = PetStore(factory)
    shop.show_pet()


if __name__ == '__main__':
    main()
