import random


class Card:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:

    def __init__(self):
        self.deck = [[suit, value] for suit in Card.suits for value in Card.values]

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def count(self):
        return len(self.deck)

    def _deal(self, number):
        try:
            x = 0
            while x < number:
                self.deck.pop()
                x += 1
        except IndexError:
            return "All cards have been dealt"

    def shuffle(self):
        (random.shuffle(self.deck))
        return self.deck

    def deal_card(self):
        return self.deck[random.randint(0, 52)]

    def deal_hand(self, number):
        x = 0
        lst = []
        while x < number:
            lst.append(random.choice(self.deck))
            x += 1
        return lst
