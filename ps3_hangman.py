# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    value1 = bool
    splitWord = [char for char in secretWord]
    for each in splitWord:
        if each in lettersGuessed:
            value1 = True
        elif each not in lettersGuessed:
            value1 = False
            break
    return value1



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    final = ""
    present = [each for each in lettersGuessed if each in secretWord]
    for letter in secretWord:
        if letter not in present:
            final = final+("_ ")
        elif letter in present:
            final = final + (letter)
    return final
# return ''.join(letter for letter in secretWord if letter in present else if letter not in secretWord letter = "_")

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    alpha = string.ascii_lowercase
    final = ''
    for each in alpha:
        if each not in lettersGuessed:
            final = final + each
    return final
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...

    wordlen = len(secretWord)
    print("Welcome to hangman!\n"+
          "\nThe word I'm thinking of is "+str(wordlen)+" letters long")
    lettersGuessed = []
    nRound = 1
    while nRound < 27:
    
        letterGuess = input("Please guess a new letter for guess number "+str(nRound))
        if letterGuess in lettersGuessed:
            print("You already used this!")
        else:
            
            lettersGuessed.append(letterGuess)
            print(getGuessedWord(secretWord, lettersGuessed))
            print("letters left: "+(getAvailableLetters(lettersGuessed)))
            if "_" not in getGuessedWord(secretWord, lettersGuessed):
                print("Congrats you got it!")
                nRound = 27
            else:
                nRound += 1
                
            
    




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
