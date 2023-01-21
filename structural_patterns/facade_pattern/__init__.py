"""
The Facade pattern is a structural design pattern that provides a simplified interface to a complex system of classes or libraries. It acts as a "facade" in front of the complex system, hiding its complexity and providing a single, easy-to-use interface for the client code.
"""

class SubsystemA:
    def operation_a(self):
        return "Subsystem A"

class SubsystemB:
    def operation_b(self):
        return "Subsystem B"

class Facade:
    def __init__(self):
        self.subsystem_a = SubsystemA()
        self.subsystem_b = SubsystemB()

    def operation(self):
        return f'{self.subsystem_a.operation_a()} + {self.subsystem_b.operation_b()}'

def main():
    # usage
    facade = Facade()
    print(facade.operation()) # Output: Subsystem A + Subsystem B


if __name__ == '__main__':
    main()
