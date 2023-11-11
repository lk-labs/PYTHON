def grading_marks(marks):

    grade=""
    while marks <0 or marks >100:
        print("sorry ,there is an error enter correct marks")
        re_enter_marks=int(input("enter your marks again"))
        marks=re_enter_marks
    else:    
        if marks >=70 and marks <=100:
            grade="A"
        elif marks >=60 and marks <=69:
            grade="B"
        elif marks >=50 and marks <=59:
            grade="C"
        elif marks >=40 and marks <=49:
            grade="D"
        elif marks >0 and marks <=39:
            grade="F"
        print("your grade is",grade)
marks=int(input("enter the marks:"))
grading_marks(marks)        

                    
