def tax_function(basicsalary,ohours):
    if ohours<=50:
        opay=300
    elif ohours>50:
        opay=(300)+((ohours-50)*350) 
    grosspay=basicsalary+opay
    print("the grosspay is",grosspay)
    if grosspay >=50000:
        paye=0.14*grosspay
    elif grosspay  >=40000 and grosspay <50000:
        paye=0.14*grosspay    
    elif grosspay>=35000 and grosspay<40000:
        paye=0.11*grosspay
    elif grosspay >=25000 and grosspay<35000:
        paye=0.08*grosspay
    elif grosspay>16000 and grosspay<25000:
        paye=0.05*grosspay
    elif grosspay>=9500 and grosspay <16000:
        paye=0.03*grosspay
    else:
        paye=0
    #define constants
    NHIF=200.00
    NSSF=80
    SC=100
    netpay=grosspay-(paye+(NSSF+NHIF+SC))
    print("the netpay is ",netpay) 
basicsalary=int(input("enter the basic salary:"))
ohours=int(input("enter the ohours:"))
tax_function(basicsalary,ohours)
