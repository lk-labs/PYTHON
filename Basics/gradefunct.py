def grading(cat,exam):
    total_exam=cat+exam
    comment=""
    print("the total exam is",total_exam)
    if total_exam > 50:
        print("pass")
    else:
        print("fail")   
grading(30,50)    