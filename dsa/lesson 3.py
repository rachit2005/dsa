# Lesson 3 - Sorting Algorithms and Divide & Conquer

# read this --> https://jovian.ai/learn/data-structures-and-algorithms-in-python/lesson/lesson-3-sorting-algorithms-and-divide-and-conquer



# List of numbers in random order
test0 = {
    'input': {
        'nums': [4, 2, 6, 3, 4, 6, 2, 1]
    },
    'output': [1, 2, 2, 3, 4, 4, 6, 6]
}
# List of numbers in random order
test1 = {
    'input': {
        'nums': [5, 2, 6, 1, 23, 7, -12, 12, -243, 0]
    },
    'output': [-243, -12, 0, 1, 2, 5, 6, 7, 12, 23]
}
# A list that's already sorted
test2 = {
    'input': {
        'nums': [3, 5, 6, 8, 9, 10, 99]
    },
    'output': [3, 5, 6, 8, 9, 10, 99]
}
# A list that's sorted in descending order
test3 = {
    'input': {
        'nums': [99, 10, 9, 8, 6, 5, 3]
    },
    'output': [3, 5, 6, 8, 9, 10, 99]
}
# A list containing repeating elements
test4 = {
    'input': {
        'nums': [5, -12, 2, 6, 1, 23, 7, 7, -12, 6, 12, 1, -243, 1, 0]
    },
    'output': [-243, -12, -12, 0, 1, 1, 1, 2, 5, 6, 6, 7, 7, 12, 23]
}
# An empty list 
test5 = {
    'input': {
        'nums': []
    },
    'output': []
}
# A list containing just one element
test6 = {
    'input': {
        'nums': [23]
    },
    'output': [23]
}
# A list containing one element repeated many times
test7 = {
    'input': {
        'nums': [42, 42, 42, 42, 42, 42, 42]
    },
    'output': [42, 42, 42, 42, 42, 42, 42]
}

# creating a long list that is shuffeled

import random

in_list = list(range(10000))
out_list = list(range(10000))
random.shuffle(in_list)

test8 = {
    'input': {
        'nums': in_list
    },
    'output': out_list
}
tests = [test0, test1, test2, test3, test4, test5, test6, test7, test8]


# this sorting method is called bubble sort method
def sort(nums):
    list1 = list(nums)

    # repeating the process over the list n-1 times
    for i in range(len(list1)-1):
        # iterating through the list items
        for j in range(len(list1)-1):
            if list1[j]> list1[j+1]:
                list1[j] , list1[j+1] = list1[j+1] , list1[j]

    return list1

from jovian.pythondsa import evaluate_test_cases

# evaluate_test_cases(sort , tests)


# sorting through insertion sorting method
def insertion_sort(nums):
    nums = list(nums)

    for i in range(len(nums)):        
        # removing the ith item from the list 
        cur = nums.pop(i)
        j = i-1
        # if the ith term of the list is smaller than its prev term(ie jth term) then we will swap its postion
        while j>=0 and nums[j] > cur:
            j -=1
        nums.insert(j+1 , cur)
    return nums

# evaluate_test_cases(insertion_sort , tests)

# now we will use divide and conquer stratergy

def merge(left_nums , right_nums):
    merged = []
    i,j = 0,0

    # loop over the two list 
    while i < len(left_nums) and j < len(right_nums):
        # now we add smaller number in the merged list 
        if left_nums[i] <= right_nums[j]:
            merged.append(left_nums[i])
            i +=1
        else:
            merged.append(right_nums[j])
            j+=1


    left_nums_tail = left_nums[i:]
    right_nums_tail = right_nums[j:]

    return merged + left_nums_tail + right_nums_tail



def merge_sort(nums):
    # terminating the list of 0 or 1 elements
    if len(nums) <=1:
        return nums
    
    mid = len(nums) // 2

    # split list into two halfs
    left = nums[:mid]
    right = nums[mid:]

    # solve the problem for each halfs recursevely
    left_sorted , right_sorted = merge_sort(left) , merge_sort(right)

    # combine the results
    sorted_nums = merge(left_sorted , right_sorted)

    return sorted_nums

