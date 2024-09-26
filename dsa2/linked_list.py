class Node:
    def __init__(self , data:None , next:None) -> None:
        self.data = data 
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def insert_at_begining(self , data):
        node = Node(data , self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print('linked list is empty')
            return
        
        itr = self.head
        llstr = ''
        while itr:
            llstr += '['+str(itr.data)+']' + '-->'
            itr = itr.next
        
        print(llstr)

    def insert_at_end(self , data):
        if self.head is None:
            self.head = Node(data , None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data , None)

    def insert_values(self , datalist):
        self.head = None

        for item in datalist:
            self.insert_at_end(item)

    def len(self):
        "print and returns the length of linked list"

        length = 0
        itr = self.head
        while itr:
            length+=1
            itr = itr.next
        return length
    
    def remove_at(self , index):
        if index < 0 or index > self.len():
            raise Exception('ERROR: index is out of length') 
        
        if index == 0:
            # changing the courrent head to its next node head
            self.head == self.head.next
            return
        
        count = 0
        itr = self.head
        value = None
        while itr:
            if count == index-1:
                value = itr.next.data
                itr.next = itr.next.next
                break
            itr = itr.next
            count+=1

        print(f'removed {value}')
        return value
    
    def insert_at(self , index , data):
        if index < 0 or index > self.len() :
            raise Exception('out of index buddy')
        
        if index ==0:
            self.insert_at_begining(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data , itr.next)
                itr.next = node
                break

            itr = itr.next
            count +=1

    def insert_after_value(self , data_after , data_to_insert):
        if self.head is None:
            return
        
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert , self.head.next)
            return
        
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert , itr.next)
                break
            itr = itr.next

    def remove_value(self , data):
        if self.head is None:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next


if __name__ == "__main__":
    ll = LinkedList()
    # ll.insert_at_begining('start')
    # ll.insert_at_begining('middle')
    # ll.insert_at_begining('end')

    # ll.insert_at_end('insereting at the end')

    # ll.print()
    # length = ll.len() # --> 4
    # print(length)

    # print('creating a new linked list')

    ll.insert_values(['rachit' , 'rastogi' , 'is' , 'very' , 'handsome'])
    ll.print()
    # length2 = ll.len() # --> 5
    # print(length2)

    # ll.remove_at(3)
    # ll.print()
    # leng = ll.len()

    ll.insert_at(3 , 'inserted at 3rd index')
    ll.print()

    ll.insert_after_value('rachit' , 'great')
    ll.print()

    ll.remove_value('great')
    ll.print()