# data structure is a way to store data and perform programs efficiently
# ds is of two type ->linear and non-linear

# 1) linear ds-->    array(stores multiple ddata of same type) ,
#                    linked list ,
#                    stacks (last in first out),
#                    queue (first in first out),
#                    hashing 

# 2) non-linear ds --> tree ,
#                      graph

# creating our own list 

import ctypes

class Meralist:
    def __init__(self):
        self.size = 1 #size of list
        self.n = 0 # number of element

        # create a ctype array with size = self.size
        self.arr = self.make_array(self.size)

    def make_array(self , capacity):
        # this creates a c type static and referential array with size = capacity
        return (capacity*ctypes.py_object)()

# getting the length of list 
    def __len__(self):
        return self.n
    
    def __resize(self , new_capa):
        # create a new array with new capacity
        new_arr = self.make_array(new_capa)
        self.size = new_capa

        # copy the content of prev array to new array
        for i in range(self.n):
            new_arr[i] = self.arr[i]

        self.arr = new_arr

# appending the list from the end 
    def append_array(self , item):
        if self.n == self.size:# it means that the list is full
            # resize
            self.__resize(self.size*2)

        # append
        self.arr[self.n] = item
        self.n += 1

# printing the list 
    def __str__(self) -> str:
        result = ''
        for i in range(self.n):
            result += str(self.arr[i]) + ","

        return '[' + result[:-1] + ']'

# indexing and then printing the item at that index (note we are starting the index from 0 and you can change it by self.n=integer from where to start)        
    def __getitem__(self , index):
        if 0<= index < self.n:
            return self.arr[index]
        else:
            return 'IndexError'

    def pop_array(self):
        if self.n == 0:
            return 'Empty list'
        
        poped_item = self.arr[self.n -1]
        self.n = self.n - 1
        return poped_item

    def clear_array(self):
        self.n = 0
        self.size = 1

    def find_array(self , item):
        for  index in range(self.n):
            if self.arr[index] == item:
                return index
        else:
            print("ValueError --> not found in the list")

# inserting an element
    def insert_array(self , index , item_on_index):
        if self.n == self.size:
            self.__resize(self.size*2)

        # shifting the element
        for i in range(self.n , index , -1):
            self.arr[i] = self.arr[i - 1]
        
        self.arr[index] = item_on_index

    def __delitem__(self , index):
        if 0<= index < self.n:
            for i in range(index , self.n -1):
                self.arr[i] = self.arr[i+1]

            self.n -=1

        else:
            raise IndexError('not in list')
        return self.arr

    def remove_array(self , value_to_remove):
        
        index_to_remove = self.find_array(value_to_remove)
        if type(index_to_remove) == int:
            self.__delitem__(index_to_remove)
        else:
            raise ValueError('value not in list')



l = Meralist()

l.append_array(100)
l.append_array(3.4)
l.append_array(3.564)


print(l)
print(l.find_array(3.4))
l.insert_array(1 , 55)
# print(l.__delitem__(10))
print(l.remove_array(100))
print('after')
print(l)