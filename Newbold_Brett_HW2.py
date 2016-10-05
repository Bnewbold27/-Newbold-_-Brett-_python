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
##Prof G - Nice approach and great handling of mixed case. You could have also
##Prof G - put this in a function.        
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

import string # Allows us to use string.punctuation

filename = input('Enter the file name: ') # Asks the user to enter a file name

disregard = string.punctuation + " " # string.punctuation will gather punctuation 
                                     # characters so we disregard them later
                                     # along with spaces 

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
    
    refined = [x for x in file.rstrip().lower() if x not in disregard]
    # List comprehension that creates a new string (refined) that collects 
    # characters from the file after making them lower case and strips the 
    # whitespace characters at the end of string. However, if x is 
    # found in disregard, it gets disregarded
    
    return refined

##Prof G - This little definition cost me about an hour of time to discover.
##Prof G - Essentially it overwrites the definition of the base funtion list()
##Prof G - and subsequent calls to list fail (such as in you char_freq_table 
##Prof G - function)
list = [] # Creates an empty list

with open(filename, 'r') as f: 
        # Use "with" keyword so that the file is properly closed after the 
        # following indented lines. open() returns a file object, the mode 'r'
        # is used since filename will only be read 
    
    for line in f:
        
        if semordnilap(line)[::-1] in list: 
        # Scans the list for its counterpart
            
            print(semordnilap(line), semordnilap(line)[::-1])
            # Prints the pair of words that are semordnilaps
            
        else:
            list.append(semordnilap(line))
            # Adds the refined string to our list in our For loop. 
    
    
    
#3
    
filename = input('Enter file name: ') # Asks the user to input a file name
   
def char_freq_table(filename):
    """
    This function, char_freq_table() accepts a file name from the user, builds 
    a frequency listing of the characters contained in the file, and prints a
    sorted and nicely formatted character frequency table to the screen.

    Parameters: 
    file - string inputted by the user 

    Returns:
    semordnilaps if it is indeed one
    
    bn-2016
    """
    
    freq_table = dict() # Creates an empty dictionary where we can display each 
                        # character with it's frequency
    
    with open(filename, 'r') as f:
    # Use "with" keyword so that the file is properly closed after the 
    # following indented lines. open() returns a file object, the mode 'r'
    # is used since filename will only be read
        
        str = [x for x in f.read() if x not in ['\n',' ']]
        # Returns a string of characters from the file but excludes new lines 
        # (\n) and whitespaces (' ')

        for char in str:
            # My guess is an arbitrary letter will be in the file more times 
            # than not so lets begin with that scenario
            if char in freq_table: 
                freq_table[char] += 1 # Adds 1 to itself for each repetition
            else:
                freq_table[char] = 1
                # This if-else creates the value based on how many times the 
                # character appears in the string and furthermore stores them
                # into the dictionary

        print('Characters frequency table:')
        
        ##Prof G - not sure why you try to call an object definiton here but
        ##Prof G - it creates an error. See my comment above.
        myList = list(freq_table.items())
        # Using items() to iterate across our dictionary (freq_table) while 
        # making a list 
        
        for char in sorted(myList, key=lambda x: x[1], reverse=True):
        # sorted() calls on each list element of myList using the key function.
        # It will sort them in ascending order by the value of each character.
        # reverse = True then makes it descending order
           
           print(char[0], freq_table[char[0]])
           # prints first character and its corresponding frequency utilizing
           # the dictionaries created above

char_freq_table(filename)


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
                
                time.sleep(ICAOpause) # delays for that many seconds between letters
                
                ##Prof G - The next line should be moved to the left to align
                ##Prof G - with the for loop "for word in .." so the pause will 
                ##Prof G - occur between words
                time.sleep(WORDpause) # delays for that many seconds bewtween words
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
        ##Prof G - This does not work when the full path of the file is 
        ##Prof G - included. You might try using two parameters (an input file
        ##Prof G - and an output file). Works well otherwise.
        with open('Numbered_' + file, 'w') as f2:
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


from string import punctuation

