"""
In this example, we have a Car class which represents the object we are building. The CarBuilder is an interface that defines the methods that the concrete builders should have. The SportsCarBuilder and SedanCarBuilder are concrete implementations of the CarBuilder interface, they build a car with different characteristics. The Director class is responsible for using the correct builder to construct a car.

This example demonstrates how the Builder pattern allows you to build complex objects step by step, by separating the construction of the object from its representation. The client code can use the Director class to construct a car with the desired characteristics, without having to know the details of how the car is built.
"""


class Car:
    def __init__(self):
        self.__wheels = None
        self.__doors = None
        self.__engine = None

    def set_wheels(self, wheels):
        self.__wheels = wheels

    def set_doors(self, doors):
        self.__doors = doors

    def set_engine(self, engine):
        self.__engine = engine

    def __str__(self):
        return f'{self.__wheels} wheels, {self.__doors} doors, {self.__engine} engine'


class CarBuilder:
    def build_wheels(self):
        pass

    def build_doors(self):
        pass

    def build_engine(self):
        pass

    def get_car(self):
        pass


class SportsCarBuilder(CarBuilder):
    def __init__(self):
        self.car = Car()

    def build_wheels(self):
        self.car.set_wheels(4)

    def build_doors(self):
        self.car.set_doors(2)

    def build_engine(self):
        self.car.set_engine('V8')

    def get_car(self):
        return self.car


class SedanCarBuilder(CarBuilder):
    def __init__(self):
        self.car = Car()

    def build_wheels(self):
        self.car.set_wheels(4)

    def build_doors(self):
        self.car.set_doors(4)

    def build_engine(self):
        self.car.set_engine('V6')

    def get_car(self):
        return self.car


class Director:
    def __init__(self, builder):
        self._builder = builder

    def construct_car(self):
        self._builder.build_wheels()
        self._builder.build_doors()
        self._builder.build_engine()


def main():
    # usage
    director = Director(SportsCarBuilder())
    director.construct_car()
    car = director.builder.get_car()
    print(car) # Output: 4 wheels, 2 doors, V8 engine

    director = Director(SedanCarBuilder())
    director.construct_car()
    car = director.builder.get_car()
    print(car) # Output: 4 wheels, 4 doors, V6 engine


if __name__ == '__main__':
    main()
