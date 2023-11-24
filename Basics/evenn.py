x=0
count=0
sum=0
avg=0
while x <=100:
    if x%2==0:
        print(x)
        sum=sum+x
        count=count+1
    x=x+1
avg=sum/count
print("the sum is",sum)
print("the average is",avg)        