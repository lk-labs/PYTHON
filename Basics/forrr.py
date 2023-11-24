x=1
sum=0
avg=0
count=0

for x in range(1,101):
    if x%2==0:
        print(x)
        count=count+1
        sum=sum+x
#calculate the average 
avg=sum/count
print("the average is",avg)        