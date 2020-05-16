import mymodule

line = mymodule.line(15)
###print(line)

l1 = [1, 3, 5, 6 ,4324]
l2 = [5 , 2 , 6, 23, 983,1]
l3 = [1000, 700, 56, 23]

# ###print(max([len(l1), len(l2), len(l3)]))
# ###print(min([len(l1), len(l2), len(l3)]))

####print(line)
a = [1, 5, 8]
b = [2, 6, 9, 10]
c = [100, 200]

####print(max([len(a), len(b), len(c)]))
###print(min([len(a), len(b), len(c)]))
###print(line)

names = ["Carol", "Albert", "Ben", "Donna"]
###print(" & ".join(sorted(names)))
###print(line)
names = ["Carol", "Albert", "Ben", "Donna"]
names.append("Eugenia")
###print(sorted(names))
###print(line)
arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
###print(arr[2:6])
###print(arr[0:3])
###print(arr[4:7])
###print(line)

# tuples practice
dimension = 23, 45, 100
length, width, height = dimension
###print ("the dimensions are {}x{}x{}".format(length,width,height))
###print(line)

#tuples quiz 2
tuple_a = 1, 2
tuple_b = (1, 2)

###print(tuple_a == tuple_b)
###print(tuple_a[1])
###print(line)
# quiz of set
a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
###print(len(a))
###print(b)
###print(len(a) - len(b))
###print(line)

a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
b.add(5)
b.pop()
###print(b)
###print(line)

#pop practice

fruit = {'apple', 'banana', 'watermilan','papaya'}
###print(fruit)
###print('coconat'in fruit)
###print('apple' in fruit)
fruit.add('coconat')
###print(fruit)
###print(fruit.pop())
###print(fruit)
###print(line)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ################ DICTIONARY PRACTICE ######################
# ------------------------------------------------------------
##print(line)
population = {'Shanghai':17.8,
        'Istanbul': 13.3,
        'Karachi': 13.0,
        'Mumbai': 12.5
        }

##print(population)
##print('\n'.join(population))
##print(line)

test_dic = {

}

# quiz
##print(line,'\n'+"QUIZ DATA STRACTURE"+ '\n')
a = [1, 2, 3]
b = a
c = [1, 2, 3]

# ##print(a == b)
# ##print(a is b)
# ##print(a == c)
# ##print(a is b)
# ##print(a,c)

# more quiz abot DICTIONARY

animals = {'dogs': [20, 10, 15, 8, 32, 15],
        'cats': [3,4,2,8,2,4],
        'rabbits': [2, 3, 3],
        'fish': [0.3, 0.5, 0.8, 0.3, 1]}

##print(type(animals))
##print(animals['dogs'][3])
###print(animals[3])
##print(animals['cats'])
##print(line)

VINIX =  {'C': 0.74, 'MA': 0.78, 'BA': 0.79, 'PG': 0.85,
 'CSCO': 0.88, 'VZ': 0.9, 'PFE': 0.92, 'HD': 0.97, 'INTC': 1.0,
  'T': 1.01, 'V': 1.02, 'UNH': 1.02, 'WFC': 1.05, 'CVX': 1.05,
    'BAC': 1.15, 'JNJ': 1.41, 'GOOGL': 1.46, 'GOOG': 1.47, 'BRK.B': 1.5,
     'XOM': 1.52, 'JPM': 1.53, 'FB': 2.02, 'AMZN': 2.96, 'MSFT': 3.28,
       'AAPL': 3.94}


VINIX = {'C': [0.74, -6.51],  'MA': [0.78, 34.77],
'BA': [0.79, 17.01],  'PG': [0.85, -8.81],  'CSCO': [0.88, 18.56],
  'VZ': [0.9, 2.16],  'PFE': [0.92, 13.96],  'HD': [0.97, 3.2],
    'INTC': [1.0, 2.61],  'T': [1.01, -15.19],  'V': [1.02, 24.0],
      'UNH': [1.02, 19.32],  'WFC': [1.05, -3.59],  'CVX': [1.05, -5.77],
        'BAC': [1.15, 4.27],  'JNJ': [1.41, -5.58],  'GOOGL': [1.46, 17.84],
          'GOOG': [1.47, 17.03],  'BRK.B': [1.5, 4.54],  'XOM': [1.52, -6.87],
            'JPM': [1.53, 7.66],  'FB': [2.02, 0.91], 'AMZN': [2.96, 62.75],
             'MSFT': [3.28, 26.61], 'AAPL': [3.94, 26.01]}

##print(VINIX['INTC'])

                            # PRACTICE QUIZ
print(line)
verse = "if you can keep your head when all about you are losing theirs and blaming it on you   if you can trust yourself when all men doubt you     but make allowance for their doubting too   if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise"
#print(verse, '\n')


# split verse into list of words
# verse_list = verse.split()
# print(verse_list, '\n')
#
# # convert list to a data structure that stores unique elements
# verse_set =set(verse_list)
# print(verse_set, '\n')
#
# # print the number of unique words
# num_unique =len(verse_set)
# print(num_unique, '\n')

# verse = "if you can keep your head when all about you are losing theirs and blaming it on you   if you can trust yourself when all men doubt you     but make allowance for their doubting too   if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise"
# #print(verse, "\n")
#
# # split verse into list of words
# verse_list = verse.split()
# print(verse_list, '\n')
#
# # convert list to set to get unique words
# verse_set = set(verse_list)
# print(verse_set, '\n')
#
# # print the number of unique words
# num_unique = len(verse_set)
# print(num_unique)

verse_dict =  {'if': 3, 'you': 6, 'can': 3, 'keep': 1, 'your': 1, 'head': 1, 'when': 2, 'all': 2, 'about': 2, 'are': 1, 'losing': 1, 'theirs': 1, 'and': 3, 'blaming': 1, 'it': 1, 'on': 1, 'trust': 1, 'yourself': 1, 'men': 1, 'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1, 'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, 'don\'t': 3, 'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1}
print(verse_dict, '\n')

# find number of unique keys in the dictionary
num_keys =len(verse_dict)
print(num_keys)

# find whether 'breathe' is a key in the dictionary
contains_breathe = "breathe" in verse_dict
print(contains_breathe)

# create and sort a list of the dictionary's keys
sorted_keys =sorted(verse_dict.keys())

# get the first element in the sorted list of keys
print(sorted_keys[0])

# find the element with the highest value in the list of keys
print(sorted_keys[-1])
