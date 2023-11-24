"""fruits=("mangoe","pawpaw","orange","apple","watermelon")
fruits_2=list(fruits)
fruits_2.insert(0,"sweetpotatoe")
fruits=tuple(fruits_2)
print(fruits)
print(fruits[0:2])
print(fruits[-1:])
fruits=tuple(fruits_2)
print(fruits)"""


#unpacking tuples

cars=("benz","volvo","mazda","v8")
(green,yellow,blue,purple)=cars
print(green)
print(blue)
print(yellow)
print(purple)


if "benz"  in cars:
    print("yes it is present")
else:
    print("No")    

for car in cars:
    print(cars)    
