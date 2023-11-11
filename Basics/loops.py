sum=0
count=0
avg=0
for x in range(0,101):
    if x %2==0:
        print(x)
        sum=sum+x
        count=count+1
avg=sum/count
print("sum =\n",sum)
print("average=\n",avg)        
