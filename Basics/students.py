class student:
    def __init__(self):
        self.name=input("enter the name of the student:")
        self.reg=int(input("enter theregistration number:"))
        self.course=input("enter the course :")
        self.department=input("enter the department:")
    def view(self):
        print(f"name:{self.name}")
        print(f"reg:{self.reg}")
        print(f"course:{self.course}")
        print(f"department:{self.department}")
s=student()
print("properties of obect 1")
s.view()  
s1=student() 
print("properties of student 2")
s1.view()         