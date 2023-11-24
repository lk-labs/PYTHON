def booking(time, destination, date):
    bus_found = False
    atime = ""
    fare = 0
    vregno = ""

    if date == "11/12/2023" and time == "8.00" and destination == "voi":
        atime = "11.00"
        fare = 1000
        vregno = "KBZ 00X"
        bus_found = True
    elif date == "12/12/2023" and time == "9.00" and destination == "Nairobi":
        atime = "12.00"
        fare = 2000
        vregno = "KBC 02Z"
        bus_found = True
    elif date == "13/12/2023" and time == "10.00" and destination == "MSA":
        atime = "13.00"
        fare = 3000
        vregno = "KCZ 009Z"
        bus_found = True

    if bus_found:
        print("Wow! The bus has been found.")
        print(f"The vehicle number is: {vregno}")
        print(f"The arrival time is: {atime}")
        print(f"The fare is: {fare}")
    else:
        print("The bus has not been found.")

date = input("Enter the date of travel (DD/MM/YYYY): ")
time = input("Enter the time of travel (HH.MM): ")
destination = input("Enter the destination: ")

booking(time, destination, date)
