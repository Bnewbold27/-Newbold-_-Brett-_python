# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 15:12:04 2016

@author: bnew
"""

#1

dictionary = {"merry":"god", "christmas":"jul", "and":"och", 
"happy":"gott", "new":"nytt", "year":"ar"}
# Defining a dictionary where the strings can be in '' or ""                    

def translate(list):
    """
    This function, translate(), recognizes a small bilingual lexicon as a Python 
    dictionary in the following fashion {"merry":"god", "christmas":"jul","and":
    "och", "happy":gott","new":"nytt","y ear":"år"} and uses it to translate 
    Christmas cards from English into Swedish. That is, translate() takes a 
    list of English words and returns a list of Swedish words.

    Parameters: 
    list - list of any English words from defined dictionary

    Returns:
    list of translated Swedish words
    
    bn-2016
    """
    
    wordList = []   # Defining wordList to be an empty list
    
    for word in list:   # For words found in the list that we input 
    
        word = dictionary[word.lower()] # Takes the words inputted into function,
                                        # makes them lower case, finds them as a 
                                        # key (left side of definition) and trades 
                                        # them for their value (right side)
        
        wordList.append(word)   # append() adds each word (now Swedish) to the 
                                # the end of wordList in the order received
            
    return wordList
    
print(translate(['HAPPY', 'christmas', 'and', 'MERRY', 'new', 'year']))

   
   
   
#2
    
def char_freq(str):
    """
    This function, char_freq(), takes a string and builds a frequency listing of 
    the characters contained in it. 

    Parameters:
    str - any string with characters
    
    Returns:
    Python dictionary with the characters and their corresponding frequencies
    
    bn-2016
    """
    freq = dict() # Creates dictionary with {keys : values}

    for char in str:
        if char not in freq: # Chances are the letter will not be in the word, 
                             # so we begin with this
        
            freq[char] = 1 # Our if-else creates the value (right side of 
                           # definition) based on how many times the character 
                           # appears in the string  
            
        else:                   
            freq[char] += 1 # Adds to 1 to itself for each repetition

    return freq

print(char_freq('mississippi'))
print(char_freq("abbabcbdbabdbdbabababcbcbab"))




 
#3
 

key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
       # Defining a dictionary for our function to work with


def caesar_cypher(str):     
    """
    This function, caesar_cypher(), implements an encoder/decoder of ROT-13 
    to be able to read secret messages.

    Parameters:
    str - any string with characters
    
    Returns:
    String that has been converted 
    
    bn-2016
    """
    result = "" # Defining variable to be an empty string

    for char in str:
        if char in key:            
            result += key[char] # If character is found in dictionary above, it 
                                # results in its value, += allows the accumulation
                                # of these values
        else:
            result += char # If the character is not found in the key it will
                           # just result in itself, += again to keep these results
                           # accumulating 
    return result
  
print(caesar_cypher('Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!'))  #Dad joke
print(caesar_cypher('This is funny!')) 



 
 
#4
 
import re     #to use regular expressions like re.sub()

def correct(string):    #function used to input our parameter (string)
    """
    This function, correct(), takes a string and sees to it that 1) two or more 
    occurrences of the space character is compressed into one, and 2) inserts 
    an extra space after a period if the period is directly followed by a letter

    Parameters:
    string - any string with characters
    
    Returns:
    String that has proper spacing
    
    bn-2016
    """
    
    compspace = re.sub(r'\s{2,}', ' ', string)
    # Method that takes pattern (first slot), replaces it with second slot 
    # anywhere in the string (third slot). The pattern \s{2,} is a whitespace 
    # that occurs 2 or more times
      
    extraspace = re.sub(r'(\.)(\w)', r'\1 \2', compspace)
    # Method that inserts a space after a period if it is directly followed 
    # by a letter. The pattern (\.)(\w) looks for a period followed by a single 
    # word character (\w) in the new string, compspace, and replaces it with 
    # the same expression but with a space between
     
    return extraspace

print(correct('This   is        very funny  and    cool.Indeed!'))





#5 


suffix = ('o', 'ch', 's', 'sh', 'x', 'z') #defining suffixes         

def make_3sg_form(str):    #create function which tests a parameter (verb)
    """
    This function, make_3sg_form(), takes a verb in infinitive form and returns 
    its third person singular form.

    Parameters:
    str - a string that is a verb
    
    Returns:
    String that is a verb in third person singular form.
    
    bn-2016
    """

    if str.endswith('y'): # True if the string ends with y
        
        return str[:-1] + 'ies' # Takes a substring of verbs that end in y (all
                                # of it except last character) and adds 'ies'     
    
    elif str.endswith(suffix): # True if string ends with defined suffixes above
        return str + 'es' # Simply adds 'es' to the unchanged string
     
    else:  
        return str +'s' # Anything else we will just add 's' to

#testing various verbs
print(make_3sg_form('try'))
print(make_3sg_form('brush'))
print(make_3sg_form('run'))
print(make_3sg_form('fix'))
print(make_3sg_form('reply'))
print(make_3sg_form('go'))  
print(make_3sg_form('munch'))
print(make_3sg_form('buzz'))
print(make_3sg_form('access'))





#6

vowels = {'a','e','i','o','u'} # Defining vowels so it can search the ends of 
                               # verbs for them

def make_ing_form(str):
    """
    This function, make_ing_form(), takes a verb in infinitive form and returns 
    its present participle form.

    Parameters:
    str - a string that is a verb
    
    Returns:
    String that is a verb in present participle form
    
    bn-2016
    """
    if str.endswith('ie'): # True if string (verb) ends with 'ie'
        return str[:-2] + 'ying' # Takes a substring by erasing last two letters
                                 # of verb and replacing it with "ying"
    
    elif str.endswith('e'): # True if string (verb) ends with 'e'
        return str[:-1] + 'ing' # Takes a substring by erasing last letter and 
                                # replacing it with "ing"
    
    elif str[-3] not in vowels: # True if there is consonant in the third from 
                                # last letter of the string (verb)
        if str[-2] in vowels: # True if there is a vowel in the second to last 
                              # letter of the string 
            if str[-1] not in vowels: # True if there is a consonant in the last 
                                      # letter of the string 
          
              return str + str[-1] + 'ing' # If it finds this consonant-vowel-
                                           # consonant pattern, it will take the 
                                           # verb, double the last letter, and
                                           # finally attach "ing" to the end
    else:    
        return str + 'ing' # True if it fails to meet any condition above, if 
                           # so we will just add "ing" to the string

#testing various verbs
print(make_ing_form('lie'))
print(make_ing_form('see'))  #unfortunate
print(make_ing_form('move')) 
print(make_ing_form('hug'))  #consonant-vowel-consonant
print(make_ing_form('accelerate'))

# I tried to go in order listed, accounting for 'e' first then 'ie' second. 
# However, "lie" would be swallowed by if str.endswith('e')
# We could possibly fix "see" by searching for endswith('ee') and + 'ing' and
# then search for endswith('e') and keep same rule (take away e and + 'ing')




#7

import functools # For higher order functions: functions that act or return 
                 # other functions

def max_in_list(list): 
    """
    This function, max_in_list(), takes a list of numbers and returns the 
    largest one.

    Parameters:
    list - a list of numbers
    
    Returns:
    Largest number in the list
    
    bn-2016
    """

    return functools.reduce(lambda x, y: x if x > y else y, list)      
    # Reduces our list to a single value by moving left to right and updating y 
    # based on our iterable. x and y start as first two items in the list

print(max_in_list([5,3,2,7,8,23,1,4]))  

# Defining and calling the function could be beneficial if our list is dependent 
# on variables. We could run code to find out what the list is and simply 
# print(max_in_list(list)) once we solve for the list. """





