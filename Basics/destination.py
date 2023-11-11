time=(input("enter your destinatrion time:"))
destination=input("enter your destination :")
busfound=False

if time=="11.00" and destination=="voi":
    atime="14.00pm"
    RegNo="KBZ 009z"
    fare=2000
    busfound=True
elif time=="9.00" and destination=="kisumu":
    atime="13.00pm"
    RegNo="KAZ 002x"
    fare=5000
    busfound=True
elif time=="8.00"   and destination=="mombasa":
    atime="13.50pm" 
    RegNo="KCB 001x"
    fare=4500
    busfound=True
if busfound==True:   
    print("wow ,the bus found ")
    print("the vehicle reg number is:",RegNo)
    print("the arrival time is:",atime)
    print("the fare is:",fare)
else:
    print("bus not found!")            

