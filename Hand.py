from Deck import *
import time


class Hand:
    def __init__(self, cards_dealt=[], name="PLAYER", dealer=False, money=100):
        self.cards = []
        for card_ in cards_dealt:
            self.cards.append(card_)
        self.dealer = dealer
        self.name = name
        self.value = 0
        self.update_value()
        self.money = money
        self.round_bet = 0

    @staticmethod
    def wait_w_prompt(prompt):
        print("\n{}".format(prompt), end="")
        print(".", end="")
        time.sleep(.25)
        print(".", end="")
        time.sleep(.25)
        print(".")
        time.sleep(.25)

    def bet(self, pot) -> int:
        """


        :param pot:
        :return: new pot value
        """
        print("\n{}'s WALLET: {} COINS   CURRENT POT: {} COINS".format(self.name, self.money, pot))
        while True:
            try:
                bet = int(input("WHAT WOULD YOU LIKE TO BET? "))
            except ValueError:
                print("enter a valid bet".upper())
                continue
            if bet > self.money:
                print("You don't have that much money".upper())
                continue
            elif bet < 0:
                print("You can't bet negative coins".upper())
                continue
            else:
                self.money = self.money - bet
                self.round_bet = bet
                pot += bet
                self.wait_w_prompt("BETTING {} COINS".format(bet))
                return pot

    def ante(self, ante) -> int:
        self.money = self.money - ante
        self.round_bet = ante
        self.wait_w_prompt("SUBMITTING {} COIN ANTE".format(ante))
        return ante

    def print_hand(self):
        for _ in range(7):
            print(self.name[_], end=" ")
            for card_ in self.cards:
                print(card_.display[_], end=" ")
            print("")
        print("VALUE: {value: >2}\n".format(value=self.value))

    def print_hand_dealer(self):
        for _ in range(7):
            print(self.name[_], end=" ")
            for card_ in self.cards:
                if card_ == self.cards[0]:
                    print(dealer_card_back[_], end=" ")
                else:
                    print(card_.display[_], end=" ")
            print("")
        print("VALUE: {value: >2}\n".format(value=self.value))

    def print_hand_dealer_start(self):
        for _ in range(7):
            print(self.name[_], end=" ")
            for card_ in self.cards:
                if card_ == self.cards[0]:
                    print(dealer_card_back[_], end=" ")
                else:
                    print(card_.display[_], end=" ")
            print("")
        print("VALUE: {value: >2}\n".format(value=self.cards[1].value))

    def update_value(self):
        self.value = 0
        for card in self.cards:
            if card.face == 1:
                card.value = 0
            self.value += card.value  # value without ace

        hard_ace_in_hand = False
        for card in self.cards:
            if card.face == 1:
                if self.value + 11 <= 21:
                    if hard_ace_in_hand:
                        card.value = 1
                    else:
                        hard_ace_in_hand = True
                        card.value = 11
                elif self.value + 11 > 21:
                    card.value = 1
                self.value += card.value

    def ace_locator(self) -> list:
        """
        Finds where aces are in hand obj, if any
        :return: array of indices of aces in hand
        """
        ace_locations = []
        for card in self.cards:
            if card.face == 1:
                ace_locations.append(self.cards.index(card))


if __name__ == "__main__":
    pass
