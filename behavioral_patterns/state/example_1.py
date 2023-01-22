"""
For example, here's an example of how the State pattern can be used to implement a simple state machine for a traffic light:
"""

class TrafficLight:
    def __init__(self):
        self._state = RedLight()

    def request(self):
        self._state.handle()

    def set_state(self, state):
        self._state = state


class State:
    def handle(self):
        pass


class RedLight(State):
    def handle(self):
        print("Red light")


class GreenLight(State):
    def handle(self):
        print("Green light")


class YellowLight(State):
    def handle(self):
        print("Yellow light")


def main():
    # usage
    light = TrafficLight()
    light.request() # prints "Red light"
    light.set_state(GreenLight())
    light.request() # prints "Green light"
    light.set_state(YellowLight())
    light.request() # prints "Yellow light"


if __name__ == '__main__':
    main()
