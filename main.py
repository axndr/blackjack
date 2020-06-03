from pip._vendor.distlib.compat import raw_input

from Hand import *
from pyfiglet import Figlet
import time


"""
NOTES:
# SPLIT
# DOUBLE
#


FIXED:
# DEALER'S VALUE NEEDS TO ONLY BE SECOND CARD UNTIL END
! DEALER'S VALUE SHOULD BE DISPLAYED AGAINST PLAYER'S
# NEW LINE AFTER PLAYER BUSTS/BLACKJACK/ECT AND HIT/STAND
# DEALER LOOPS ON A 19
# DEALER'S VALUE SET TO ZERO BY END OF GAME PROB

"""


def clear_screen():
    for _ in range(45):
        print("\n")


def hit(hand_, deck_):
    hand_.cards.append(deck_.cards.pop(0))


def deal_two(deck_) -> list:
    dealt = [deck_.cards.pop(0), deck_.cards.pop(0)]
    return dealt


def natural_check(hand) -> bool:
    if hand.cards[0].face == 1 and hand.cards[1].value == 10:
        return True
    elif hand.cards[1].face == 1 and hand.cards[0].value == 10:
        return True
    else:
        return False


def split_check(hand) -> bool:
    if hand.cards[0].face == hand.cards[1].face and player_hand.money >= hand.round_bet:
        user_input = input("Would you like to split? [Y/N] ".upper())
        if user_input.upper() == "Y" or user_input.upper() == "YES":
            return True
        elif user_input.upper() == "N" or user_input.upper() == "NO":
            return False
    else:
        return False


def double_down_check(hand) -> bool:
    if hand.cards[0].value + hand.cards[1].value in [9, 10, 11] and player_hand.money >= hand.round_bet:
        user_input = input("Would you like to double down? [Y/N] ".upper())
        if user_input.upper() == "Y" or user_input.upper() == "YES":
            return True
        elif user_input.upper() == "N" or user_input.upper() == "NO":
            return False
    else:
        return False


def black_jack_round(hand, deck):
    """
    Plays one round of Black Jack
    :param hand:
    :return: score as int
    """
    while True:
        hand.update_value()
        # clear_screen()  # Clear Screen
        hand.print_hand()
        print("`````````````````````````````````````````````")

        if hand.value == 21:
            print("{name} HITS BLACKJACK!\n".format(name=hand.name).upper())
            print("`````````````````````````````````````````````")
            time.sleep(1)
            break
        elif hand.value > 21:
            print("{name} BUSTS!\n".format(name=hand.name).upper())
            print("`````````````````````````````````````````````")
            time.sleep(1)
            break
        elif hand.value < 21:
            user_input = input("{name} HIT OR STAND? [H/S] ".format(name=hand.name))
            if user_input[0].upper() == "H":
                # deck.cards.insert(0, Card())
                hit(hand, deck)
            elif user_input.upper()[0] == "S":
                print("\n{name} STANDS WITH {value}\n".format(name=hand.name, value=hand.value).upper())
                print("`````````````````````````````````````````````")
                time.sleep(1)
                break


def discard_to_deck(deck, hand):
    for _ in range(len(hand.cards)):
        deck.cards.append(hand.cards.pop(0))


def dealer_round(hand, deck):
    """
    Plays one round of Black Jack for dealer
    :param hand:
    :return: score as int
    """
    hand.print_hand_dealer_start()
    time.sleep(.5)

    while True:
        # clear_screen()  # Clear Screen
        hand.update_value()
        hand.print_hand()
        time.sleep(1)
        print("`````````````````````````````````````````````")
        if hand.value == 21:
            print("{name} HITS BLACKJACK!\n".format(name=hand.name).upper())
            print("`````````````````````````````````````````````")
            break
        elif hand.value > 21:
            print("{name} BUSTS!\n".format(name=hand.name).upper())
            print("`````````````````````````````````````````````")
            break
        elif hand.value < 21:
            if hand.value < 17:
                print("{name} HITS!\n".format(name=hand.name).upper())
                hit(hand, deck)
            elif hand.value >= 17:
                print("{name} STANDS WITH {value}\n".format(name=hand.name, value=hand.value).upper())
                print("`````````````````````````````````````````````")
                break


