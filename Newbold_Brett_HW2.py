# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 19:13:22 2016

Group D

@author: bnew
"""

#1


import string # Allows us to use string.punctuation

filename = input('Enter the file name: ') # Asks the user to enter a file name

disregard = string.punctuation + " " # string.punctuation will gather punctuation 
                                     # characters so we disregard them later
                                     # along with spaces 

def is_palindrome(file):
    """
    This function, is_palindrome() accepts a file from the user, reads each line,
    and prints the line to the screen if it is a palindrome.

    Parameters: 
    file - file provided by user

    Returns:
    palindromes if it is indeed one
    
    bn-2016
    """
    
    refined = [x for x in file.lower() if x not in disregard]
    # List comprehension that creates a new string (refined) that collects 
    # characters from the file after making them lower case. However, if x is 
    # found in disregard, it, wait for it... gets disregarded
    
    if refined == refined[::-1]: # If this newly refined string is equal to
                                 # itself in reverse order then return true
        return True

with open(filename, 'r') as f: 
        # Use "with" keyword so that the file is properly closed after the 
        # following indented lines. open() returns a file object, the mode 'r'
        # is used since filename will only be read
    
    for line in f:

        if is_palindrome(line.rstrip()): 
        # rstrip() returns a copy of each line in the file after stripping
        # the default whitespace characters at the end of the string. After
        # our function is_palindrome decides if it is a palindrome, if it is
        # we print the line
        
            print(line.rstrip()) 
    
    
    
#2

def semordnilap(file):
    """
    This function, semordnilap() accepts a file from the user(pointing to a 
    list of words) from the user and finds and prints all pairs of words that 
    are semordnilaps to the screen. A semordnilap is a word or phrase that spells 
    a different word or phrase backwards. ("Semordnilap" is itself "palindromes" 
    spelled backwards.)

    Parameters: 
    file - file provided by user 

    Returns:
    semordnilaps if it is indeed one
    
    bn-2016
    """

    f = open(file).read() # Opens file and returns a string containing all 
    # characters in the file, stores the string as f 
    
    lines = f.split('\n') # split spearates the string f based on the specified
    # delimiter (newline)
    
    while lines: # will keep executing as long as boolean is True
        x = lines[0] # x is assigned as the first entry from the list lines
        lines.remove(x) # removes the first entry from the list lines and recreates
        # lines without first entry
        
        if x[::-1] in lines: # if its reversed string is found in the remainder
        # of the entries we will print both to the screen
        
            print (x + ' and ' + x[::-1] + ' are semordnilaps')

# Test using a txt file                
semordnilap('/Users/bnew/GitHub/Newbold_Brett_python/test.txt')
    
    
    
#3
    
   
def char_freq_table():
    """
    This function, char_freq_table() accepts a file name from the user, builds 
    a frequency listing of the characters contained in the file, and prints a
    sorted and nicely formatted character frequency table to the screen.

    Parameters: 
    file - string inputted by the user 

    Returns:
    frequency list of the characteres in the file
    
    bn-2016
    """  
    file = input('Enter the filename: ') # allows user to input a filename
    
    d = dict() # creating an empty dictionary to store frequencies 
    
    for char in open(file,'r').read(): # for each character found in the file
    
        d[char] = d.get(char,0) + 1 # creates the definition in our dictionary
         # the character that is found in the file is placed on the left side 
         # of definition and get() returns the value of the given key, for every 
         # occurence it will add one to its value 
        
    return d # returns the dictionary at the end of for loop
 
print(char_freq_table())



#4

import time # to use time.sleep()
import os # to use os.system()
from string import punctuation

d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 
	 'f':'foxtrot', 'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 
	 'k':'kilo', 'l':'lima', 'm':'mike', 'n':'november', 'o':'oscar', 
	 'p':'papa', 'q':'quebec', 'r':'romeo', 's':'sierra', 't':'tango', 
	 'u':'uniform', 'v':'victor', 'w':'whiskey', 'x':'x-ray', 'y':'yankee', 
	 'z':'zulu'}

def speak_ICAO(text, ICAOpause = 1, WORDpause = 1):
    """
    This function, speak_ICAO() is able to translate any text (i.e. any string)
    into spoken ICAO words.

    Parameters: 
    text - string
    ICAOpause - float indicating the length of the pause between each spoken 
    ICAO word (initialized to be 1 second)
    WORDpause - float indicating the length of the pause between each word
    spoken (initialized to be 1 second)
     
    Returns:
    spoken ICAO words
    
    bn-2016
    """

    wordList = text.split() # Returns a list of the words in the string (text)

    for word in wordList: 
        for c in word: # For every character in each word from text
            if c not in punctuation: 
            # If the character is not considered a punctuation character
                os.system('say ' + d[c.lower()])
                # c.lower() will make the character lowercase so the dictionary
                # can find it. The mac will then speak the value of that char
                # from the dictionary (ICAO word)
                
                time.sleep(ICAOpause) # delays for that many seconda between letters
        time.sleep(WORDpause) # delays for that many seconds between words
                # user can input their own value for these parameters when using
                # the function, if not the default is 1 second


# 5

def hapax(file):
    """
    This function, hapax(), takes a file and returns all of its hapaxes while 
    ignoring capitalization. A hapax legomenon (often abbreviated to hapax) is 
    a word which occurs only once in either the written record of a language, 
    the works of an author, or in a single text.

    Parameters: 
    file - file inputted by the user
     
    Returns:
    hapaxes if the file has any
    
    bn-2016
    """

    wordList = [] # Creates an empty list

    with open(file, 'r') as f:
    # Use "with" keyword so that the file is properly closed after the 
    # following indented lines. open() returns a file object, the mode 'r'
    # is used since filename will only be read 
    
        for line in f:
            
            wordList += line.lower().split()
            # split() returns a list of words from the line while lower() 
            # ensures we are taking the characters to be lowercase. Our wordList
            # will keep building on itself

    hapaxes = [x for x in wordList if wordList.count(x) == 1]
    # Now that we've built a list we can use a list comprehension to create our 
    # hapaxes by seeking out words (x) in the wordList whose count equals 1 
    # (if they occur once)
    
    return hapaxes



# 6


def numbered(file):
    """
    This function, numbered(), takes a given text file and creates a new text
    file in which all the lines from the original file are numbered from 1 to n
    (where n is the number of lines in the file)

    Parameters: 
    file - string
     
    Returns:
    new text file with numbered lines
    
    bn-2016
    """

    with open(file, 'r') as f1:
    # Use "with" keyword so that the file is properly closed after the 
    # following indented lines. open() returns a file object, the mode 'r'
    # is used since f1 will only be read 
    
        with open(file, 'w') as f2:
        # f2 is named as a new file, indicating it will be "numbered", the mode
        # 'w' is used since f2 will be opened for writing
            
            for num, str in enumerate(f1, start=1):
            # enumerate() is a built in function that returns tuples with a 
            # count starting at 1 and string values obtained from iterating 
            # over f1 
            
                f2.write('%d %s' % (num, str))
                # takes our tuples and outputs their numbers and strings without
                # parentheses


#7


import re # import regular expressions

def avg_word_length(file):
    """
    This function, avg_word_length(), calculates the average word length of 
    a text stored in a file (i.e the sum of all the lengths of the word tokens 
    in the text, divided by the number of word tokens)

    Parameters: 
    file - string
     
    Returns:
    average word length of the file
    
    bn-2016
    """
    x = 0.0 # creating a count to store the length of the words 
    
    f = open(file) # opens the file inputted by user and stores it as f
    
    wordlist = re.findall('\w+', f.read()) # findall() matches all occurences of
    # words and stores as a list of strings in wordlist
    
    for word in wordlist: # for each word in wordList
        x += len(word) # x will count the total sum of the length of words
    return x/len(wordlist) # the total sum will be divided by the amount of
    # words in wordlist to give us the average

#  Testing with a txt file
avg_word_length('/Users/bnew/GitHub/Newbold_Brett_python/test.txt')



#8


from random import randrange

def guess():
    """
    This function, guess(), allows the user to play the "Guess the Number" game,
    where the number to be guessed is randomly chosen between 1 and 20.
     
    Returns:
    interaction in the terminal
    
    bn-2016
    """
    
    print("Hello! What is your name?") # Shows up in terminal
    
    name = input() # User types in their name

    print('Well, %s, I am thinking of a number between 1 and 20.' % name)
    # The %s token is replaced by whatever I pass to the string after the % symbol.
    
    num_guess = 0 # Count for the number of guesses
    
    number = randrange(1,21) # Random integer between 1 and 20 inclusive

    while True:
        print('Take a guess.') # Prints to the terminal
        guess = int(input()) # Guess is defined to be what the user types
        num_guess += 1 # Every time while loop repeats the number of guesses 
                       # will build 

        if guess == number:
            print('Good job, %s! You guessed my number in %d guesses!' % (name, num_guess))
            break # Ends while loop if correct
            
        elif guess > number:             
            print('Your guess is too high.')
            # If the guess is greater than the actual number
            
        else: 
            print('Your guess is too low.')
            # If the guess is less than the actual number
    


#10 


def lingo(word):
    """
    This function, lingo(), allows the user find a hidden word by guessing, and 
    in return receive two kinds of clues: 1) the characters that are fully 
    correct, with respect to identity as well as to position, and 2) the
    characters that are indeed present in the word, but which are placed in the
    wrong position. 
    
    Parameters: 
    guess - string (word) of 5 characters (letters)
    
    Returns: string of characters with each letter unchanged, with (), 
    or with []
    
    
    bn-2016
    """

    guess = input('Enter a 5 letter word: ')
    
    while guess != word: # will keep executing as long as boolean is true,
    # so as long as the users guess does not equal the "hidden" word
        clue = '' # creating an empty string to store the output
        for j, i in enumerate(guess): # runs multiple counters in a single loop
            if i in word: # if the same letter is found in word
                if guess[j]== word[j]: # if the location of the letter is the same
                    clue += '[' + i + ']' # put it in brackets
                else:
                    clue += '(' + i + ')' # if the same letter is found but 
                    # in a different location
            else:
                clue += i # if it was not found at all in the hidden word
        print ('Clue:' + clue) # outputs the clue after running through the 
        # for loop 
        guess = input('Please input another 5 letter guess: ') # creates a new
        # guess for the while loop to work with
    print ('Congrats! You guessed correctly!') # if boolean is false from while
    # loop (if guess == word) then it is time to celebrate at the new MGM casino
    # at National Harbor
            
# Testing, testing
lingo('tiger')
lingo('lingo')


#11

import re # import regular expressions to use split()
    
def splitter(file):
    """
    This function, splitter(), takes the name of a text file and writes its 
    content with each sentence on a separate line.
    
    Parameters: 
    file - provided by user
    
    Returns: The contents of the file with each sentence written on a new line.
    
    bn-2016
    """
    
    with open(file, 'r') as f:
    # Use "with" keyword so that the file is properly closed after the 
    # following indented lines. open() returns a file object, the mode 'r'
    # is used since f will only be read 
        
        str = f.read() # string is defined to be the contents of the file

    for i in re.split(r'(?<=[^Mr|Mrs|Dr][.?!])\s(?=[A-Z])', str): # A lot going 
    # on here, it will create a new line if any character from [.?!] is followed
    # by \s (whitespace) and a capital letter (?=[A-Z]) using "lookahead assertion", 
    # ?<=[][] is a "Positive lookbehind assertion" will make sure to avoid the case
    # of Mr., Mrs., or Dr. 
        print (i) 

# Here comes the splitter down the middle 
splitter('copy file here')