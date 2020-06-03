face_table = {
                1: "A",
                2: "2",
                3: "3",
                4: "4",
                5: "5",
                6: "6",
                7: "7",
                8: "8",
                9: "9",
                10: "10",
                11: "J",
                12: "Q",
                13: "K"
            }

value_table = {
                1: 0,
                2: 2,
                3: 3,
                4: 4,
                5: 5,
                6: 6,
                7: 7,
                8: 8,
                9: 9,
                10: 10,
                11: 10,
                12: 10,
                13: 10
            }

suit_table = {
                1: "Spades",
                2: "Diamonds",
                3: "Clubs",
                4: "Hearts"
            }

suit_symbol_table = {
                1: '♠',
                2: '♦',
                3: '♣',
                4: '♥',
    }

dealer_card_back = [
                "┌─────────┐",
                "| ░ ░ ░ ░ |",
                "|  ░ ░ ░  |",
                "| ░ ░ ░ ░ |",
                "|  ░ ░ ░  |",
                "| ░ ░ ░ ░ |",
                "└─────────┘"
    ]


class Card:
    def __init__(self, face=1, suit=1):
        self.face = face
        self.value = value_table[face]
        self.suit = suit
        self.display = []
        self.build_display()

    def build_display(self):
        self.display.append("┌─────────┐")
        self.display.append("| {value: >2}      |".format(value=face_table[self.face]))
        self.display.append("│         |")
        self.display.append("│    {suit}    │".format(suit=suit_symbol_table[self.suit]))
        self.display.append("|         |")
        self.display.append("│      {value: <2} │".format(value=face_table[self.face]))
        self.display.append("└─────────┘")

    def print_card(self):
        # ░
        for i in range(7):
            print(self.display[i])


"""
Card A Card B Card C

print( top a    top b   top c   
        a1      b1      
    
for _ in lines         
    for cards in hand
        print(current line (_) of card without nl)
    print(/n)


"""

"""
club    /u2663
spade   /u2660
diamond /u2666
heart   /u2665


"""

if __name__ == "__main__":
    card = Card(1, 1)
    card.print_card()
    print(face_table[card.face], value_table[card.face], card.suit)