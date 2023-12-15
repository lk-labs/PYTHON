def employee_pay(basicsalary,ohours):
    if ohours >=0 and ohours <=5:
        opay=(ohours*500)
    elif ohours >5:
        opay=(ohours*650)
    grosspay=basicsalary+opay
    print(f"the grosspay is:{grosspay}")   

    if grosspay >100000 :
        paye=0.3*grosspay
    elif grosspay >30000 and grosspay <=100000: 
        paye=0.25*grosspay
    elif grosspay <=30000:
        paye=0.15*grosspay
    netpay=grosspay-paye
    print(f"the netpay is:{netpay}") 
basicsalary=int(input("enter your basic salry:"))
ohours=int(input("enter the overtime hours:"))                  
employee_pay(basicsalary,ohours) 
        