from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def consumption(self):
        pass


class Overcoat(Clothes):
    def consumption(self):
        return f'На пальто нужно: {self.param / 6.5 + 0.5 :.2f} ткани'


class Suit(Clothes):
    def consumption(self):
        return f'На костюм нужно: {2 * self.param + 0.3 :.2f} ткани'


overcoat = Overcoat(400)
suit = Suit(55)
print(overcoat.consumption())
print(suit.consumption())
