"""
The Composite design pattern is a structural pattern that allows you to compose objects into tree-like structures to represent part-whole hierarchies. In Python, the Composite pattern can be implemented by creating a Component class that defines the interface for objects in the composition, and a Composite class that holds a collection of Component objects and implements the same interface as Component.

For example, a Shape class could be the Component class and CompositeShape class could be the Composite class:

"""

class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        print(f"Drawing Circle at ({self.x}, {self.y}) with radius {self.radius}")

class Square(Shape):
    def __init__(self, x, y, side_length):
        self.x = x
        self.y = y
        self.side_length = side_length

    def draw(self):
        print(f"Drawing Square at ({self.x}, {self.y}) with side length {self.side_length}")


class CompositeShape(Shape):
    def __init__(self):
        self._shapes = []

    def draw(self):
        for shape in self._shapes:
            shape.draw()

    def add_shape(self, shape):
        self._shapes.append(shape)

    def remove_shape(self, shape):
        self._shapes.remove(shape)


def main():
    # usage
    composite = CompositeShape()
    composite.add_shape(Circle(0, 0, 5))
    composite.add_shape(Square(5, 5, 10))

    # Creating another composite shape
    composite2 = CompositeShape()
    composite2.add_shape(Circle(10, 10, 7))
    composite2.add_shape(Square(15, 15, 12))

    # Adding composite2 to composite
    composite.add_shape(composite2)

    composite.draw()


if __name__ == '__main__':
    main()
