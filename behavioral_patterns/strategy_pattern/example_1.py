from abc import ABC, ABCMeta, abstractmethod


class Strategy(metaclass=ABCMeta):
    """ Sorting strategy interface"""

    @abstractmethod
    def sort(self) -> None:
        ...

    @staticmethod
    @abstractmethod
    def __repr__(self) -> str:
        ...


class BubbleSort(Strategy):
    """ Algorithm which uses bubble sort"""

    def sort(self, arr: list):
        print(arr)

        for i in range(len(arr)):
            for j in range(0, len(arr) - i - 1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

        print(arr)


    def __repr__(self):
        return f"Bubble sort [O(n*n)]"


class HybridSort(Strategy):
    """ Algorithm which uses python inbuilt sort() method"""

    def sort(self, arr: list):
        print(arr)
        arr.sort()
        print(arr)

    def __repr__(self):
        return f"Hybrid sort [O(logn)]"


class Sorting:

    def __init__(self, strategy: Strategy = None) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def sort_values(self, arr) -> None:
        self._strategy.sort(arr)


def main():
    p = Sorting(BubbleSort())
    print("Client: Strategy is set to use bubble sort")
    p.sort_values([2, 4, 3, 1, 6, 9, 8])

    print(f"\nClient: Strategy is set to use hybrid sort")
    p.strategy = HybridSort()
    p.sort_values([2, 4, 3, 1, 6, 9, 8])


if __name__ == '__main__':
    main()
