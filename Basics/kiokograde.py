def grade_comment(marks):
    grade=""
    comment=""
    while marks <0 or marks >100:
        print("sorry,enter the correct marks")
        re_marks=int(input("enter the marks again"))
        marks=re_marks

    if marks >=70 and marks <100:
        grade="A"
        comment="excellent"  
    elif marks >=60 and marks <=69:
        grade="B"
        comment="Good" 
    elif marks >=50 and marks <=59:
        grade="C"
        comment="Fair" 
    elif marks >=40 and marks <=49:
        grade="D"
        comment="Pass" 
    elif marks >=0 and marks <=39:
        grade="F"
        comment="Fail" 
    print(f"your grade is:{grade}  your comment is :{comment}")

    


regno=int(input("enter the registration number:"))
name=input("enter your name:")
gender=input("enter your gender:")
unit_name=input("enter the unit name:") 
marks=int(input("enter your marks:")) 

grade_comment(marks)