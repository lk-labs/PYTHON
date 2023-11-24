def employee_salary(basic_salary,ohours):
    if ohours > 0 and ohours <=50:
        opay=(ohours*300)
    elif ohours >50:
        opay=(ohours*300)+(ohours-50)*350

    grosspay=basic_salary+opay
    print("the grosspay is",grosspay)
    if grosspay >50000:
        paye=0.14
    elif grosspay >=40000 and grosspay <50000:
        paye=0.12
    elif grosspay >=35000 and grosspay <40000:
        paye=0.11
    elif grosspay >=25000 and grosspay <35000:
        paye=0.08
    elif grosspay >=16000 and grosspay <25000:
        paye=0.05
    elif grosspay >=9500 and grosspay < 16000:
        paye=0.03
    elif grosspay <9500:
        paye=0

    NSSF=80
    NHIF=200
    SC=100   
    netpay=grosspay-(paye+NSSF+NHIF+SC)
    print("the net pay is",netpay)

basic_salary=int(input("enter your basic salary:"))
ohours=int(input("enter the overtime hours"))    

employee_salary(basic_salary,ohours)
