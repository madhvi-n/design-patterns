from abc import ABCMeta, abstractmethod

class Context():
    "This is the object whose behavior will change"
    @staticmethod
    def strategy(strategy):
        #The strategy is handled by the class passed in
        return strategy()


class IStrategy(metaclass=ABCMeta):
    "A strategy Interface"
    @staticmethod
    @abstractmethod
    def __str__():
        "Implement the __str__ dunder"


class ConcreteStrategyA(IStrategy):
    "A Concrete Strategy Subclass"
    def __str__(self):
        return "I am ConcreteStrategyA"


class ConcreteStrategyB(IStrategy):
    "A Concrete Strategy Subclass"
    def __str__(self):
        return "I am ConcreteStrategyB"


class ConcreteStrategyC(IStrategy):
    "A Concrete Strategy Subclass"
    def __str__(self):
        return "I am ConcreteStrategyC"


def main():
    # The Client
    c = Context()
    print(c.strategy(ConcreteStrategyA))
    print(c.strategy(ConcreteStrategyB))
    print(c.strategy(ConcreteStrategyC))


if __name__ == '__main__':
    main()
