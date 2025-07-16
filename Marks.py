class Marks:
    def __init__(self,studentName,studentClass):
        self.studentName=studentName
        self.studentClass=studentClass
        self.__mathMarks=0
    def getMathMarks(self):
        return self.__mathMarks
    def setMathMarks(self,marks):
        self.__mathMarks=marks
s1=Marks("Sai",9)
s1.setMathMarks(90)
print(f"Marks of {s1.studentName} in math is {s1.getMathMarks()}.")
