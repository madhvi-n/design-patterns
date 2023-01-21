"""
The Builder pattern is a creational design pattern that allows you to create complex objects step by step, by separating the construction of the object from its representation. This can be useful in situations where you need to create an object with many optional or interchangeable parts
"""


class Builder:
    def build_part_a(self):
        pass

    def build_part_b(self):
        pass

    def get_result(self):
        pass


class ConcreteBuilder(Builder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.add("PartA")

    def build_part_b(self):
        self.product.add("PartB")

    def get_result(self):
        return self.product


class Product:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        print(f'Product parts: {", ".join(self.parts)}')


class Director:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder):
        self.builder = builder

    def build_minimal_viable_product(self):
        self.builder.build_part_a()

    def build_full_featured_product(self):
        self.builder.build_part_a()
        self.builder.build_part_b()


def main():
    # usage
    director = Director()
    builder = ConcreteBuilder()
    director.set_builder(builder)

    director.build_minimal_viable_product()
    product = builder.get_result()
    product.list_parts() # Output: Product parts: PartA

    director.build_full_featured_product()
    product = builder.get_result()
    product.list_parts() # Output: Product parts: PartA, PartB


if __name__ == '__main__':
    main()
