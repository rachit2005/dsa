class Tree:
    def __init__(self , data) -> None:
        self.data = data 
        self.children = []
        # every child node is parent node of another child node so each element of children list will be the instance of tree node
        self.parent = None # this will stores the parent node

    def add_child(self , child):
        child.parent = self # this means that the child is the instance of class Tree and it will have parent property as self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent

        while p:
            p = p.parent
            level +=1

        return level

    # def print_my_method(self):
    #     print(self.data)
    #     for child in self.children:
    #         print()
    #         print(child.data , " --> " , end="")

    #         if len(child.children) > 0:
    #             child.print_my_method()
    #         else:
    #             for child2 in child.children:
    #                 print(child2.data , end=" , ")

    def print_tree(self):
        if self.get_level() ==0:
            spaces = ""
        else:
            spaces = "  "*(self.get_level()*3) +"|" + "___"

        print(spaces + self.data)

        if self.children:
            for child in self.children:
                child.print_tree()

def build_tree():
    root_node = Tree("Electronics") # we created electronics as a parent node
    
    laptop = Tree('laptop') # and laptop as another parent node
    laptop.add_child(Tree("hp"))
    laptop.add_child(Tree("asus"))
    laptop.add_child(Tree("macbook"))

    phones = Tree('phones')
    phones.add_child(Tree('apple'))
    phones.add_child(Tree('samsung'))
    phones.add_child(Tree('nokia'))

    tv = Tree('TV')
    tv.add_child(Tree('samsung'))
    tv.add_child(Tree('LG'))

    root_node.add_child(laptop) # adding the laptop node to child node list of electronics
    root_node.add_child(phones)
    root_node.add_child(tv)

    return root_node

if __name__ == "__main__":
    root = build_tree()
    root.print_tree()

    # print(root.get_level())
    pass
