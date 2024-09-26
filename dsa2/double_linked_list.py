class Node:
    def __init__(self , data:None , next:None , prev:None) -> None:
        self.data = data
        self.next = next
        self.prev = prev

class Doubly_linked_list:
    def __init__(self) -> None:
        self.head = None

    def print_forward(self):
        if self.head is None:
            print("Linked list is empty !!!")
            return
        
        itr = self.head
        llstr = ''
        while itr:
            llstr += '[' + str(itr.data) + '] -->'
            itr = itr.next

        print(llstr)

    def print_backward(self):
        if self.head is None:
            print('Linked List is empty !!!')
            return
        
        last_node = self.get_lastNode()
        itr = last_node
        llstr = ''
        while itr:
            llstr += '[' + str(itr.data) + '] -->'
            itr = itr.prev

        print('Linked list in reverse order: ')
        print(llstr)
        
    def get_lastNode(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr
    
    def len(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count+=1

        return count
    
    def insert_at_begining(self , data):
        if self.head is None:
            self.head = Node(data , self.head , None)
        else:
            node = Node(data , self.head , None)
            self.head.prev = node
            self.head = node    
 
    def insert_at_end(self , data):
        if self.head is None:
            self.head = Node(data , None , None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data , None , itr)
    
    def insert_values(self , DataList):
        self.head = None

        for item in DataList:
            self.insert_at_end(item)


if __name__ == "__main__":
    dll = Doubly_linked_list() # initialising

    dll.insert_values(['rachit' , 'rastogi' , 'is' , 'great', 'boi'])
    dll.print_forward()
    dll.print_backward()

    