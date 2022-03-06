class Card:
    """
    Card class.

    # Doctests for str and repr
    >>> card_1 = Card("A", "spades")
    >>> print(card_1)
    ____
    |A  |
    | ♠ |
    |__A|
    >>> card_1
    (A, spades)
    >>> card_2 = Card("K", "spades")
    >>> print(card_2)
    ____
    |K  |
    | ♠ |
    |__K|
    >>> card_2
    (K, spades)
    >>> card_3 = Card("A", "diamonds")
    >>> print(card_3)
    ____
    |A  |
    | ♦ |
    |__A|
    >>> card_3
    (A, diamonds)

    # Doctests for comparisons
    >>> card_1 < card_2
    False
    >>> card_1 > card_2
    True
    >>> card_3 > card_1
    False

    # Doctests for set_visible()
    >>> card_3.set_visible(False)
    >>> print(card_3)
    ____
    |?  |
    | ? |
    |__?|
    >>> card_3
    (?, ?)
    >>> card_3.set_visible(True)
    >>> print(card_3)
    ____
    |A  |
    | ♦ |
    |__A|
    >>> card_3
    (A, diamonds)
    """

    # Class Attribute(s)

    def __init__(self, rank, suit, visible=True):
        """
        Creates a card instance and asserts that the rank and suit are valid.
        """
        assert isinstance(rank, int) | isinstance(rank, str)
        self.rank = rank
        self.suit = suit
        self.visible = visible

    def __lt__(self, other_card):
        self.other_card = other_card
        jack_val = 11
        queen_val = 12
        king_val = 13
        ace_val = 14
        club_val = 1
        dia_val = 2
        heart_val = 3
        spade_val = 4
        if isinstance(self.rank, str):
            if self.get_rank() == 'J':
                c1 = 11
            elif self.get_rank() == 'Q':
                c1 = 12
            elif self.get_rank() == 'K':
                c1 = 13
            elif self.get_rank() == 'A':
                c1 = 14
        else:
            c1 = self.rank
            
        if isinstance(self.other_card.rank, str):
            if self.other_card.get_rank() == 'J':
                c2 = 11
            elif self.other_card.get_rank() == 'Q':
                c2 = 12
            elif self.other_card.get_rank() == 'K':
                c2 = 13
            elif self.other_card.get_rank() == 'A':
                c2 = 14
        else:
            c2 = self.other_card.rank
        
        if self.get_suit() == 'clubs':
            c1_suit = club_val
        elif self.get_suit() == 'diamonds':
            c1_suit = dia_val
        elif self.get_suit() == 'hearts':
            c1_suit = heart_val
        elif self.get_suit() == 'spades':
            c1_suit = spade_val
            
        if self.other_card.get_suit() == 'clubs':
            c1_suit = club_val
        elif self.other_card.get_suit() == 'diamonds':
            c2_suit = dia_val
        elif self.other_card.get_suit() == 'hearts':
            c2_suit = heart_val
        elif self.other_card.get_suit() == 'spades':
            c2_suit = spade_val
                
        if c1 < c2:
            return True
        elif c1 > c2:
            return False
        else:
            if c1_suit < c2_suit:
                return True
            else:
                return False


    def __str__(self):
        """
        Returns ASCII art of a card with the rank and suit. If the card is
        hidden, question marks are put in place of the actual rank and suit.

        Examples:
        ____
        |A  |
        | ♠ |
        |__A|
        ____
        |?  |
        | ? |
        |__?|             
        """
        if self.get_suit() == 'clubs':
            suit_icon = '♣'
        elif self.get_suit() == 'diamonds':
            suit_icon = '♦'
        elif self.get_suit() == 'hearts':
            suit_icon = '♥️'
        elif self.get_suit() == 'spades':
            suit_icon = '♠'
            
        if self.visible == False:
            return "____" + "\n" + \
            "|?  |" + "\n" + \
            "| ? |" + "\n" + \
            "|__?|"
        else:
            return "____" + "\n" + \
            "|" + self.get_rank() + "  |" + "\n" + \
            "| " + suit_icon + " |" + "\n" + \
            "|__" + self.get_rank() + "|"
            
    def __repr__(self):
        """
        Returns (<rank>, <suit>). If the card is hidden, question marks are
        put in place of the actual rank and suit.           
        """        
        if self.visible == True:
            return "(" + str(self.get_rank()) + ", " + self.get_suit() + ")"
        else:
            return "(?, ?)"

    def get_rank(self):
        return self.rank
    
    def get_suit(self):
        return self.suit

    def set_visible(self, visible):
        self.visible = visible 
    
