stack = []

# it is "Last In First Out"

# in --> 
stack.append('1')
stack.append('2')
stack.append('3')
stack.append('4') # this is the last in so it will go out first
print(stack)

# to remove the last element --> it will acts as a stack
stack.pop()
print(stack)

# to remove the first element --> it will acts as a queue
stack.pop(0)
print(stack)

'''**********************************************************************************************************************************'''

from collections import deque
stack = deque()

# to see all the methods --> https://www.geeksforgeeks.org/deque-in-python/ 
print(dir(stack))
