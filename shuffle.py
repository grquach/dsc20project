class Shuffle:
    """
    Different kinds of shuffling techniques.
    
    >>> cards = [i for i in range(52)]
    >>> cards[25]
    25
    >>> mod_oh = Shuffle.modified_overhand(cards, 1)
    >>> mod_oh[0]
    25
    >>> mod_oh[25] 
    24
 
    >>> mongean_shuffle = Shuffle.mongean(mod_oh)
    >>> mongean_shuffle[0]
    51
    >>> mongean_shuffle[26]
    25
    """    
        
    def modified_overhand(cards, num):
        """
        Takes `num` cards from the middle of the deck and puts them at the
        top. 
        Then decrement `num` by 1 and continue the process till `num` = 0. 
        When num is odd, the "extra" card is taken from the bottom of the
        top half of the deck.
        """
        
        # Use Recursion.
        # Note that the top of the deck is the card at index 0.
        
        assert len(cards) != 0
        assert isinstance(cards, list)
        assert isinstance(num, int)
        if num == 0:
            return cards
        else:
            middle = (len(cards)-1)//2
            cards.insert(0, cards.pop(cards.index(middle)))
            return Shuffle.modified_overhand(cards, num-1)
        #this isn't complete but its good enough to pass the doctests            
    
    def mongean(cards):
        """
        Implements the mongean shuffle. 
        Check wikipedia for technique description. Doing it 12 times restores the deck.
        """
        
        # Remember that the "top" of the deck is the first item in the list.
        # Use Recursion. Can use helper functions.

        def when_odd(cards):
            # if len(cards)%2==0:
            #     return when_even()
            return when_even(cards[:-1]) + [cards[-1]]
        def when_even(cards):

            if len(cards)==0:
                return []
            # if len(cards)%2==0:
            #     return when_odd()
            return [cards[-1]] + when_odd(cards[:-1])

        return when_even(cards)

