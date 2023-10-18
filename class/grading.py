marks = int(input('\n Enter your marks :')) # use this input to make your submission
if  100 >= marks >= 90:
    print('A+')
elif 90 > marks >=80:
    print('A')
elif 80 > marks >=70:
    print('B')
elif 70 > marks >=60:
    print('C')
elif 60 > marks >=50:
    print('D')
elif 50 > marks >=40:
    print('E')
elif 40 > marks:
    print('F')
else:
    print('You entered invalid digits')