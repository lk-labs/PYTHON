def grading(cat,exam):
    total_exam=cat+exam
    print("the total exam is",total_exam)
    if total_exam > 50:
        print("pass")
    else:
        print("fail")
cat=int(input("enter the cat mark:"))
exam=int(input("enter the exam mark:"))
grading(cat,exam)
            