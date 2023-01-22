"""
The Visitor pattern is a behavioral design pattern that allows adding new behavior to a set of existing classes, without changing their code. It separates the operation being performed on an object from the object itself. It uses a Visitor object, which contains the new behavior, and visits each element in a collection of objects, performing the operation.

In Python, the Visitor pattern can be implemented using a class hierarchy, where the base class defines an accept method that takes a Visitor object as an argument. The derived classes implement the accept method and call the appropriate method on the Visitor object.
"""

class Visitor:
    def visit_dog(self, dog):
        pass

    def visit_cat(self, cat):
        pass


class Animal:
    def accept(self, visitor):
        pass


class Dog(Animal):
    def accept(self, visitor):
        visitor.visit_dog(self)


class Cat(Animal):
    def accept(self, visitor):
        visitor.visit_cat(self)


class SoundVisitor(Visitor):
    def visit_dog(self, dog):
        print("Woof woof!")

    def visit_cat(self, cat):
        print("Meow meow!")


def main():
    animals = [Dog(), Cat(), Dog(), Cat()]
    sound_visitor = SoundVisitor()
    for animal in animals:
        animal.accept(sound_visitor)


if __name__ == '__main__':
    main()
