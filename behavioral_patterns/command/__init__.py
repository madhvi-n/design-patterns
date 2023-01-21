"""
The Command pattern is a behavioral design pattern that allows you to encapsulate a request or an action as an object, separate from the object that actually performs the action. This allows for greater flexibility and decoupling between the objects involved, as the requestor doesn't need to know the details of how the action is performed.
"""

class Command:
    def execute(self):
        pass

class TurnOnCommand(Command):
    def __init__(self, device):
        self.device = device

    def execute(self):
        self.device.turn_on()

class TurnOffCommand(Command):
    def __init__(self, device):
        self.device = device

    def execute(self):
        self.device.turn_off()

class Device:
    def turn_on(self):
        print("Device is on")

    def turn_off(self):
        print("Device is off")

class RemoteControl:
    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()


def main():
    # usage
    device = Device()

    turn_on_command = TurnOnCommand(device)
    turn_off_command = TurnOffCommand(device)

    remote = RemoteControl()

    remote.set_command(turn_on_command)
    remote.press_button() # Device is on

    remote.set_command(turn_off_command)
    remote.press_button() # Device is off


if __name__ == '__main__':
    main()
