import random
from Card import *


class Deck:
    def __init__(self):
        self.cards = []
        self.fill_deck()
        self.shuffle()

    def fill_deck(self):
        for suit in range(1, 5):
            for _ in range(13):
                self.cards.append(Card(_ % 13 + 1, suit))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def print_deck(self):
        for card_ in self.cards:
            card_.print_card()


if __name__ == "__main__":
    deck1 = Deck()
    deck1.print_deck()
