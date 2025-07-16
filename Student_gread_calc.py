import grade_calc
import validate_marks
'''Enter student name: John
Enter marks separated by space: 80 90 70 85 78

Student: John
Marks: [80, 90, 70, 85, 78]
Average: 80.60
Grade: A'''
name=input("Enter student name: ")
while True:
    marks = list(map(int, input("Enter marks separated by space: ").split()))
    if validate_marks.validate(marks):
        avg = grade_calc.avg(marks)
        grade=grade_calc.grade(avg)
        print("Student: ",name)
        print("Marks: ",marks)
        print("Average: ", avg)
        print("Grade: ", grade)
        break
    else:
        print("Invalid marks, please enter the marks again.")