#8


def word_length_a(wordList):   
    """
    These functions, word_length_a(), word_length_b(), and word_length_c(), all
    map a list of words into a list of integers representing the lengths of 
    the corresponding words.

    Parameters:
    wordList - a list of words
    
    Returns:
    list of integers corresponding to the lengths of words
    
    bn-2016
    """
    wordLengths = [] # Defining a variable as an empty list 
    
    for word in wordList: # For-loop for every word we find in the list 
  
        wordLengths.append(len(word)) 
        # len() is a built in function that returns the number of items of an 
        # object, this finds the length of a word in the list and then append() 
        # adds this length to the end of our defined list "wordLengths"
    
    return wordLengths


def word_length_b(wordlist): 
    
    return list(map(len, wordlist))  
    # The function map() applies the function len (defined above) to every item 
    # of the itereable wordlist and furthermore creates a list using list()  
      

def word_length_c(wordlist): 

    return [len(word) for word in wordlist] 
    # List comprehension that creates a list by evaluating len(word) for every 
    # word found in the wordlist and results in a list of word lengths


print(word_length_a(['python', 'R', 'sas']))
print(word_length_b(['python', 'R', 'sas']))
print(word_length_c(['python', 'R', 'sas']))


#9

def find_longest_word(wordlist):  
    """
    This function, find_longest_word(), takes a list of words and returns the 
    length of the longest one.

    Parameters:
    wordList - a list of words
    
    Returns:
    Length of the longest word in the list
    
    bn-2016
    """
    
    return max(list(map(len, wordlist)))  
    # Working from the inside out: the function map() applies the function len 
    # to every item of wordlist. In other words, map() finds the length of every 
    # word in the list. List() creates a list of these lengths (integers).
    # Finally, max() returns the maximum value of this list!

