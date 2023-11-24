def passenger_details():
    departure_time = input("Enter the departure time: ")
    destination = input("Enter your destination: ")
    departure_day = input("Enter the departure day: ")
    return departure_time, destination, departure_day

def train_timetable(departure_time, destination, departure_day):
    atime = ""
    fare = 0
    train_number = ""
    train_found = False

    if departure_time == "8.00" and destination == "Nairobi" and departure_day == "Monday":
        atime = "11.00"
        fare = 2000
        train_number = "KBZ 009x"
        train_found = True
    elif departure_time == "10.00" and destination == "Thika" and departure_day == "Tuesday":
        atime = "12.00"
        fare = 3500
        train_number = "KCZ 99x"
        train_found = True

    if train_found:
        print("The train reg no is", train_number)
        print("The fare is", fare)
        print("The arrival time is", atime)
    else:
        print("Sorry, the train was not found")

departure_time,destination,departure_day=passenger_details()
train_timetable(departure_time,destination,departure_day)
