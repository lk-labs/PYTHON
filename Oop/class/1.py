"""Example 1 of method definition
Let’s assume you wish to define a method which accepts
marks of a student then computes the grade of the grade of
the student. The method shall return the grade of the
student to the calling block
"""
def grade(marks):
    marks=int(input("Enter your marks :"))
    if 100<=marks>=70:
        print("A")
    elif 70>marks>=60:
            print("B")
    elif 60 > marks >= 50:
        print("C")
    elif 50 > marks >= 40:
        print("D")
    elif 39 > marks:
        print("F")
    else:
        print("INVALID")

grade(20)