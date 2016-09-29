# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 19:11:48 2016

Group D

@author: bnew
"""


import pandas as pd 
import urllib.request
import matplotlib.pyplot as plt

"""
1. Directly load the files from the internet into python and add the column
   names using Python code instead of an editor.
"""

url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

webpage = urllib.request.urlopen(url) # Opens the url and defines it as webpage

df = pd.read_csv(webpage, names=['sepal length in cm', 'sepal width in cm', \
    'petal length in cm', 'petal width in cm', 'class'])
    # pandas.read_csv() takes the URL and stores it into DataFrame. pd is just
    # a shortcut to use instead of writing pandas constantly. names is a parameter
    # that allows us to input a list of column names to use
    
"""
2. Using Pandas, display the first ten and last ten rows of the data.
"""
    
print(df.head(10)) # Returns first 10 rows

print(df.tail(10)) # Returns last 10 rows

"""
3. Using pandas, print simple location statistics
"""

print(df.describe()) # Generates various summary statistics 

"""
4. Write a function.. (see below) 
"""

columns = ['sepal length in cm', 'sepal width in cm', 'petal length in cm', \
    'petal width in cm']
    # Creating a list of only the numeric columns

def bin_sizes(integers):
    """
    This function, bin_sizes() accepts a list of numbers that represent numbers 
    of bins and, using Pandas, plots a histogram for each of the numeric columns 
    at each bin size. For example, if the function is called with [10, 50, 100] 
    as bin sizes, the function plots 12 histograms (3 for each numeric
    variable). The histograms are grouped by the column name.

    Parameters: 
    integers - list of integers

    Returns:
    Histograms 
    
    bn-2016
    """

    for str in columns: 
        for int in integers: 
        # Nested for loop so the function takes each column (str) and runs the 
        # inner for loop with respect to each column. This way the histograms 
        # are grouped by name. In other words, starts with first string in 
        # column, runs through every integer in the list, goes to second string,
        # runs through every integer in the list... Rinse, lather, repeat 
        
            x = df.hist(column = str, bins = int)
            # Creates histograms for each column with bin sizes corresponding
            # to the list of integers accepted by the function
            
    return x
    
print(bin_sizes([10,20,30])) # Testing the function 

"""
5. Plot a box plot for each of the numeric columns
"""

df.plot.box() # Plots a box plot for each numeric column

plt.xticks(rotation=45) # The x-axis was too condensed (column names are long)
                        # so I called this to make the x-axis more readable,
                        # it rotates the names 45 degrees CCW  

plt.show() # Had to call this to avoid the box plot and bar chart showing up
           # on the same graph, it shows the box plot before considering the 
           # next plot
"""
6. Plot a bar chart for the nominal column
"""

df.groupby('class').size().plot.bar() # Creates a bar chart for our nominal
                                      # column (class) by grouping the names in
                                      # the column, creating the size by counting 
                                      # how many times they appear, and making 
                                      # a corresponding bar chart

plt.xticks(rotation = 0) # X-axis had vertical names so made them horizontal 
