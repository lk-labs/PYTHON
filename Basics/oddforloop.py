x=1
sum=0
avg=0
count=0

for t in range(0,101):
    if t%2==1:
        print(t)
        count=count+1
        sum=sum+t


avg=sum/count
print("the average is",avg)


