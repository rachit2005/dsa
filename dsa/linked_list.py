# linked list is a collection of nodes(object that contains dataand its address)

class Node:
    def __init__(self , data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        # creating an empty linked list 
        self.head = None
        self.no_of_nodes = 0

    def __len__(self):
        return self.no_of_nodes
    
    def insert_head(self , value):
        'inserting the node in LinkedList'
        new_node = Node(value)
        new_node.next = self.head #establishing the connection

        self.head = new_node
        self.no_of_nodes +=1

    def append_in_ll(self , value):
        'adding node at the end'
        new_node = Node(value)
        self.no_of_nodes +=1

        if self.head == None:
            self.head = new_node
            return
            
        curr = self.head

        while curr.next != None:
            curr = curr.next

        curr.next = new_node

    def __str__(self):
        'printing/traversing the nodes'
        current = self.head

        result = ''
        while current != None:
            result += '[' + str(current.data) + ']' + "-->"
            current = current.next
        
        return result[:-3]

    def insert_at_pos(self , after_index , value):
        'insert the value after the "after_index" item in the linked list'
        new_node = Node(value) #node to be added after the 'after' value

        if self.head == None:
            self.head = new_node
            return 'it was an empty list so node has been added in the first'
        else:
            curr = self.head
            while curr != None: #looping through the ll
                if curr.data == after_index:
                    break
                curr = curr.next

            if curr != None:
                new_node.next = curr.next
                curr.next = new_node
                self.no_of_nodes +=1
            else:
                return 'nothing'

    def clear(self):
        'clear the ll'
        self.head = None
        self.no_of_nodes = 0

    def del_head(self):
        'removes the head of the linked list and return it'
        if self.head == None:
            print("Empty linked list")
            return

        removed = self.head
        self.head = self.head.next
        self.no_of_nodes -=1

        return removed
    
    def del_tail(self):
        'removes the tail of the linked list and return it'
        Curr = self.head
        if self.head == None:
            print('Empty linked list')
            return

        elif Curr.next == None:
            removed = self.del_head()
            return removed
            
        else:
            while Curr.next.next != None:
                Curr = Curr.next

            self.no_of_nodes -=1
            removed = Curr.next
            Curr.next = None
            return removed
        
    def remove(self , value_to_remove):
        "remove the value from the linked list and returns it"
        removed = 0
        if self.head == None:
            raise IndexError('empty list')
        if self.head.data == value_to_remove:
            removed = self.del_head()

        curr = self.head
        while curr.next != None:
            if curr.next.data == value_to_remove:
                break
            curr = curr.next
        if curr.next == None:
            raise ValueError("value not found")
        
        else:
            removed = curr.next
            curr.next = curr.next.next
        return removed
    
    def search(self , item):
        'returns the node and its position on the linked list'
        curr = self.head
        pos = 0

        while curr != None:
            if curr.data == item:
                return curr , pos
            pos+=1
            curr = curr.next

        raise ValueError("value not found")    

    def search_index(self , index):
        curr = self.head
        pos = 0

        while curr != None:
            if pos == index:
                return pos , curr
            pos +=1
            curr = curr.next

        raise IndexError("index out of linked list")
    

    def find_max(self):
        curr = self.head
        max = curr

        while curr != None:
            if curr.data >max.data :
                max = curr
            curr = curr.next
        
        return max
    
    def replace_max(self,value):
        n_max = self.find_max()
        n_max.data = value

        return n_max

    def reverse_linked_list(self):
        prev = None
        curr = self.head

        while curr != None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev

    def ll_to_string(self):
        curr = self.head
        result = ""

        while curr != None:
            if curr.data == '*' or curr.data == '/':
                curr.data = " "

            elif curr.data == "/.":
                curr.data = "."
                curr.next.data = curr.next.data.capitalize()

            result +=  str(curr.data)
            curr = curr.next
        
        return result

ll = LinkedList()
ll.append_in_ll("t")
ll.append_in_ll("h")
ll.append_in_ll("e")
ll.append_in_ll("/")
ll.append_in_ll("*")
ll.append_in_ll("/.")
ll.append_in_ll("full stop")
print(ll)
print(ll.ll_to_string())
print(ll)