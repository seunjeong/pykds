################################################################################
# More on String
################################################################################

my_name = 'Seongeun'
my_age = 46

# Two different ways of print things
print ('My name is: ' + my_name)
print ('My name is {}'.format (my_name))

# With age
print ('My name is {}, and my age is {}'.format (my_name, my_age))


################################################################################
# List 
#   - definition: A list is a data structure in Python that is ordered sequence of elements. Each element (or value) that is inside of a list is called an item. 
################################################################################

#===============================================================================
# Initiating list
#===============================================================================
num_list = [1,2,3] # number
mixed_list = [1,'a', 'b', 2]


# Play with a shopping list
shopping_list = ['banana', 'yogurt', 'milk', 'meat', 'peach', 'chips', 'chocolate', 'tomato', 'toothpaste']

for i in range (len(shopping_list)):
  print (i) # i is called index
  print (shopping_list [i])

# empty list
a_list = []

# add to the empty list
a_list.append (1)
print ('Now a_list is {}'.format(a_list))

# add more
a_list.append ('a')
print ('Now a_list is {}'.format(a_list))

#===============================================================================
# Create a longer list and print its item.
#===============================================================================
# Adding more 
long_list = []
items = range (10)
for i in items:
  long_list.append (i)
# by now, long_list is full of 10 values.

# now let's see it 
for this_item in long_list:
  print (this_item)

################################################################################
# Dictionary 
#   - defintion: Dictionaries are Python’s data structure, and  a dictionary consists of a collection of key-value pairs.
################################################################################

# Declare a dictionary
avengers = {'movie_name': 'Iron Man', 'year':2008}
print ('Release year of Iron Man: {}'.format (avengers['year']))


################################################################################
# "for" loop 
################################################################################
for name, year in avengers.items():
    #print (name)
    print ('{}; {}'.format(name, year))



