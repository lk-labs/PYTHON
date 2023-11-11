def circle_area(radius):
    pi=3.14
    area=pi*radius**2
    return area
radius=int(input("enter the radius of a circle:"))
circle_area_2=circle_area(radius)
print("the area of a circle is ",circle_area_2)