def area(radius):
    pi=3.14
    area=pi*radius**2
    return area

radius=int(input("enter the radius:"))
result=area(radius)
print("the area of a circle",result)   