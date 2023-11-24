def volume(radius,height):
    pi=3.14
    return pi*radius**2*height
radius=int(input("enter the radius of cylinder:"))
height=int(input("enter the height of a cylinder:"))
volume2=volume(radius,height)
print("the volume is",volume2)