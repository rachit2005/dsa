class TreeNode():
    def __init__(self, key):
        self.key, self.left, self.right = key, None, None
    
    def height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.height(self.left), TreeNode.height(self.right))
    
    def size(self):
        if self is None:
            return 0
        return 1 + TreeNode.size(self.left) + TreeNode.size(self.right)

    def traverse_in_order(self):
        if self is None: 
            return []
        
        return (TreeNode.traverse_in_order(self.left) + [self.key] + TreeNode.traverse_in_order(self.right))
    
    def display_keys(self, space='\t', level=0):
        # If the node is empty
        if self is None:
            print(space*level + '∅')
            return   

        # If the node is a leaf 
        if self.left is None and self.right is None:
            print(space*level + str(self.key))
            return

        # If the node has children
        TreeNode.display_keys(self.right, space, level+1)
        print(space*level + str(self.key))
        TreeNode.display_keys(self.left,space, level+1)    
    
    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return TreeNode.to_tuple(self.left),  self.key, TreeNode.to_tuple(self.right)
    
    def __str__(self):
        return "BinaryTree <{}>".format(self.to_tuple())
    
    def __repr__(self):
        return "BinaryTree <{}>".format(self.to_tuple())
    
    @staticmethod    
    def parse_tuple(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        else:
            node = TreeNode(data)
        return node
    


# Binary Search Tree (BST)
# A binary search tree or BST is a binary tree that satisfies the following conditions:

#1)  The left subtree of any node only contains nodes with keys less than the node's key
#2)  The right subtree of any node only contains nodes with keys greater than the node's key

def remove_none(nums):
    return [x for x in nums if x is not None]

def is_bst(node):
    if node is None:
        return True, None, None
    
    is_bst_l, min_l, max_l = is_bst(node.left)
    is_bst_r, min_r, max_r = is_bst(node.right)
    
    is_bst_node = (is_bst_l and is_bst_r and 
              (max_l is None or node.key > max_l) and 
              (min_r is None or node.key < min_r))
    
    min_key = min(remove_none([min_l, node.key, min_r]))
    max_key = max(remove_none([max_l, node.key, max_r]))
    
    # print(node.key, min_key, max_key, is_bst_node)
        
    return is_bst_node, min_key, max_key

tree = TreeNode.parse_tuple((('aakash', 'biraj', 'hemanth')  , 'jadhesh', ('siddhant', 'sonaksh', 'vishal')))
# print(is_bst(tree))

class User():
    def __init__(self , username , password , email):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self) -> str:
        return "User(username='{}', password='{}', email='{}')".format(self.username, self.password, self.email)    
    def __str__(self) -> str:
        return self.__repr__()
    
aakash = User('aakash', 'Aakash@Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj@Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth@Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh@Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant@Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh@Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal@Goel', 'vishal@example.com')
rachit = User('rachit' , 'Rachit@2005' , 'rachitkamaal@gmail.com')


class BSTNode():
    def __init__(self , key , value = None) -> None:
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

# level 0
tree = BSTNode(jadhesh.password , jadhesh)

# level 1
tree.left = BSTNode(biraj.password , biraj)
tree.right = BSTNode(sonaksh.password , sonaksh)

# level 2
tree.left.left = BSTNode(aakash.password , aakash)
tree.left.right = BSTNode(hemanth.password , hemanth)
tree.right.left = BSTNode(siddhant.password , siddhant)
tree.right.right = BSTNode(vishal.password , vishal)

# print(TreeNode.display_keys(tree , level=2))

# inserting new node in the binary tree     
def insert(node , key , value):
    if node is None:
        node = BSTNode(key , value)
    elif key < node.key:
        node.left = insert(node.left , key , value)
        node.left.parent = node
    elif key > node.key:
        node.right = insert(node.right , key , value)
        node.right.parent = node

    return node


# finding node in the binary tree 
def find(node, key):
    if node is None:
        return None
    if key == node.key:
        return node
    if key < node.key:
        return find(node.left, key)
    if key > node.key:
        return find(node.right, key)

node_finded = find(tree , hemanth.password)
print(node_finded.value)


def update(node, key, value):
    target = find(node, key)
    if target is not None:
        target.value = value

update(tree , aakash.password , User('rachit' , 'rachit@2005' , 'rachitkamaal@gmail.com'))
print(find(tree , aakash.password).value)



def list_all(node):
    if node is None:
        return []
    return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)



def is_balanced(node):
    if node is None:
        return True, 0
    balanced_l, height_l = is_balanced(node.left)
    balanced_r, height_r = is_balanced(node.right)
    balanced = balanced_l and balanced_r and abs(height_l - height_r) <=1
    height = 1 + max(height_l, height_r)
    return balanced, height


def make_balanced_bst(data, lo=0, hi=None, parent=None):
    if hi is None:
        hi = len(data) - 1
    if lo > hi:
        return None
    
    mid = (lo + hi) // 2
    key, value = data[mid]

    root = BSTNode(key, value)
    root.parent = parent
    root.left = make_balanced_bst(data, lo, mid-1, root)
    root.right = make_balanced_bst(data, mid+1, hi, root)
    
    return root
    
def balance_bst(node):
    return make_balanced_bst(list_all(node))

users = [aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]

tree1 = None

for user in users:
    tree1 = insert(tree1, user.username, user)

tree2 = balance_bst(tree1)
print(TreeNode.display_keys(tree1 , level=3))
print(TreeNode.display_keys(tree2 , level=3))

class TreeMap():
    def __init__(self):
        # this is node itself
        self.root = None
        
    def __setitem__(self, key, value):
        # we are inserting and updating in the same function 
        node = find(self.root, key)
        if not node:
            self.root = insert(self.root, key, value)
            self.root = balance_bst(self.root)
        else:
            update(self.root, key, value)
            
        
    def __getitem__(self, key):
        node = find(self.root, key)
        return node.value if node else None
    
    def __iter__(self):
        return (x for x in list_all(self.root))
    
    def __len__(self):
        return TreeNode.size(self.root)
    
    def display(self):
        return TreeNode.display_keys(self.root)
