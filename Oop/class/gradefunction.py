def grading(name,regno,unit,cat,exam):
    grade=""
    exam2=0
    cat2=0
    total_mark=cat+exam
    print("the total mark is",total_mark)

    while  total_mark <0 or total_mark >100:
        print("sorry ,re-enter marks again:")
            
        cat2=int(input("enter cat again:"))
        exam2=int(input("enter the exam2:"))
        total_mark=cat2+exam2
                          
    if total_mark >=70 and total_mark <=100:
        grade="A"
    elif total_mark >=60 and total_mark <=69:
        grade="B" 
    elif total_mark >=50 and total_mark <=59:
        grade="C"
    elif total_mark >=40 and total_mark <=49:
        grade="D"
    elif total_mark >=0 and total_mark <39:
        grade="D"
    
    return grade

name=input("enter your name:")
regno=int(input("enter your regno:"))
unit=input("enter the unit:")
cat=int(input("enter the cat mark:")) 
exam=int(input("enter exam mark:"))
result=grading(name,regno,unit,cat,exam)


print("Name:", name)
print("Reg No:", regno)
print("Unit:", unit)
print("Cat Mark:", cat)
print("Exam Mark:", exam)
print("Grade:", result)

