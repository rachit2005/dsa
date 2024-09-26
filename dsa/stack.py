# stack --> last in first out , eg: stack of plates

class Node:
    def __init__(self , value) -> None:
        self.data = value
        self.next = None

class Stack:

  def __init__(self):
    self.top = None

  def push(self, value):

    new_node = Node(value)
    new_node.next = self.top
    self.top = new_node

  def pop(self):

    if self.top is None:
      return "Stack Empty"
    else:
      data = self.top.data
      self.top = self.top.next
      return data

  def is_empty(self):
    return self.top == None

  def peek(self):

    if self.top is None:
      return "Stack Empty"
    else:
      return self.top.data

  def traverse(self):
    temp = self.top

    while temp != None:
      print(temp.data,end=' ')
      temp = temp.next

  def size(self):

    temp = self.top
    counter = 0

    while temp is not None:
      temp = temp.next
      counter+=1

    return counter

def reverse_string(text):
    temp = Stack()
    result = ""
    for i in text:
        temp.push(i)
        
    while not temp.is_empty():
        result = result + temp.pop() 

    return result


def text_editor(text , pattern):
    'in pattern u removes the word from the end and r adds that word at the end'
    u = Stack()
    r = Stack()

    res = ""
    for i in text:
       u.push(i)

    for i in pattern:
       if i == 'u':
          data = u.pop()
          r.push(data)
       elif i == 'r':
          data = r.pop()
          u.push(data)
       else:
          print("not valid")

    while not u.is_empty():
       res = u.pop() + res

    return res

l = [[0,0,1,1] ,
     [0,0,1,0] ,
     [0,0,0,0] ,
     [0,0,1,0]]

def celebrity(sq_matrix):
    s = Stack()
    for i in range(len(sq_matrix)):
       s.push(i)
    #  s = [3,2,1,0]
        
    while s.size() >=2:
       i = s.pop() #stores 3 , 1
       j = s.pop() #stores 2 , 0

       if sq_matrix[i][j] == 0:
        #   j is not a celebrity but i is a celebrity
          s.push(i)

       else:
        #   j is celebrity but i is not a celebrity
          s.push(j) 

    celeb = s.pop() #we getting the celebrity to cross check 
    for i in range(len(sq_matrix)):
       if i != celeb:
          if sq_matrix[i][celeb] == 0 or sq_matrix[celeb][i] == 1:
            print("no one is a celebrity")
            return
          
    print(f'the celebrity is {celeb}') 
             

celebrity(l)

stack_1 = Stack()
stack_1.push('rastogi')
stack_1.push('rachit')
stack_1.push('billionair')

# stack_1.traverse()
# print(stack_1.__length__())
# stack_1.peek()
# print('after')
# curr = stack_1.pop()
# stack_1.traverse()
# # print(curr.value)
# print(stack_1.__length__())
# print(reverse_string("hello"))
# print(text_editor('rachit' , 'uurru'))