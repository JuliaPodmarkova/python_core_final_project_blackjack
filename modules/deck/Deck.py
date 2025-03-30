import random

from modules.card.Card import Card

class Deck:
    SUITS = ["clubs", "diamonds", "hearts", "spades"]
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    VALUES = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
              "J": 10, "Q": 10, "K": 10, "A": 11}

    def __init__(self):
        self.cards = [Card(suit, rank, Deck.VALUES[rank]) for suit in Deck.SUITS for rank in Deck.RANKS]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if self.cards:
            return self.cards.pop()
        else:
            return None