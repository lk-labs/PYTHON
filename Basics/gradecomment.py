Regno=input("Enter the registaration number:")
Name=input("Enter your name:")
Gender=input("Enter your gender:")
Unit_name=input("Enter the unit name:")
Unit_code=input("Enter the unit code:")
marks=int(input("Enter marks :"))
grade=""
comment=""
while marks < -1 or marks > 100:
    print("there was an error!put marks between 0 and 100")
    Re_enter_marks=int(input("enter the marks again:"))
    marks=Re_enter_marks
    
else:        
    if marks >=70 and marks <=100:
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
        comment="pass"
    elif marks >=0 and marks <=39:
        grade="F"
        comment="Fail"  
print(f"your grade is: {grade}: the  comment is:  {comment}")            