while True:  # Initiate game play loop
    f = Figlet(font="roman",)
    print("\n")
    print(f.renderText("BLACKJACK"))

    # """ # Testing Code
    user_name = "PLAYER"
    # user_name = raw_input("WHAT IS YOUR NAME? [str] ") or "PLAYER"
    # user_input = "Y"  # Testing Code
    while True:
        user_input = input("{}, would you like to play Black Jack? [Y/N] ".format(user_name))
        if user_input.upper() == "Y" or user_input.upper() == "YES":
            play = True
            break
        elif user_input.upper() == "N" or user_input.upper() == "NO":
            play = False
            break
        else:
            continue
    print("`````````````````````````````````````````````")

    """
    
    user_input = ""
    
    # """  # Testing Code

    play = True
    player_hand = Hand(name=user_name[:7].ljust(7, " ").upper())
    deck = Deck()

    while play:

        pot = 0

        # Test Code
        # deck.cards.insert(0, Card())  # Ace
        # deck.cards.insert(0, Card(2, 1))  # Jack

        player_hand.cards.append(deck.cards.pop(0))
        player_hand.cards.append(deck.cards.pop(0))

        dealer_hand = Hand(deal_two(deck), "DEALER ")

        player_hand.update_value()

        pot += player_hand.ante(2)
        pot = player_hand.bet(pot)

        Hand.wait_w_prompt("DEALING")
        print("`````````````````````````````````````````````")

        dealer_hand.print_hand_dealer_start()

        """  # Split and Double Down not implemented yet
        if split_check(player_hand):
            player_split = [player_hand]
            player_split.append(Hand(player_split[0].cards.pop(1)))
        if double_down_check(player_hand):
            pass
        """

        p_nat = natural_check(player_hand)
        d_nat = natural_check(dealer_hand)

        if p_nat or d_nat:
            player_hand.print_hand()
        else:
            black_jack_round(player_hand, deck)
            dealer_round(dealer_hand, deck)

        if p_nat and not d_nat:
            player_hand.money += player_hand.round_bet * 1.5
            print("YOU WON {} COINS WITH A NATURAL BLACKJACK\n".format(player_hand.round_bet * 1.5))
        elif p_nat and d_nat:
            player_hand.money += player_hand.round_bet
            print("YOU AND THE DEALER BOTH HAD NATURALS, YOUR {} COIN BET IS RETURNED\n".format(player_hand.round_bet))
        elif d_nat and not p_nat:
            print("THE DEALER HAD A NATURAL BLACKJACK\n")
        elif dealer_hand.value < player_hand.value <= 21 or player_hand.value <= 21 < dealer_hand.value:
            player_hand.money += player_hand.round_bet * 2
            print("YOU WON WITH {value} AND WON {round_bet} COINS!\n".format(value=player_hand.value, round_bet=player_hand.round_bet * 2))
        elif player_hand.value < dealer_hand.value <= 21 or dealer_hand.value <= 21 < player_hand.value:
            print("THE DEALER WAS THE WINNER WITH {value}!\n".format(value=dealer_hand.value))
        elif 21 < dealer_hand.value <= player_hand.value:
            print("YOU BOTH BUST\n")
        elif dealer_hand.value == player_hand.value:
            player_hand.money += player_hand.round_bet
            print("YOU PUSHED, YOUR {} COIN BET IS RETURNED\n".format(player_hand.round_bet))
        print("`````````````````````````````````````````````")

        # print(player_hand.value, dealer_hand.value)  # Test Code

        discard_to_deck(deck, player_hand)
        discard_to_deck(deck, dealer_hand)
        deck.shuffle()

        while True:
            if player_hand.money == 0:
                user_input = input("Would you like to buy in with another 100 coins? [Y/N] ")
                if user_input.upper() == "Y" or user_input.upper() == "YES":
                    player_hand.money = 100
                    play = True
                    break
                elif user_input.upper() == "N" or user_input.upper() == "NO":
                    play = False
                    break
            else:
                while True:
                    user_input = input("Would you like to play again? [Y/N] ")
                    if user_input.upper() == "Y" or user_input.upper() == "YES":
                        play = True
                        print("`````````````````````````````````````````````")
                        break
                    elif user_input.upper() == "N" or user_input.upper() == "NO":
                        play = False
                        print("`````````````````````````````````````````````")
                        break
                break

    else:
        print("See you later!")
        break

