from abc import ABCMeta, abstractmethod


class GameCharacter():
    "This is the context whose strategy will change"

    def __init__(self, player="P"):
        self.player = player
        self.position = [0, 0]

    def move(self, movement_strategy):
        "The movement algorithm has been decided by the client"
        movement_strategy(self.player, self.position)


class Strategy(metaclass=ABCMeta):
    "A Concrete Strategy Interface for character movement"

    @staticmethod
    @abstractmethod
    def __call__():
        "Implementors must select the default method"


class Walking(Strategy):
    "A Concrete Strategy Subclass"

    @staticmethod
    def walk(player, position):
        "A walk algorithm"
        position[0] += 1
        print(f"{player} is walking. New position = {position}")
    __call__ = walk


class Running(Strategy):
    "A Concrete Strategy Subclass"

    @staticmethod
    def run(player, position):
        "A run algorithm"
        position[0] += 2
        print(f"{player} is running. New position = {position}")
    __call__ = run


class Crawling(Strategy):
    "A Concrete Strategy Subclass"

    @staticmethod
    def crawl(player, position):
        "A crawl algorithm"
        position[0] += 0.5
        print(f"{player} is crawling. New position = {position}")
    __call__ = crawl


def main():
    # The Client
    player = GameCharacter("Lia")
    player.move(Walking())

    # Character sees the enemy
    player.move(Running())

    # Character finds a small cave to hide in
    player.move(Crawling())


if __name__ == '__main__':
    main()
