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


class PetFactory:
    def get_pet(self, pet_type):
        if pet_type == "Dog":
            return Dog("Dog")
        elif pet_type == "Cat":
            return Cat("Cat")


def main():
    factory = PetFactory()
    pet = factory.get_pet("Dog")
    print(pet.speak())

    pet = factory.get_pet("Cat")
    print(pet.speak())


if __name__ == '__main__':
    main()
