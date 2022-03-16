"""
DSC 20 Project
Names:  Gregory Quach,  Nathen Lee
PID:    A16959667,      I'm not sure
"""

from card import Card
from hand import PlayerHand, DealerHand
from shuffle import Shuffle

class Deck:
    """
    Card deck of 52 cards.

    >>> deck = Deck()
    >>> deck.get_cards()[:5]
    [(2, clubs), (2, diamonds), (2, hearts), (2, spades), (3, clubs)]

    >>> deck.shuffle(modified_overhand=2, mongean=3)
    >>> deck.get_cards()[:5]
    [(A, clubs), (Q, clubs), (10, clubs), (7, diamonds), (5, diamonds)]

    >>> hand = PlayerHand()
    >>> deck.deal_hand(hand)
    >>> deck.get_cards()[0]
    (Q, clubs)
    """

    # Class Attribute(s)

    def __init__(self):
        """
        Creates a Deck instance containing cards sorted in ascending order.
        """
        ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        suits = ['clubs', 'diamonds', 'hearts', 'spades']
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]

    def shuffle(self, **shuffle_and_count):
        """Shuffles the deck using a variety of different shuffles.

        Parameters:
            shuffle_and_count: keyword arguments containing the
            shuffle type and the number of times the shuffled
            should be called.
        """
        try:
            num_modified_overhand = shuffle_and_count['modified_overhand']
        except:
            num_modified_overhand = 0
        try:
            num_mongean = shuffle_and_count['mongean']
        except:
            num_mongean = 0
        self.cards = Shuffle.modified_overhand(self.cards, num_modified_overhand)
        for j in range(num_mongean):
            self.cards = Shuffle.mongean(self.cards)

    def deal_hand(self, hand):
        """
        Takes the first card from the deck and adds it to `hand`.
        """
        self.hand = hand
        assert isinstance(self.hand, PlayerHand)
        self.hand.add_card(self.cards[0])
        self.cards.pop(0)

    def get_cards(self):
        return self.cards
