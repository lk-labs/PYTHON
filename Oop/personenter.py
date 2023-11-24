class person:
    def __init__(self,name,course,department):
        self.name=name
        self.course=course
        self.department=department
    def view(self):
        print(f"name:{self.name} course:{self.course} department:{self.department}") 
name=input("enter your name:")
course=input("enter course:")
department=input("enter your department:")

p1=person(name,course,department)
print("attributes of p1\n")
p1.view()
print("attributes of p2\n")
name2=input("enter your name:")
course2=input("enter course:")
department2=input("enter your department:")
p2=person(name2,course2,department2)

p2.view()