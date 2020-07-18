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

#assert False
### Function

def read_text (file_path):
  with open(file_path) as f:
      ct = 0
      for line in f:
        print("#{}: {}".format(ct, line))
        #record_word_cnt(line.strip().split(' '), bag_of_words)
        ct = ct + 1


# Now call the function
# data = read_text (file_path)


### Funtion: read data into Python list
def remove_dot_and_more (words):
  data = []
  for w in words:
    w = w.replace('.', '')
    w = w.replace(',', '')
    w = w.replace('(', '')
    w = w.replace(')', '')
    w = w.replace('”', '')
    w = w.replace('“', '')
    w = w.replace('?', '')
    data.append (w)    
  
  return (data)

def read_text_2 (file_path):
  data = []
  with open(file_path) as f:      
      for line in f:
        words = line.strip().split(' ')
        line_list = remove_dot_and_more (words)

        # Remove the first element
        line_list = line_list [1:]
        #print (line_list)       
        #data.append (line_list)
        data = data + line_list
  return (data)

# Now call the function
data = read_text_2 (file_path)

def count_num_words (data):
  word_count = {}
  for word in data:
    #print (word.lower())
    if word.lower() in word_count:
      word_count[word.lower()] += 1
    else:
      word_count[word.lower()] = 1
  
  return (word_count)

word_count = count_num_words (data)

### Sort the dictionary
sort_orders = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
print (sort_orders)