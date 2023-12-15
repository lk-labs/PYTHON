x=1
sum=0
count=1
avg=0
for x in range(1,101):
    if x%2==0:
        print(x)
    sum=sum+x
    count=count+1
avg=sum/count
print("the sum is",sum)
print("the average is",avg)    



    