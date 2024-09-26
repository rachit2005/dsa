# data structure is a builiding blocks for any software.

'''Big O notation ''' # is used to measure how running time or space reuqirements for your program grow as input size grows

# time = order of n --> O(n)

# example --> 
def getsquared(numbers):
    squared_numbers = []
    for n in numbers:
        squared_numbers.append(n**2)
    
    return squared_numbers

numbers = [1,2,3,4,5,6,7,8,9]
# print(getsquared(numbers=numbers))

def duplicate_numbers(numbers):

    for i in range(len(numbers)):
        for j in range(i+1 , len(numbers)):
            if numbers[j] == numbers[i]:
                print(f"{numbers[j]} is duplicate")
                break

dup_num = [1,2,3,4,4,5,6,7,8,9]
duplicate_numbers(dup_num)

