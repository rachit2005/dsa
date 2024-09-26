class HashTable:
    def __init__(self) -> None:
        self.max = 10
        # so instead of None we use an array (chaining method)
        self.arr = [[] for i in range(10)]

    def get_hash(self , key):
        hash = 0
        for char in key:
            hash += ord(char)

        return hash%self.max
    
    def __getitem__(self,key):
        "prints and return value of that key"
        h = self.get_hash(key)
        val = None
        for ele in self.arr[h]:
            if ele[0] == key:
                print(ele[1])
                return ele[1]                

    def __setitem__(self , key , data):
        h = self.get_hash(key)
        found = False
        # chaining the data in that hash table cell 
        for idx , element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key , data)
                found = True
                break
        if not found:
            self.arr[h].append((key,data)) 
    
    def __delitem__(self , key):
        h = self.get_hash(key)
        for index , ele in enumerate(self.arr[h]):
            if ele[0] == key:
                del self.arr[h][index]
                print('deletion sucessfull !!')
    
    def print(self):
        print('Printing the hash table')
        for key in self.arr:
            if len(key) > 0:
                print(key)
            
            

table = HashTable()

table['march 9'] = '9'
table['march 1'] = '1'
table['march 2'] = '2'
table['march 3'] = '3'
table['march 94'] = '94'

# now lets do collisions

table['march 6'] = '120'
# table['march 6']
table['march 17'] = '456'

table['march 6']
print('next')
table['march 17']
table.print()

del table['march 17']
table.print()

# print(table.arr)