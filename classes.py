import datetime as dt
class Expense:
    def __init__(self, exp_name: str = "", amount: float = 0.0, category: str = ""):
        self.name = exp_name
        self.amount = float
        self.category = ""
#class to store user
class User: 
    def __init__(self, user = "", pwd = ""):
        self.username = user
        self.password = pwd
        self.expenses = list
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
