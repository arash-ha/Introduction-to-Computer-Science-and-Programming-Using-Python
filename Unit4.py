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
Problem 3
"""
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    
    if word not in wordList:
        return False
    hand_new = hand.copy()
    for w in word:
        if hand_new.get(w, 0) > 0:
            hand_new[w] -= 1
        else:
            return False
    return True
"""
-----------------------------------------------------------------------------------------------
Problem 4
"""
def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    handLength = 0
    for w in hand:
      handLength += hand[w]
    return handLength

"""
-----------------------------------------------------------------------------------------------
Problem 5
"""

def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
   # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Keep track of the total score
    total_score=0
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) > 0:
        # Display the hand
        displayHand(hand)
        # Ask user for input
        word = input('Enter word, or a "." to indicate that you are finished: ')
        # If the input is a single period:
        if word == '.':
            # End the game (break out of the loop)

            break
        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if isValidWord(word, hand, wordList) == False: 
                # Reject invalid word (print a message followed by a blank line)
                print('Invalid word, please try again.')
                print()
                
            # Otherwise (the word is valid):
            else:   
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                
                score = getWordScore(word, n)
                total_score += score
                print(word, "earned", score, "points. Total:", total_score, "points")
                print()
                # Update the hand 
                hand = updateHand(hand, word)

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if calculateHandlen(hand) > 0:
        print('Goodbye! Total score:', ' ', total_score, ' ', 'points.')
    else:
        print('Run out of letters. Total score:', total_score, 'points.')

       
    
"""
-----------------------------------------------------------------------------------------------
Problem 6
"""

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1
    """
    # TO DO ... <-- Remove this comment when you code this function

    n = HAND_SIZE
    hand = {}

    while True:  
        cmd = input('Enter n to deal a new hand, r to replay the last hand, or e to end game:')
        if cmd == 'r':
            if not hand:
                print("You have not played a hand yet. Please play a new hand first!")
            else:
                playHand(hand, wordList, n)
        elif cmd == 'n':
            hand = dealHand(n)
            playHand(hand, wordList, n)
        elif cmd == 'e':
            break
        else:
            print ("Invalid command.")
