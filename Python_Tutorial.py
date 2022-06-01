# This is a file with all of the syntax examples used in the official Python tutorial found here https://docs.python.org/3/tutorial/index.html

# Make a file executable add the UNIX shebang line
#! /usr/bin/env python3
# Then give the file execute rights with chmod +x

# Control flow is based on indentation, use tabs as spaces, so no curly braces like in js, but the colon : and indentation

#Numeric operations
floor = 17 // 3 # do the division and return as int, discard fractional part
mod = 17 % 3 # return the remainder
powerThree = 2 ** 3 # calculate powers


#strings on mlti lines
"""This produces
Multiline output
"""

# strings concatentation and repeating
combine = "One string" + "another"
repeat2Times = combine * 2 # OnestrongAnotherOnestrongAnother

# indexing into strings is zero-based
firstLetter = "String"[0] # S
lastLetter = "String[-1] # g

# Slicing gives you substrings
word = "Python"
sub = word[0:2] # Py, it is right exclusive
exceptFirst = word[1:] #ython
upTo2 = word[:2] # py

# len gives length of string
size = len("Python) # 6
           
# Lists in python are mutable
letters = ['a','b','c','d']
letters[2:3] = ['C'] # ['a','b','C','d'] replace a letter(s)
letters[:] = [] # clear a list
letter.append('a') # appends an item, lists can hold multiple types
           
for char in "somestring": # also works for lists
           print(char) 
           
for i in range(5, 10): # can alos pass onvalue to generae an arithmetic progression, add a third argument to specify the step increment
           print(i)
           
# use enumerate function if you need the index and actual item stored at that index
           


          


