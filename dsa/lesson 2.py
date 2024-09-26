# Lesson 2 - Binary Search Trees, Traversals and Recursion

# read this --> https://jovian.ai/learn/data-structures-and-algorithms-in-python/lesson/lesson-2-binary-search-trees-traversals-and-balancing

class User():
    def __init__(self , username , password , email):
        self.username = username
        self.email = email
        self.password = password

        print("User Created")

    def __repr__(self) -> str:
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.password, self.email)    
    def __str__(self) -> str:
        return self.__repr__()


# this is linear seraching and operations
class UserDatabase:
    def __init__(self):
        self.users = []

    # adding user in alphabetical order
    def insert(self, user):
        i = 0
        while i < len(self.users):
            if user.username < self.users[i].username:
                break
            i+=1
        self.users.insert(i , user)
    
    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user
        else:
            print("no user exist with this username")
    
    def update(self, username,new_name , new_password , new_email):
        target = self.find(username)
        target.username , target.password , target.email = new_name, new_password , new_email
        print(f"user has been updated -->from {username} to {target.username}")

    def remove(self,username):
        self.users.remove(self.find(username))
        
    def list_all(self):
        return self.users


aakash = User('aakash', 'Aakash@Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj@Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth@Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh@Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant@Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh@Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal@Goel', 'vishal@example.com')

database = UserDatabase()
database.insert(aakash)
database.insert(biraj)
database.insert(hemanth)
database.insert(sonaksh)
database.insert(vishal)

user_find = database.find('aakash')
print(user_find)

updating = database.update('vishal' ,'rachit', 'rachit@2005', "rachitkamaal@gmail.com")
print(database.find('rachit'))



# We can limit the number of iterations required for common operations like 
# find, insert and update by organizing our data in the following structure, called a binary tree search:


