def train_timetable():
    trainNO=input("enter the number of the train:")
    Dtime=input("enter the departure time:")
    fare=int(input("enter the fare:"))
    destination=input("enter your destination:")
    Atime=input("enter the arrival time:")
    Dday=input("the day of departure :")
    return trainNO,Dtime,fare,destination,Atime,Dday


def search_train(Dtime,destination,Dday):
    trainNO=""
    Atime=""
    fare=0
    flag=0
    if Dtime=="11.05" and destination=="Nairobi" and Dday=="monday":
        trainNO="kbz 123x"
        Atime="13.00"
        fare=2000                       
        flag=1
    elif Dtime=="12.00" and destination=="mombasa" and Dday=="tuesday":
        trainNO="kaz 432x"
        Atime="14.00"
        fare=3000
        flag=1
    elif Dtime=="8.00" and destination=="thika"  and Dday=="wednesday":
        trainNO="kcz 235 v"
        Atime="11.00"
        fare=3500  
        flag=1
    if flag ==1:
        print("wow!the bus has been found") 
        print(f"train number:{trainNO}")
        print(f"fare:{fare}")
        print(f"arrival time :{Atime}")  
    else:
        print("no mtching criteria!")       

trainNO,Dtime,fare,destination,Atime,Dday=train_timetable()
search_train(Dtime,destination,Dday)    