class Account:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.__balance=0
    def getBalance(self):
        return self.__balance
    def setBalance(self,balance):
        self.__balance+=balance
a1=Account("John",22)
print(a1.getBalance())
a1.setBalance(100)
print(a1.getBalance())