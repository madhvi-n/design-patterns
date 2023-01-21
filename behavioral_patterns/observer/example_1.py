"""
The Observer pattern is a design pattern where an object, called the subject, maintains a list of its dependents, called observers, and notifies them automatically of any changes to its state. The observer pattern is often used in event-driven systems, such as user interfaces, where changes to the state of one object can trigger updates in other objects.
"""

from abc import ABC, ABCMeta


class Subject(ABC):
    __metaclass__ = ABCMeta

    def __init__(self):
        self._observers = set()

    def attach(self, observer):
        self._observers.add(observer)

    def detach(self, observer):
        self._observers.discard(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)


class Observer(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self, subject):
        pass


class ConcreteSubject(Subject):
    def __init__(self):
        super().__init__()
        self._state = None

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
        self.notify()


class ConcreteObserverA(Observer):
    def update(self, subject):
        print(f'ConcreteObserverA: {subject.state}')


class ConcreteObserverB(Observer):
    def update(self, subject):
        print(f'ConcreteObserverB: {subject.state}')


def main():
    subject = ConcreteSubject()

    observerA = ConcreteObserverA()
    subject.attach(observerA)

    observerB = ConcreteObserverB()
    subject.attach(observerB)

    subject.state = 'Hello'
    # ConcreteObserverA: Hello
    # ConcreteObserverB: Hello

    subject.detach(observerA)

    subject.state = 'World'
    # ConcreteObserverB: World


if __name__ == '__main__':
    main()
