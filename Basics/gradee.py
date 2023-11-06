from tabulate import tabulate

student_no = input("Enter the student number: ")
name = input("Enter the student name: ")
unit_code = input("Enter the unit code: ")
unit_name = input("Enter the unit name: ")
cat_mark = int(input("Enter the CAT mark: "))
exam_mark = int(input("Enter the exam mark: "))

total_exam = cat_mark + exam_mark

if total_exam >= 70 and total_exam <= 100:
    grade = "A"
elif total_exam >= 60 and total_exam <= 69:
    grade = "B"
elif total_exam >= 56 and total_exam <= 59:
    grade = "C"
elif total_exam >= 50 and total_exam <= 55:
    grade = "D"
elif total_exam < 50:
    grade = "F"
else:
    grade = "Invalid choice"

data = [
    ["Student Number", student_no],
    ["Student Name", name],
    ["Unit Code", unit_code],
    ["Unit Name", unit_name],
    ["CAT Mark", cat_mark],
    ["Exam Mark", exam_mark],
    ["Total Exam Mark", total_exam],
    ["Grade", grade],
]

table = tabulate(data, headers=["Field", "Value"], tablefmt="pretty")

print(table)
