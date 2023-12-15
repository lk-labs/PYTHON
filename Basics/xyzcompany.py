def tax_function(jobgrade):
    basicsalary=0
    houseallowance=0
    travellingallowance=0
    flag=0
    if jobgrade=="H":
        basicsalary=12,000
        houseallowance=2000
        travellingallowance=3000
        flag=1
    elif jobgrade=="M":
        basicsalary=18000
        houseallowance=0
        travellingallowance=0
        flag=1
    elif jobgrade=="S":
        basicsalary=60000
        houseallowance=40000
        travellingallowance=12000
        flag=1
    if flag==1:
        print("basic salary",basicsalary)
        print("housellowance",houseallowance)
        print("travelling allowance",travellingallowance)
    else:
        print("no matching jobgrade")
jobgrade=input("enter the job grade:")        
tax_function(jobgrade)        

