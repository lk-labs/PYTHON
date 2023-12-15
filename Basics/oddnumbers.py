x=1
sum=0
avg=0
count=0
for x in range(1,101):
    if x%2!=0:
        print(x)
        sum=sum+x
        print("the sum is",sum)
        count=count+1
    x=x+1 
avg=sum/count
print("the average is",avg)       