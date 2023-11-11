sum=0
avg=0
subjects=1
count=1



for subjects in range(1,11):
    subjects=float(input(f"enter the marks for each subjects{subjects}:"))
    print(subjects)
    sum=sum+subjects
    count=count+1

#calculate the average
avg=sum/10
print("the sum of the subjects is ",sum) 
print("the average of the subjects is",avg)   
