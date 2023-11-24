def wages(no_of_hours):

    hourly_rate=850.00     
    basic_salary=no_of_hours*hourly_rate
    print("the basic salary is",basic_salary) 
    #define constants
    l_allowance=200.00

    grosspay=basic_salary+l_allowance
    print("the grosspay is",grosspay) 

    if grosspay >=0 and grosspay <2000:
        tax=0
    elif grosspay >=2000 and grosspay <3000:
        tax=0.05*grosspay
    elif grosspay >=3000 and grosspay <4000:
        tax=0.07*grosspay
    elif grosspay >=4000 and grosspay <5000:
        tax=0.09*grosspay
    elif grosspay >=5000:
        tax=0.11*grosspay
    net_pay=grosspay-tax
    print("the net pay is",net_pay) 

no_of_hours=int(input("enter the number of hours:"))

wages(no_of_hours)

