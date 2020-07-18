print ()
print ('#'*50)

################################################################################
# dictionary
################################################################################

age = {'yeojin': 15, 'david': 14, 'chase': 13, 'daniel': 12, 'jooan': 12, 'hamin':11}


my_name = 'hamin'
#print ('My age is: {}'.format(age['chase']))
print ('My name is {}, \
and my age is: {}'.format(my_name, age[my_name]))

# Amazon
user_ids = {'seunjeong': 2002, 'davidj': 'no', 'yamazon':2019}

user = 'yamazon'

#print ("member since {} for {}".format (user_ids[user], user))


# Now, print them all.

for x in age.items():
  print (x)

# In a clearer way
for x in age.items():
  print ('Name: {}; Age {}'.format (x[0], x[1]))

################################################################################
# Function
################################################################################

def add (x, y): # x and y are called parameters.
  total = x + y
  return (total)

print (add (3,5))
print (add (1215461123,112345)) # reuse.

def multiply (x, y):
  return (x * y)

print (multiply (3, 5))
print (multiply (1215461123, 112345)) # reuse.

def average (x, y):
  return ((x + y)/2)

print (average (2, 8))

################################################################################
# Reading data from files
################################################################################
file_path = 'john_3.txt'

with open(file_path) as f:
  #ct = 0
  for ln in f:
    #print("#{}: {}".format(ct, a))
    print("{}".format(ln))
    #ct = ct + 1