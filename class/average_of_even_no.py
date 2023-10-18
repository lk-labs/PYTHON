def average(sum,even):
    for j in  range(0,101,2):
        if j%2==0:
            sum+=j
            even+=1
        j=j+1

    else:
        print(sum/even)

average(0,0)