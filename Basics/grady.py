def hiring(jobgrade):
    basic_salary=0
    house_allowance=0
    travellling_allowance=0
    gross_salary=basic_salary+house_allowance+travellling_allowance


    if jobgrade=="H":
        basic_salary=12000
        house_allowance=2000
        travellling_allowance=3000
        gross_salary=basic_salary+house_allowance+travellling_allowance
        print("the basic salary is",basic_salary)
        print("the house allowanc is",house_allowance)
        print("the travelling allowance is",travellling_allowance)
        print("the gross salary is",gross_salary)

    elif jobgrade=="M":
        basic_salary=18000
        house_allowance=0
        travellling_allowance=0
        gross_salary=basic_salary+house_allowance+travellling_allowance
        print("the basic salary is",basic_salary)
        print("the house allowanc is",house_allowance)
        print("the travelling allowance is",travellling_allowance)
        print("the gross salary is",gross_salary)

    elif jobgrade=="S":
        basic_salary=60000
        house_allowance=40000
        travellling_allowance=12,000
        gross_salary=basic_salary+house_allowance+travellling_allowance
        print("the basic salary is",basic_salary)
        print("the house allowanc is",house_allowance)
        print("the travelling allowance is",travellling_allowance)
        print("the gross salary is",gross_salary)

name=input("enter the employee name:")
gender=input("enter your gender:")
jobgrade=input("enter the jobgrade:")
hiring(jobgrade)