print(find_longest_word(['Find', 'longest', 'word']))




#10

  
def filter_long_words(n, wordlist): 
    """
    This function, filter_long_words(), takes a list of words and an integer n
    and returns a list of words that are longer than n.

    Parameters:
    n - integer
    wordList - list of words
    
    Returns:
    List of words that are longer than n
    
    bn-2016
    """  
    
    return list(filter(lambda x: len(x) > n, wordlist)) 
    # filter() scans through the sequence "wordlist", if the function 
    # "len(x) > 2" returns true for each word it will return that item in a list 
    # because we have used list() 


print(filter_long_words(2, ['Georgetown', 'University', 'does', 'no', 'good']))  
# Hopefully the program corrects this nonsense



#11

# Defined dictionary
dict = {"merry":"god", "christmas":"jul", "and":"och",
        "happy":"gott", "new":"nytt", "year":"år"}

def translate(English):
    """
    This function, translate(), takes a list of English words and returns a
    list of Swedish words.

    Parameters:
    English - list of English words defined in the dictionary above
    
    Returns:
    List of Swedish words corresponding to their English counterpart
    
    bn-2016
    """  
    
    return list(map(lambda x: dict[x.lower()], English))   
    # map() will take each element of the list "English", find it as a key in 
    # the dictionary above, and return its value in Swedish. list() creates a 
    # list dependent on the result of map(). x.lower() returns a copy that is in 
    # lower case, as a precaution I added this so it would recognize capital 
    # letters

print(translate(['Merry', 'Christmas', 'and', 'HAPPY', 'NEW', 'YEAR']))




#12

def map(function, iter):
    """
    This function, map(), makes an iterator that computes the function using
    arguments from each of the iterables. Stops when the shortest iterable is 
    exhausted.

    Parameters:
    function 
    iterable
    
    Returns:
    list of the items from iterable that has passed through the function
    
    bn-2016
    """  
    
    result = [] # Defining the variable result to be an empty list
    
    for item in iter:
        
        result.append(function(item))   
        # append() adds every item of the list to the end of the result list
        # once it is applied to the function
        
    return result
    
print(map())
    
def filter(function, iterable):  
    """
    This function, filter(), returns an iterator yielding those item of iterable
    for which function(item) is true. If function is None, return the items 
    that are true. 

    Parameters:
    function 
    iterable
    
    Returns:
    items from iterable that are true after they pass through the function
    
    bn-2016
    """  

    if isinstance(iterable, str): # Returns true if iterable is a string
    
        result = '' # Result is empty string for now
    
    elif isinstance(iterable, tuple): # Returns true if iterable is a tuple   
  
        result = () # Result is empty tuple for now
        
    else:
        result = [] # If none of the above, return a list
        
    for item in iterable:
        
        if function(item): # Items will pass through defined function in filter()
                           # and the ones that return true will be kept
        
            if isinstance(iterable, str): # Returns true if iterable is a string
            
                result += item # Result will be a string of items that returned
                               # true
                    
            elif isinstance(iterable, tuple): # Returns true if iterable is a 
                                              # tuple
           
                result += item # Result will be a tuple of items that returned 
                               # true
                    
            else:
                result.append(item) # If none of the above, a list is created 
                                    # with the items that returned true in the
                                    # function
                
        return result
        

def reduce(function, iterable, initial=None):
    """
    This function, reduce(), applies the input function to items of our iterable
    until it is reduced to a single value.

    Parameters:
    function 
    iterable
    initial
    
    Returns:
    single value
    
    bn-2016
    """

    i = iter(iterable) # Creating an iterator object from the iterable
    
    if initial is None:
        result = next(i)
        
    else:
        result = initial
    
    for item in i:
        result = function(result, item) # Will result in one value 
        
    # If it is given, initial comes before the items in our sequence when the 
    # function is applied. Reduce() has two arguments (x,y) that start with the 
    # first two elements. It makes sense that our function is passing two 
    # parameters in a for loop because it keeps taking the result and operating 
    # on the next item. 
     
    return result
    