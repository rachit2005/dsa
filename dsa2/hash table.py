# dictionary uses hash table to store data 
stock_prices = {}

with open('stock_prices.csv') as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_prices[day] = price

# print(stock_prices)
# print(stock_prices['march 9'])

def get_hash1(key):
    h = 0
    for char in key:
        h +=ord(char)
    
    return h%100

# print(get_hash1('march'))


class HashTable:
    def __init__(self) -> None:
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self , key):
        h = 0
        for char in key:
            h += ord(char)
        
        return h % self.MAX
    
    def __setitem__(self , key , value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self , key):
        h = self.get_hash(key)
        print(self.arr[h])

    def __len__(self):
        count = 0
        for item in self.arr:
            if item is not None:
                count +=1
        print(count)
        return count
    
    def __delitem__(self , key):
        h = self.get_hash(key)
        self.arr[h] = None
                

table = HashTable()
# print(table.arr)

# table.add('march 9' , 'hello world')
table['march 9'] = '9'
table['march 1'] = '1'
table['march 2'] = '2'
table['march 3'] = '3'
table['march 94'] = '94'
# print(table.get_hash('march 9'))
table['march 9']
len(table)

