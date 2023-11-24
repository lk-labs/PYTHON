def vehicle(destination,time,date):
    Vregno=""
    atime=""
    fare=0
    bus_found=False

    if time=="11.00"and destination=="Voi" and date=="11/12/2023":
        Vregno="KBz 009z"
        atime="12.00"
        fare=2000
        bus_found=True
    elif time=="8.00" and destination=="mombasa" and date=="12/12/2023":
        Vregno="Kaz 002c"
        atime="11.00"
        fare=2500
        bus_found=True
    elif time=="12.00" and destination=="Nairobi"  and date=="13/12.2023":
        Vregno="KBZ 009x"
        atime="4.00"
        fare=3000
        bus_found=True
    if bus_found==True:
        print("wow!the bus has been found")
        print("the vehucle reg no is",Vregno)
        print("the fare is",fare)
        print("the arrival time is",atime)  
    elif bus_found==False:
        print("the bus has not been found")



time=input("enter the departure time:")
destination=input("enter your destination:")
date=input("enter the date for travel:") 
vehicle(destination,time,date)

               


