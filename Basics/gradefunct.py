def grading(cat,exam):
    return cat+exam  
cat=int(input("enter the cat mark"))
exam=int(input("enter the exam mark:"))  
total_exam=cat+exam
print("the total_exam",total_exam)
if total_exam >=50:
    print("passed")
else:
    print("failed")     