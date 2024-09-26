from collections import deque

stack = deque() # last in first out(add element at back and removes that element from front first)
# adding element at the back
stack.append('rachit')
stack.append('rastogi')
stack.append('rajput')
stack.append('something')

# print(stack)

# removing from the front
stack.pop()
# print(stack)


queue = deque() # first in first out (add elements from front and removes element from front)
# adding element from front 
queue.appendleft('rachit')
queue.appendleft('am')
queue.appendleft('I')
# print(queue)

# removing from the back 
queue.pop()
# print(queue)



# double ended queue 

double_ended_queue = deque([1,1,2,3,5,8,13,21])

#adding and removing from left
l = ['left' , 'left2']
double_ended_queue.extendleft(l)
# print(double_ended_queue)

double_ended_queue.popleft()
# print(double_ended_queue)

# adding and removing from right
r = ['right' , 'right2']
double_ended_queue.extend(r)
# print(double_ended_queue)

double_ended_queue.pop()
# print(double_ended_queue)



'''Genva Confection'''
# in mountain random number is stored and branch will be an helping hand to dump those random numbers into the lake in particular order

t = int(input('how many times: '))

for _ in range(t):
    mountain = []
    n = int(input('how many element: '))
    for j in range(n):
        mountain.append(int(input('add element: ')))

    print(f'mountain : {mountain}')

    branch = []

    lake = []
    nex = 1
    while nex < n+1:
        if mountain and mountain[-1] == nex:
            lake.append(mountain.pop())
            nex +=1
        elif branch and branch[-1] == nex:
            lake.append(branch.pop())
            nex +=1
        else:
            if mountain: branch.append(mountain.pop())
            else: break

    print(f'branch : {branch}')
    print(f'lake : {lake}')


    if nex == n+1:
        print('y')
    else:
        print('n')


'''Sets'''
sets = set({1,1,2,3,5,4,4,3,3}) # removes the repeating element and arranges it in acen order
# print(sets)

# creating a set
example = {'rachit1' , 'apples'}

example.add('rachit')
example.add('rastogi')
example.add('25')
example.add(25)
# print(example)

example.discard('rachit1')
# print(example)

example.add('sets')
for i in example:
    # print(i)
    pass


'''arrays'''
array = [[elem for elem in range(7)] for _ in range(4)]
print(array)

# we can acces element by array[0-3][0-6]
