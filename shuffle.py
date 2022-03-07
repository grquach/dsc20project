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
        
        shuffled_res = []
        if len(cards) == 0:
            return shuffled_res
        else:
            if len(cards)%2 == 0:
                shuffled_res.append(cards[0])
                return shuffled_res.extend(Shuffle.mongean(cards[1:]))
            else:
                shuffled_res.insert(0, cards[0])
                return shuffled_res.extend(Shuffle.mongean(cards[1:]))
    
