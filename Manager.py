import Employee
class Manager:
    def __init__(self,managerName):
        self.managerName=managerName
    def manages(self):
        self.manages=Employee.Employee.work(self)
manager = Manager("Sai")
emp = Employee.Employee("Ravi")
print(f"{manager.managerName} manages {manager.manages()} done by {emp.empName}")
