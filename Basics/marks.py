marks=float(input("enter your marks"))
if marks >=70 :
    grade="A"
elif marks>=60 :
    grade="B"
elif marks >=50 :
    grade="C"
elif marks >=40 :
    grade="D" 
elif marks<=39:
     grade="F"
else :
    grade="Z"
print(f"the grade is:{grade}")   


