No_of_hours=int(input("enter the no of hours\n:"))
#defining a constant
Hourly_rate=850.00
basic_salary=No_of_hours*Hourly_rate
#defining a constant
Lallowance=200.00
Gpay=basic_salary+Lallowance
if Gpay >=0 and Gpay <2000:
    paye=0
elif Gpay >=2000 and Gpay <3000:
    paye=0.05*Gpay
elif Gpay >=3000 and Gpay  <4000:
    paye=0.07*Gpay
elif Gpay >=4000 and Gpay  <5000:
    paye=0.09*Gpay
elif Gpay >=5000:
    paye=0.11*Gpay
#calculating the net pay
net_pay=Gpay-paye

print(f"the basic salary is :  the gross pay is  :   the net pay is :{basic_salary}  {Gpay}   {net_pay}")