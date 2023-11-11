sum=0
avg=0
count=0
i=100

while i >= 0:
    if i % 2 ==1:
        print(i)
        count=count+1
        sum=sum+i
    i=i-1
#the average
avg=sum/count
print("the sum is",sum)  
print("the average is ",avg)     