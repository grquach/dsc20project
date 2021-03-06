"""
DSC 20 Project
Names:  Gregory Quach,  Nathen Lee
PID:    A16959667,      A16938397
"""

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
            cut = 2
            one_side = (len(cards)-num)//cut
            if num%2==len(cards)%2:
                temp = cards[one_side: -one_side]
                del cards[one_side: -one_side]
                cards = temp + cards
                return Shuffle.modified_overhand(cards, num-1)
            else:
                temp = cards[one_side: -(one_side+1)]
                del cards[one_side: -(one_side+1)]
                cards = temp + cards
                return Shuffle.modified_overhand(cards, num-1)           
    
    def mongean(cards):
        """
        Implements the mongean shuffle. 
        Check wikipedia for technique description. Doing it 12 times restores the deck.
        """
        
        # Remember that the "top" of the deck is the first item in the list.
        # Use Recursion. Can use helper functions.
        
        def when_odd(cards):
            return when_even(cards[:-1]) + [cards[-1]]
            
        def when_even(cards):
            if len(cards)==0:
                return []
            if len(cards)%2==1:
                return when_odd(cards)
            return [cards[-1]] + when_odd(cards[:-1])

        return when_even(cards)
