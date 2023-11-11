sum=0
avg=0
count=0

for x in range(0,101):
    if x % 2==0:
        print(x)
        count=count+1
        sum=sum+x
         
      
#average of numbers is
avg=sum/count
print("the sum of x is",sum)
print("the average of the numbers",avg)