class Employee:
    #Create class Employee with method work(). Inherit it in Manager and add method manage().
    def __init__(self,empName):
        self.empName = empName
    def work(self):
        self.work="Testing"