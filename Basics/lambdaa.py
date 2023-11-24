def passenger_details():
    departure_time=input("enter the departure time:")
    destination=input("enter your destination:")
    departure_day=input("ennter the departure day")
passenger_details()

def train_timetable(departure_time,destination,departure_day):
    atime=""
    fare=0
    train_number=""
    train_found=False


    if departure_time=="8.00" and destination=="Nairobi" and departure_day=="Monday":
        atime="11.00"
        fare=2000
        train_number="KBZ 009x"
        train_found=True
    elif departure_time=="10.00" and destination=="Thika" and departure_day=="Tuesday":
        atime="12.00"
        fare=3500
        train_number="KCZ 99x"
        train_found=True
    if train_found==True:
        print("the train reg no is",train_number)
        print("the fare is",fare)
        print("the arrival time is",atime) 
    elif train_found==False:
        print("sorry,the train not found") 
    train_timetable(departure_time,destination,departure_day)              

