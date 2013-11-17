
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


wordlist = load_words()
chosen_word=choose_word(wordlist)

print "Welcome to the game Hangman!  I am thinking of a word that is " + str(len(chosen_word)) + " letters long"


x="abcdefghijklmnopqrstuvxywz"
i=0
j=0
h=0
d=""
for p in range(len(chosen_word)):
    l="_"
    d=d+l
    g=list(d)

    

while (i<(len(chosen_word))) and len(chosen_word)+2-j>0:
    print " You have " + str(len(chosen_word)+2-j) + " available guesses"
    print "Available letters are : " + x
    a=raw_input('Enter your guess: ')
    j=j+1
    for k in range(len(chosen_word)):
        if a==chosen_word[k]:
            i=i+1
            h=h+1
            x=x.replace(a,"")
            if h==1:
                print "Good Guess"
            g[k]=a
            
    print ''.join(g)
            

                
                    
            
            
            
        
    
        
    
    

if chosen_word==''.join(g):
    print"Congratulations, you won!!"

else:
    print"Sorry you lost The correct answer is " + chosen_word
    print"Run the program again to play"
    
    
        



