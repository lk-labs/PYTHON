cat_mark=int(input("enter the cat mark out of 30:\n"))
main_exam=int(input("enter the main exam out of 70:\n"))
total_exam=cat_mark+main_exam


if 100>= total_exam >=70:
    grade="A"
elif 70> total_exam >=60:
    grade="B"
elif 60>  total_exam >=50:
    grade="C"
elif 50> total_exam >=40:
    grade="D"
elif 40> total_exam  >=0:
    grade="F"
else:
    grade="Z" 




print(f" total  {total_exam}  grade is :{grade}")             