def average_word_length(file):
    """
    This function, average_word_length(), calculates the average word length of 
    a text stored in a file (i.e the sum of all the lengths of the word tokens 
    in the text, divided by the number of word tokens)

    Parameters: 
    file - string
     
    Returns:
    average word length of the file
    
    bn-2016
    """
    
    with open(file, 'r') as f:
    # Use "with" keyword so that the file is properly closed after the 
    # following indented lines. open() returns a file object, the mode 'r'
    # is used since f will only be read 
    
        for line in f:
           
            new_line = [x for x in line if x not in punctuation]
            # List comprehension that creates a new string (new_line) that gets
            # rid of the unwanted punctuation
            
            ##Prof G - Need to coerce new_line into a string before the split
            ##Prof G - method can be called. This breaks the function on my
            ##Prof G - machine. See my comments above about the list object
            ##Prof G - you defined.
            values = list(map(len, new_line.split()))
            # split() creates a list of the words in new_line
            # map() applies the len function to each word of the list to evaluate
            # the length of each word
            # list() creates a list of these values
            
    print( sum(values) / len(values) )
    # to calculate the average 


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
        guess = input() # Guess is defined to be what the user types
        num_guess += 1 # Every time while loop repeats the number of guesses 
                       # will build 
        ##Prof G - Need to coerce input string to a number. You can do this with
        ##Prof G - the int() function like this guess = int(input())
        
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

    
from random import randrange 

##Prof G - I like your approach of randomly selecting a word to play against but
##Prof G - the logic and scope do not quite work out. In play_lingo, you should
##Prof G - call lingo with the word list. Then your should implement the while 
##Prof G - loop around the for loop.
def lingo(wordList):
    """
    This function, lingo(), allows the user find a hidden word by guessing, and 
    in return receive two kinds of clues: 1) the characters that are fully 
    correct, with respect to identity as well as to position, and 2) the
    characters that are indeed present in the word, but which are placed in the
    wrong position. 
    
    Parameters: 
    wordList - word bank to generate a random word
    guess - string (word) of 5 characters (letters)
    
    Returns: string of characters with each letter unchanged, with (), 
    or with []
    
    
    bn-2016
    """

    hidden = wordList[randrange(0, len(wordList))]
     # randrange() takes a random integer from 0 to len(wordList), in our case
     # (0,6) excluding 6. Afterwards, wordlist[] then defines hidden as the word 
     # in wordList using that integer position of the random integer


    def play_lingo(guess): # This function will take the users guess and output
                           # a clue 
        
        clue = '' # Begins as an empty string
  
        for c in guess: # For character (letter) in the user's guess
            c = c.lower() # Just in case they tYpe in an UppeRcase letter
            
            if c in hidden: # If the letter is in the hidden word 
            
                if guess[guess.index(c)] == hidden[guess.index(c)] \
                    and guess.index(c) == hidden.index(c):
                # guess.index(c) gets the position of c in guess. Furthermore, 
                # guess[guess.index(c)] outputs the actual letter. This is first
                # checking if the letter in both words are the same AND if the
                # postions are the same
                    
                    clue += '[%s]' % c # The c's that satisfy these two conditions
                                       # will be placed inside []
                else:
                    clue += '(%s)' % c # The c's in hidden but failed to meet the
                                       # two conditions will be placed in ()
                    
            else: 
                clue += c # If c is not in hidden it remains as itself. The +=
                          # will take care of the accumulating string as each c
                          # goes through this "flow chart" 
        
        print('Clue: ' + clue) # Displays the clue

    while True: # Needed to add so program keeps running 
        guess = input('Enter a 5 letter word: ') # Prompts user to input word
        play_lingo(guess) # Our function gets called up to the big leagues

lingo(['snake', 'times', 'tiger', 'black', 'ocean', 'lower'])


#11

import re # To use regular expressions

##Prof G - Doesn't quite work on my file.
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

    text = re.sub(r'\n', '', str)
    # Replaces the pattern \n (newlines) with null, therefore it initially 
    # removes new lines
    
    text = re.sub(r'\?\s', '?\n', text)
    # This will replace question marks followed by a space (\?\s) with a new
    # line after the question mark (?\n).
    
    text = re.sub(r'!\s', '!\n', text)
    # This will replace exclamation points followed by a space (!\s) with a new
    # line after the exclamation point (!\n).

    text = re.sub(r'(?<!Mr)(?<!Ms)(?<!Mrs)(?<!Dr)\.\s([A-Z])', r'.\n\1', text)
    # This will replace the pattern \.\s([A-Z]) (Periods followed by whitespace 
    # and then an upper case letter) by period, new line, and whatever letter
    # was found (\1). 
    # ?<! will exclude the scenarios when a period is after Mr, Ms, Mrs, or Dr. 

    # Text keeps refining with each step because it is calling the previous
    # text string with each sub() 

    print(text)
