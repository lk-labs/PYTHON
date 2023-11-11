bpay=float(input("Enter the basic pay\n:"))
ohours=int(input("Enter the overtime hours worked\n:"))
if ohours >=1 and ohours <=50:
    opay=ohours * 300
if ohours > 50:
    opay=(50*300)+ ((ohours-50)*350 )   
gpay=bpay+opay


if gpay >=50000:
    paye=0.14*gpay
elif gpay>=40000 and gpay<50000:
    paye=0.12*gpay
elif gpay>=35000 and gpay<40000:
    paye=0.11*gpay
elif gpay>=25000 and gpay<35000:
    paye=0.08*gpay
elif gpay >=16000 and gpay<25000:
    paye=0.05*gpay
elif gpay >=9500 and gpay<16000:
    paye=0.03*gpay
else:
    paye=0                    
#define constants
NSSF=80.00
NHIF=320.00
SC=100.00

#calculate the net pay
npay=gpay-(NHIF+NSSF+SC+paye)
#display values in a tabular format
print("Gross pay paye Net pay\n")
print(gpay,paye,npay)
