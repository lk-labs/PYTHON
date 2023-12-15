def tax_function(Bsalary,ohours):
    if ohours >=0 and ohours <=5:
        opay=(ohours * 500)
    elif ohours >5:
        opay=(ohours*650)
grosspay=Bsalary+opay            