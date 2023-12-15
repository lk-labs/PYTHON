x=0
sum=0
count=0
avg=0
while x<=100:
    if x%2!=0:
        print(x)
    sum=sum+x
    count+=1
    x+=1
avg=sum/count
print("sum",sum)
print("average",avg)        