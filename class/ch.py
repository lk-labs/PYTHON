def grading(name, regno, unit, cat, exam):
    grade = ""
    exam2 = 0
    cat2 = 0
    total_mark = cat + exam
    print("The total mark is", total_mark)

    while total_mark < 0 or total_mark > 100:
        print("Sorry, re-enter marks again:")
        cat2 = int(input("Enter cat again:"))
        exam2 = int(input("Enter the exam mark:"))
        total_mark = cat2 + exam2

    if total_mark >= 70 and total_mark <= 100:
        grade = "A"
    elif total_mark >= 60 and total_mark <= 69:
        grade = "B"
    elif total_mark >= 50 and total_mark <= 59:
        grade = "C"
    elif total_mark >= 40 and total_mark <= 49:
        grade = "D"
    elif total_mark >= 0 and total_mark < 40:
        grade = "F"
    else:
        grade = "Invalid choice"

    return grade

name = input("Enter your name:")
regno = int(input("Enter your regno:"))
unit = input("Enter the unit:")
cat = int(input("Enter the cat mark:"))
exam = int(input("Enter exam mark:"))
result = grading(name, regno, unit, cat, exam)

print("\nName:", name)
print("Reg No:", regno)
print("Unit:", unit)
print("Cat Mark:", cat)
print("Exam Mark:", exam)
print("Grade:", result)
