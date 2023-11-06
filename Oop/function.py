def grading(RegNo, Name, Unit_name, cat_mark, main_exam, grade):
    exam_mark = cat_mark + main_exam

    if exam_mark >= 70 and exam_mark <= 100:
        grade = "A"
    elif exam_mark >= 60 and exam_mark <= 69:
        grade = "B"
    elif exam_mark >= 50 and exam_mark <= 59:
        grade = "C"
    elif exam_mark >= 40 and exam_mark <= 49:
        grade = "D"
    elif exam_mark >= 0 and exam_mark <= 39:
        grade = "F"
    else:
        grade = "Z"

    return grade

RegNo = input("Enter the registration number: ")
Name = input("Enter the name of the student: ")
Unit_name = input("Enter the unit name: ")
cat_mark = int(input("Enter the cat mark: "))
main_exam = int(input("Enter the main exam mark: "))
grade = ""

student_grade = grading(RegNo, Name, Unit_name, cat_mark, main_exam, grade)

print(f"\nRegistration Number: {RegNo}")
print(f"Name: {Name}")
print(f"Unit Name: {Unit_name}")
print(f"Exam Mark: {cat_mark + main_exam}")
print(f"Grade: {student_grade}")
