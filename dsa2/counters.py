from collections import Counter
import random

obj_list = ["a" , 'b','c','d','e']

# using dict for counting the repetition
'''
dct = {}
for obj in obj_list:
    dct[obj] = 0

for _ in range(100):
    dct[random.choice(obj_list)] +=1

print(dct)
'''

# using counter 
# we can use counter as a dictionary without initialising it first
'''
counter = Counter()
print(counter)

for _ in range(100):
    counter[random.choice(obj_list)] +=1

print(counter)
print(counter.total()) # gives us the sum of all the individual key
'''

# now we have to count the occurences of the individual items

# 1) first we use the dictionary method
'''occurences = random.choices(obj_list , k=100)

dct = {}
for obj in obj_list:
    dct[obj] = 0

for i in occurences:
    dct[i] +=1

print(dct)

# 2) using counter method

counter = Counter(occurences)
print(counter)

# finding the most common 
print(counter.most_common(2)) # gives us the 'n' most common key in counter dict

# for finding the common in dictionary

max_val = -1
max_key = None

for key , value in dct.items():
    if value > max_val:
        max_val = value
        max_key = key

print(max_key , max_val)
'''
