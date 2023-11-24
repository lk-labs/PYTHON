def volume_cylinder( radius,height):
    pi=3.14
    volume=pi*radius*radius*height
    return volume
radius=int(input("enter the radius:"))
height=int(input("enter the height:"))
volume_cylinder2=volume_cylinder(radius,height)
print("the volume of a cylinder",volume_cylinder2)
