#define function
def schedular():
    lec_name=""
    unit=""
    lec_hall=input("enter the lecturer hall:")
    time=input("enter the time:")
    day=input("enter the day: ")
    if lec_hall=="TH" and time=="8.00-11.00" and day=="Monday":
        lec_name="mr kioko"
        unit="oop1"
        flag=1
    elif lec_hall=="OH"  and time=="11.00-2.00" and day=="Tuesday":
        lec_name="chris nandasaba"
        unit="database"
        flag=1
    elif lec_hall=="RH" and time =="2.00-5.00" and day=="friday":
        lec_name="lanoi"
        unit="accounting"
        flag=1
    else:
        flag=0
        print("hall is free at that time")
    if flag ==1:
        print("the lecture name ",lec_name)  
        print("the unit is",unit) 
schedular()        























              