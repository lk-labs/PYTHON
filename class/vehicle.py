def booking(time,destination,date):
    bus_found=False
    atime=""
    fare=0
    vregno=""

    if date=="11/12/2023" and time=="8.00" and destination=="voi":
        atime="11.00"
        fare=1000
        vregno="KBZ 00X"
        bus_found=True
    elif date=="12/12/2023" and time=="9.00" and destination=="Nairobi" :
        atime="12.00"
        fare=2000
        vregno="KBC 02Z"
        bus_found=True
    elif date=="13/12/2023" and time=="10.00" and destination=="MSA":
        atime="13.00"
        fare=3000
        vregno="KCZ 009Z"
        bus_found=True

    if bus_found ==True:
        print("wow !the bus has been found")
        print(f"the vregno is : {vregno}")
        print(f"the atime is: {atime}")
        print(f"the fare is:  {fare}")
    else:
        print("the bus has not found!")
date=input("enter the date of travel(DD/MM/YYYY):") 
time=input("enter the time of travel(HH/MM):")
destination=input("enter the destination:") 


booking(time,destination,date)    
             