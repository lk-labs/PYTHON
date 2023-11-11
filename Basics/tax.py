Bpay=float(input("Enter the basic salary for each month\n:"))
Ehours=int(input("Enter the extra hours worked\n:"))
if Ehours >=1 and Ehours <=50:
    opay=Ehours *300
elif Ehours >50:
    opay=(Ehours *300)+(Ehours-50)*350

#calculating the Gpay
Gpay=Bpay+opay

if Gpay > 50000:
    paye=0.14*Gpay
elif Gpay >=40000 and Gpay <=49999:
    paye=0.12*Gpay
elif Gpay >=35000 and Gpay <=39999:
    paye=0.11*Gpay
elif Gpay >=25000 and Gpay <=34999:
    paye=0.08*Gpay  
elif Gpay >=16000 and Gpay <=24999:
    paye=0.05*Gpay
elif Gpay >=9500 and Gpay <=15999:
    paye=0.03*Gpay
else:
    paye=0

#defining the constants
NSSF=80.00
NHIF=200.00
Sc=100.00
#calculating the net pay
netpay=Gpay-(paye+(NSSF+NHIF+Sc))

print(f"the gross pay is :the paye is: the net pay is:{Gpay}  {paye}  {netpay}")
