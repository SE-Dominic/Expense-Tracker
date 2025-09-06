import queue
class User: 
    def __init__(self, user = "", pwd = ""):
        self.username = user
        self.password = pwd
    def __str__(self):
        return f"Username: {self.username}\nPassword: {self.password}\n"
    #getter functions
    def getUser(self):
        return self.username
    def getPassword(self):
        return self.password
    #setters
    def setUser(self, name):
        self.username = name
    def setPassword(self, pwd):
        self.password = pwd

class DB:
    def __init__(self):
        self.db = []
    def insertVal(self, val: User):
        self.db.append(val)
    def removeVal(self, val: str): #remove by username
        for user in self.db:
            if user.getUser()== val:
                self.db.remove(user)
        #user not found
        return f"User {val} was not found in database."
    def find(self, val: str):
        left = 0
        right = len(self)
        #simple binary search to keep things quick and effictive O(log(n))
        while (left < right):
            mid = (left + right) // 2
            if self.db[mid].getUser() == val:
                return self.db[mid]
            elif self.db[mid].getUser() < val:
                left = mid + 1
            else:
                right = mid
        return None
