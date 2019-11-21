import random

class Card:

    suit_names = ["Spade", "Hearts", "Diamonds", "Clubs"]
    rank_names = [None, "Ace", '2', '3', '4', '5', '6', '7',
            '8','9', '10', "Jack", "Queen", "King"]


    def __init__(self, suit=0,rank=2):
        self.suit = suit
        self.rank = rank


    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2


    def __str__(self):
        return f"{Card.suit_names[self.suit]} of {Card.rank_names[self.rank]}"


class Deck:

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort_cards(self):
        self.cards.sort()

    def move_card(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return "\n".join(res)

class Hand(Deck):

    def __init__(self, label=""):
        self.cards = []
        self.label = label
