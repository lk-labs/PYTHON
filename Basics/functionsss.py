def grading(cat,exam):
    total=cat+exam
    print("the total mark is",total)
    if total > 50:
        print("above average")
    else:
        print("below average")    
grading(30,40)    