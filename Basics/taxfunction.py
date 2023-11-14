def tax(basic_salary,o_hours):
    

    if o_hours >0 and o_hours <=50:
        opay=o_hours*300
    elif o_hours > 50:
        opay=(o_hours*300)+((o_hours-50)*350)
    gross_pay=basic_salary+opay 
    print(f"the grosspay is:{gross_pay}")

    if gross_pay >50000:
        paye=0.14*gross_pay
    elif gross_pay >=40000 and gross_pay <50000:
        paye=0.12*gross_pay
    elif gross_pay >=35000 and gross_pay <40000:
        paye=0.11*gross_pay
    elif gross_pay >=25000 and gross_pay <35000:
        paye=0.08*gross_pay
    elif gross_pay >=16000 and gross_pay <25000:
        paye=0.05*gross_pay
    elif gross_pay >=9500 and gross_pay <16000:
        paye=0.03*gross_pay
    elif gross_pay <9500:
        paye=0
    #define constants
    NSSF=80.00
    NHIF=200.00
    Sc=100.00
    net_pay=gross_pay-(paye+(NSSF+NHIF+Sc)) 
    print(f"the net pay is : {net_pay}") 
basic_salary=float(input("enter the basic salary:"))
o_hours=int(input("enter the overtime hours"))
tax(basic_salary,o_hours)      


