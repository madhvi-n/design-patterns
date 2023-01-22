"""
The Mediator pattern is a behavioral design pattern that allows objects to communicate with each other through a mediator object, rather than directly. This pattern is used to reduce the dependencies between objects, and to make the communication between them more flexible and decoupled.
"""


class Mediator:
    def __init__(self):
        self._colleagues = []

    def add_colleague(self, colleague):
        self._colleagues.append(colleague)

    def send(self, message, sender):
        for colleague in self._colleagues:
            if colleague != sender:
                colleague.receive(message)

class Colleague:
    def __init__(self, mediator, name):
        self._mediator = mediator
        self._name = name
        self._mediator.add_colleague(self)

    def send(self, message):
        self._mediator.send(message, self)

    def receive(self, message):
        print(self._name, "received:", message)

def main():
    # Usage
    mediator = Mediator()
    colleague1 = Colleague(mediator, "Colleague 1")
    colleague2 = Colleague(mediator, "Colleague 2")
    colleague3 = Colleague(mediator, "Colleague 3")

    colleague1.send("Hello, colleagues!")
    # Output: "Colleague 2 received: Hello, colleagues!"
    #         "Colleague 3 received: Hello, colleagues!"


if __name__ == '__main__':
    main()
