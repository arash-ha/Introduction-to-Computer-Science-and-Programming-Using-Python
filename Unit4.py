"""
Problem 1
"""
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    # TO DO ... <-- Remove this comment when you code this function

    count=0
    scoreall=0
    scoreword=0
    if word=='':
       return scoreall
    else:
        for char in word:
            scoreword=SCRABBLE_LETTER_VALUES[char]
            scoreall=scoreall+scoreword
        return scoreall*len(word)+(50 if (len(word)==n and count==0) else 0)   
    count+=1
"""
-----------------------------------------------------------------------------------------------
"""
"""
Problem 2
"""
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ... <-- Remove this comment when you code this function
    
    hand_new = hand.copy()
    for w in word:
        hand_new[w] -= 1
    return hand_new
"""
-----------------------------------------------------------------------------------------------
"""

