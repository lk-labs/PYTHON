def capture_information():
    lechall=input("enter the lecture hall:")
    unit_name=input("enter the unit name:")
    lecname=input("enter the lec name:")
    timeslot=input("enter the time slot:")
    day=input("enter the day")
    return lechall,unit_name,lecname,timeslot,day
def search_hall(lechall,timeslot,day):
    unitname=""
    lecname=""
    flag=0
    if lechall=="TH lab A" and timeslot=="11.00-2.00" and day=="tuesday":
        unitname="database system"
        lecname="joe"
        flag=1
    elif lechall=="TH lab A" and timeslot=="2.00-5.00" and day=="wednesday":
        unitname="operating system" 
        lecname="phil"
        flag=1
    elif lechall=="TH lab B" and timeslot=="11.00-2.00" and day=="friday":
        unitname="logic programming"
        lecname="christiana"
        flag=1
    if flag==1:
        print("the lechall is free")
        print(f"unitname:{unitname}")
        print(f"lecname:{lecname}")
    else:
        print("resource not free")

lechall,unit_name,lecname,timeslot,day=capture_information()
search_hall(lechall,timeslot,day)


