def grading(cat,exam):
    totalexam=cat+exam
    print("the total exam is",totalexam)
    if totalexam >=50:
        print("passed")
    else:
        print("fail")    
cat=int(input("enter the cat mark:"))
exam=int(input('enter the exam mark'))   
