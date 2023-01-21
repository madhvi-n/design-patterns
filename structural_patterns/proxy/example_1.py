"""
The Proxy pattern is a structural design pattern that allows you to provide a surrogate or placeholder object for another object, in order to control access to that object. This can be useful in situations where you need to add additional functionality to an existing object, such as caching, security, or lazy initialization.
"""

class Subject:
    def request(self):
        pass

class RealSubject(Subject):
    def request(self):
        return "Real Subject"

class Proxy(Subject):
    def __init__(self):
        self.real_subject = RealSubject()

    def request(self):
        return self.real_subject.request()


def main():
    # usage
    proxy = Proxy()
    print(proxy.request()) # Output: Real Subject


if __name__ == '__main__':
    main()
