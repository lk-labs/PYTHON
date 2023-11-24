sum=0
avg=0
count=0


for i in range(0,101):
    if(i%2!=0):
       print(i)
       sum=sum+i
       count=count+1


avg=sum/count
print("the sum is",sum)
print("the average is",avg)       