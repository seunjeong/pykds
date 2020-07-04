################################################################################
# Variable
################################################################################
"""
   definition: "a variable or scalar is a storage address (identified by a memory address) paired with an associated symbolic name, which contains some known or unknown quantity of information referred to as a value."
    (Source: https://en.wikipedia.org/wiki/Variable_(computer_science)#:~:text=In%20computer%20programming%2C%20a%20variable,referred%20to%20as%20a%20value)
"""

# Number
num = 1
# where "num" is the variable and 1 is the value
print (num)

# String (words)
word = 'Hello'
# (again) where "word" is the variable, and "Hello" is the value. But this time
#   the value is word or "type String value"
print (word)

# A String variable can have a file name, which can be very long
file_name = '~/rlib/ATutorial/A_Jupyter/github/pykids/pykids/class_1.py/class_1.py'

# String name can be almost anything (in a rough definition)
this_is_my_variable_name = 10
thisismyvariablename = 10  # but this is hard to read

# My preferred one would be:
my_var = 10


################################################################################
# Simple math using numerical variable 
################################################################################

#...............................................................................
# Addition
#...............................................................................
x = 20
y = 10
x_y = x + y

print ('x plus y is:')
print (x_y)

#...............................................................................
# Subtraction
#...............................................................................
x_minus_y = x - y
print ('x minus y is:')
print (x_minus_y)

#...............................................................................
# Multiplication 
#...............................................................................
x_times_y = x * y # note the "*" sysmbol
print ('x times y:')
print (x_times_y)

# big random number
x = 12965
y = 939
x_times_y_big = x * y

print ('x times y, big number:')
print (x_times_y_big)

#...............................................................................
# Division
#...............................................................................
x = 25
y = 5
x_div_y = x / y # note the "/" symbol

print ('x divided by y: ')
print (x_div_y)