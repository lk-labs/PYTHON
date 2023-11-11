def area_circle(radius):
    import math
    area=math.pi *radius**2
    return area
radius=int(input("Enter the radius of a circle:"))
area_circle2=area_circle(radius)
print("the area of a circle is ",area_circle2)