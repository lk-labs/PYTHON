
def booking_timetable(time, destination, date):
    bous_found = False
    vRegno = ""
    fare = 0
    atime = ""

    if time == "11.00" and date == "11/02/2023" and destination == "voi":
        atime = "15.00"
        fare = 2000
        vRegno = "KBZ 009X"
        bous_found = True
    elif time == "8.00" and date == "11/03/2023" and destination == "mombasa":
        atime = "13.00"
        fare = 5000
        bous_found = True
    elif time == "11.30" and date == "11/05/2023" and destination == "Nairobi":
        atime = "16.00"
        fare = 1000
        bous_found = True
    
    if bous_found:
        return (vRegno, fare, atime)
    else:
        return None

time = input("Enter the departure time: ")
destination = input("Enter your destination: ")
date = input("Enter the date of travel in format (DD/MM/YY): ")

result = booking_timetable(time, destination, date)

if result:
    vRegno, fare, atime = result
    print("Wow, the bus has been found!")
    print("The vehicle registration number is:", vRegno)
    print("The fare is:", fare)
    print("The arrival time is:", atime)
else:
    print("Sorry, the bus has not been found.")