# evaluate_test_cases(merge_sort , tests)

# now we will use quick sort method

# function called partitions which picks a pivot, partitions the array in-place, and returns the position of the pivot element.
def partition(nums, start=0, end=None):
    print('partition', nums, start, end)
    if end is None:
        end = len(nums) - 1
    
    # Initialize right and left pointers
    # we are taking the pivot point end element of the list 
    l, r = start, end-1
    
    # Iterate while they're apart
    while r > l:
        print('  ', nums, l, r)
        # Increment left pointer if number is less or equal to pivot
        if nums[l] <= nums[end]:
            l += 1
            print('Increment left pointer if number is less or equal to pivot')
        
        # Decrement right pointer if number is greater than pivot
        elif nums[r] > nums[end]:
            r -= 1
            print('Decrement right pointer if number is greater than pivot')
        
        # Two out-of-place elements found, swap them
        else:
            nums[l], nums[r] = nums[r], nums[l]
    print('  ', nums, l, r)
    # Place the pivot between the two parts
    if nums[l] > nums[end]:
        nums[l], nums[end] = nums[end], nums[l]
        print(nums , l)
        return l
    else:
        print(nums , end)
        return end

def quicksort(nums , start=0 , end = None):
    if end is None:
        nums = list(nums)
        end = len(nums) - 1

    if start < end:
        pivot = partition(nums,start , end)

        # now we will do recursive sorting
        quicksort(nums , start , pivot -1)
        quicksort(nums ,pivot +1 , end)

    return nums

l1 = [1,5,2,6,9,11,3]
# pivot = partition(l1)
# print(l1 , pivot)


# now solving question

class Notebook:
    def __init__(self, title, username, likes):
        self.title, self.username, self.likes = title, username, likes
        
    def __repr__(self):
        return 'Notebook <"{}/{}", {} likes>'.format(self.username, self.title, self.likes)
    
nb0 = Notebook('pytorch-basics', 'aakashns', 373)
nb1 = Notebook('linear-regression', 'siddhant', 532)
nb2 = Notebook('logistic-regression', 'vikas', 31)
nb3 = Notebook('feedforward-nn', 'sonaksh', 94)
nb4 = Notebook('cifar10-cnn', 'biraj', 2)
nb5 = Notebook('cifar10-resnet', 'tanya', 29)
nb6 = Notebook('anime-gans', 'hemanth', 80)
nb7 = Notebook('python-fundamentals', 'vishal', 136)
nb8 = Notebook('python-functions', 'aakashns', 136)
nb9 = Notebook('python-numpy', 'siddhant', 92)

notebooks = [nb0, nb1, nb2, nb3, nb4, nb5,nb6, nb7, nb8, nb9]

def compare_likes(nb1, nb2):
    if nb1.likes > nb2.likes:
        return 'lesser'
    elif nb1.likes == nb2.likes:
        return 'equal'
    elif nb1.likes < nb2.likes:
        return 'greater'


def default(x,y):
    if x > y:
        return 'greater'
    elif x<y:
        return 'lesser'
    else:
        return 'equal'
    
def merge_sort(obs, compare = default):
    if len(obs) < 2:
        return obs
    mid = len(obs)//2
    print("left list")
    print(merge_sort(obs[:mid] , compare))
    print()
    print("right list")
    print(merge_sort(obs[mid:] , compare))

    return (merge(merge_sort(obs[:mid] , compare) , merge_sort(obs[mid:] , compare), compare=compare))


def merge(left , right , compare):
    i ,j ,merged = 0,0,[]

    while i < len(left) and j < len(right):
        result = compare(left[i] , right[j])
        print(result)

# we are arranging the notebooks in descending order
        if result == 'lesser' or result == 'equal':
            merged.append(left[i])
            i +=1
        elif result == 'greater':
            merged.append(right[j])
            j +=1

    return merged + left[i:] + right[j:]

sorted_notebooks = merge_sort(notebooks , compare_likes)

for _ in sorted_notebooks:
    print(_.username , _.likes)