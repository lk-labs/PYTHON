def mwende_grade(marks):
    grade=""
    comment=""

    while marks <0 or marks >100:
        print("sorry re_enter the marks again")
        re_marks=int(input("re_enter the marks again:"))
        marks=re_marks
        
    if marks >=70 and marks <=100:
        grade="A"
        comment="excellent"
    elif   marks >=60 and marks <=69:
        grade="B"
        comment="good" 
    elif marks >=50 and marks <=59:
        grade="C"
        comment="fair"
    elif marks>=40 and marks <=49:
        grade="D"
        comment="pass"
    else:
        grade="F"
        comment="fail"  
    print("grade is",grade)
    print("comment",comment)

                   
regno=int(input("enter the registration number:"))
name=input("enter the name:")
unitcode=input("enter the unitcode:")
marks=int(input("enter the marks:")) 
mwende_grade(marks)       