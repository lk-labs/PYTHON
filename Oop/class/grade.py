def grading(marks):
    marks = int(input('Enter your marks :\n'))
    grade=""
    if marks >= 70 and marks <= 100:
       grade = "A"
    if marks >= 60 and marks < 70:
       grade = "A"
    if marks >= 50 and marks < 60:
       grade = "c"
    if marks >= 40 and marks < 50:
           grade = "D"
    if marks >= 0 and marks < 40:
       grade = "F"

    return grade

print(grading(marks=20))