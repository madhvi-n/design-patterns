"""
The Adapter pattern is a structural design pattern that allows you to adapt the interface of one class to match the interface of another class. This can be useful in situations where you need to integrate two incompatible classes or libraries together.
"""

class Adaptee:
    def specific_request(self):
        return "Specific request."

class Target:
    def request(self):
        pass

class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        return self.adaptee.specific_request()


def main():
    # usage
    adaptee = Adaptee()
    target = Adapter(adaptee)
    print(target.request()) # Output: Specific request.


if __name__ == '__main__':
    main()
