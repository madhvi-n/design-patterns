"""
In this example, we have a Product class that represents a basic product, with a name and price attribute. We then define a ProductDecorator class that is a wrapper for a Product object, and allows us to add additional functionality to it. The SizeDecorator, ColorDecorator, and MaterialDecorator classes inherit from ProductDecorator and add the specific functionality for size, color, and material respectively.
We can then create a product object and use the decorators to add size, color and material to the product, which can be seen in the last line of the code.

It is worth noting that this is a simple example, in practice, it's important to consider how these decorators are created and used in order to make the codebase maintainable and easy to reason about.
"""

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        return f'{self.name} - ${self.price}'


class ProductDecorator:
    def __init__(self, product):
        self.product = product

    def get_info(self):
        return self.product.get_info()


class SizeDecorator(ProductDecorator):
    def __init__(self, product, size):
        super().__init__(product)
        self.size = size

    def get_info(self):
        return f'{self.product.get_info()} - Size: {self.size}'


class ColorDecorator(ProductDecorator):
    def __init__(self, product, color):
        super().__init__(product)
        self.color = color

    def get_info(self):
        return f'{self.product.get_info()} - Color: {self.color}'


class MaterialDecorator(ProductDecorator):
    def __init__(self, product, material):
        super().__init__(product)
        self.material = material

    def get_info(self):
        return f'{self.product.get_info()} - Material: {self.material}'


def main():
    product = Product("Shirt", 20)
    product = SizeDecorator(product, "Medium")
    product = ColorDecorator(product, "Blue")
    product = MaterialDecorator(product, "Cotton")
    print(product.get_info())
    # Output: Shirt - $20 - Size: Medium - Color: Blue - Material: Cotton


if __name__ == '__main__':
    main()
