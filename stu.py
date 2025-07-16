class Student:
    # this method sets the name(property) of the student(object)
    def setName(self,name):
        self.__name=name
    # this returns the name(property) of the student(object)
    def getName(self):
        return self.__name
    # this method sets the marks(property) of the student(object), if the marks are valid, then it sets the marks(property) else it shows an error message.
    def setMarks(self,marks):
        if marks<=100 and marks>=0:
            self.__marks=marks
        else:
            print("Error: Marks should be between 0 and 100.")
    # this method returns th marks of student(object)
    def getMarks(self):
        return self.__marks
#initilizing th student object
s=Student()
sn = input("Student Name:")
s.setName(sn)
# this while loop is used to take user marks as input, it loops until the user enters valid marks(0-100 inclusive) and then set the marks property of the studdent object
while True:
    sm=int(input("Student Marks:"))
    s.setMarks(sm)
    if sm<=100 and sm>=0:
        break

