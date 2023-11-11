sum=0
avg=0
count=0
n=100
while n>=0 :
    if n%2==1:
        print(n)
        sum=sum+n
        count=count+1 
    n=n-1
avg=sum/count
print("sum=",sum)
print("average=",avg)        
