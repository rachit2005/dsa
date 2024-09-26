# Lesson 1 - Binary Search, Linked Lists and Complexity

#read this please-->  https://jovian.ai/learn/data-structures-and-algorithms-in-python/lesson/lesson-1-binary-search-linked-lists-and-complexity

cards = [13,11,10,7,4,3,1,0]
query = 7
output = 3

# right now we are doing linear search 
def locate_card(cards , query):
    # creating a variable position
    position = 0 

    print('cards:' , cards)
    print('query:' , query)

    # # now we are looping through the list 
    # while True:

    #     print("position: " , position)
    #     if cards[position] == query:
    #         print(f"The number at given position is {cards[position]}")
    #         return position
            

    #     # increamenting the position 
    #     position +=1

    #     # if we are looped through the list then there is no solution
    #     if position == len(cards):
    #         print("no solution found")
    #         return -1
            

    while position < len(cards):
        if cards[position] == query:
            return position
        
        position +=1
    return -1

# result = locate_card(cards , query)
# print(result)
# print(result == output)

test = {
    'input' : {
        'cards': [13,11,10,7,4,3,1,0] , 
        'query' : 7
    },
    'output' : 3
}

# print(locate_card(test['input']['cards'] , test['input']['query']) == test['output']) 
# it is same as 
# print(locate_card(**test['input']) == test['output'])

# from jovian.pythondsa import evaluate_test_case
# result = evaluate_test_case(locate_card , test)
# print(result)




# NOW WE ARE TESSTING THE DIFFERENT CONDITIONS 

tests = []

# query occurs in the middle
tests.append(test)

tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
})

# query is the first element
tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})

# query is the last element
tests.append({
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})

# cards contains just one element, query
tests.append({
    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0 
})

# cards does not contain query 
tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})

# cards is empty
tests.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})

# numbers can repeat in cards
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})

# query occurs multiple times
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})

from jovian.pythondsa import evaluate_test_cases
# print(evaluate_test_cases(locate_card , tests))

# now we have to minimise the no of times we are accessing the element in the list, It can be done by using binary search algorithm
# now we are doing binary search

# managing repeated value list 
def test_location(cards , query , mid):
    mid_number = cards[mid]

    if mid_number == query:
        if mid-1>=0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number > query:
        return 'right'
    else:
        return'left'

def locate_cards_binary_search(cards , query):
    lo , hi = 0, len(cards) - 1
    while lo <= hi:
        mid = (lo+hi)//2
        result = test_location(cards,query,mid)

        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid-1
        elif result == 'right':
            lo = mid+1
        else:
            print("some thing happened ")

# if we are not finding any result
    return -1
        

# print(evaluate_test_cases(locate_cards_binary_search , tests))



# analyze the complexity of the algorithm
# the generic binary search 

def binary_search(lo , hi , condition):
    while lo <=hi:
        mid = (lo+hi)//2
        result = condition(mid)

        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == "right":
            lo = mid+1
        else:
            print("kuch to hua haiiii, clap clap!!")
    return -1


def locate_card_finally(cards , query):

    def condition(mid):
        if cards[mid] == query:
            if mid-1>0 and cards[mid-1] == query:
                return 'left'
            else:
                return 'found'
        elif cards[mid] > query:
            return 'right'
        elif cards[mid] < query:
            return 'left'
        else:
            print("pata nhi")

    return binary_search(0,len(cards) - 1 , condition)

# print(evaluate_test_cases(locate_card_finally , tests))

# next question
def first_postion(nums , target):

    def condition(mid):
        if nums[mid] == target:
            if mid-1>0 and nums[mid-1] !=target:
                return 'found'
            else:
                return 'left'

        elif nums[mid] > target:
            return 'left'
        else:
            return 'right'

    return binary_search(0 , len(nums)-1 , condition)

def last_position(nums , target):
    lo , hi = 0,len(nums)-1

    def condition(mid):
        if nums[mid] == target:
            if mid< hi and nums[mid+1] !=target:
                return 'found'
            else:
                return 'right'
        elif nums[mid] > target:
            return 'left'
        else:
            return 'right'
        
    return binary_search(lo,hi , condition)

def first_and_last_postion(nums , target):
    return first_postion(nums,target) , last_position(nums , target)

