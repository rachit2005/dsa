class BinarySearchTreeNode:
    def __init__(self , data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def add_child(self , data):
        # i need to check the value first
        if data == self.data:
            print('already data is in tree' , self.data)
            return
        if data > self.data:
            # if data is bigger than the parent node then it will be added in the right node otherwise in left node 
            if self.right:
                self.right.add_child(data)
            else:
                # tree is a recursive data structure 
                self.right = BinarySearchTreeNode(data)
        else:
            if self.left:
                # if we have some data in left node then we will use the recursion 
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)



    def in_order_traversal(self): # --> we append list as: (left  , node , right)
        elements = []

        # visit the left branch first
        if self.left:
            # this the recursive method to adding list for each time there is a left node and will continue recursion till self.left is None
            elements += self.left.in_order_traversal() # adding the list again and again
        # then visit the base node 
        elements.append(self.data)


        # then visit the right node 
        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    def preorder(self): # --> (N,L,R)
        elements = [self.data]

        if self.left:
            elements += self.left.preorder()
        if self.right:
            elements += self.right.preorder()

        return elements
    
    def post_order(self): # --> (L,R,N)
        elements = []

        if self.left:
            elements += self.left.post_order()

        if self.right:
            elements += self.right.post_order()

        elements.append(self.data)

        return elements


    
    def search(self , val):
        if self.data == val:
            return True
        
        if val > self.data:
            # value might be in right branches 
            if self.right:
                # we will use recursion 
                return self.right.search(val)
            else:
                return False
        
        if val < self.data:
            # value might be in the left branches
            if self.left:
                return self.left.search(val)
            else:
                return False

    def find_max(self):
        if self.right is None: # when right node is None then it means that we have reached the right most val which is the highest val in whole tree
            return self.data
        return self.right.find_max()
    
    def find_min(self):
        if self.left is None: # when left node is None then it means that we have reached the left most val which is the lowest val in whole tree
            return self.data
        return self.left.find_min()
    
    def delete(self , val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)

        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
            
        else:
            if self.left is None and self.right is None:
                return None
            
            if self.left is None:
                return self.right
            
            if self.right is None:
                return self.left
            
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self

    
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == "__main__":
    l = [7,12,14,15,20,23,27,88 , 7,7,7,88]
    l.sort(reverse=True)
    # print(f'sorted list --> {l}')
    tree = build_tree(l)
    print(tree.in_order_traversal())
    # print(tree.search(7))
    # print(tree.search(99))
    # print(tree.find_min())
    # print(tree.find_max())
    # tree = tree.delete(20)
    print(tree.preorder())
    print(tree.post_order())
    # print(tree.in_order_traversal())
