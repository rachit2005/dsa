from time_efficiency import time_it
import random

@time_it
def bubble_sort(elements):
    size = len(elements)     

    for j in range(size):
        swapped = False
        for i in range(size-j-1):
            if elements[i] > elements[i+1]:
                elements[i] , elements[i+1] = elements[i+1] , elements[i]
                swapped = True

        if not swapped : # list is already sorted
            break



def bubble_sort_for_dictionary(dictionary , key=None):
    size = len(dictionary)

    for j in range(size):
        swapped = False
        for i in range(size-1-j):
            if dictionary[i][key] > dictionary[i+1][key]:
                dictionary[i] , dictionary[i+1] = dictionary[i+1] , dictionary[i]
                swapped = True

        if not swapped:
            break



if __name__ == "__main__":
    # l = [i for i in range(1000)]
    # elements = random.choices(l , k = 1000)
    # elements = [1,2,3,4,5,6,7,8,9]    

    elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

    # bubble_sort(elements=elements)
    bubble_sort_for_dictionary(elements , 'transaction_amount')
    for _ in elements:
        print(_)