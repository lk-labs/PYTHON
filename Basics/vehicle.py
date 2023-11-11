time=input("enter time for travel\n:")
destination=input("Enter the destination for  travel\n:")

if time=="10.00" and destination=="voi":
    vregNo="KDZ 201"
    atime="5.00 pm"
    fare=2000.00
elif time=="2.00" and destination=="kisumu":
    vregNo="KAT 221v"
    atime="11.00 pm"
    fare=5000.00
    flag=1
else:
    flag=0
#determine the value of flag
if flag==1:
    print("Bus found!\n")
    print(vregNo,atime,fare)
if flag==0:
    print("sorry no bus match the two criteria\n:")               

  