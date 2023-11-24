
count=0
sum=0
avg=0
score=0

for score in range(1,11):
    score=int(input(f"enter the score for each subject{1:10}:"))
    sum+=score
    count=count+1
    print(score)
    print("the sum is",sum)

#calculate the average
avg=sum/count      
print("the average is",avg)
print("the sum is",sum)  