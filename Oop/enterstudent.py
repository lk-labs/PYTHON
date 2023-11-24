class student:
    def __init__(self,name,regno,course,dept):
        self.name=name
        self.regno=regno
        self.course=course
        self.dept=dept
    def view(self):
        print(f"name:{self.name} regno:{self.regno} course:{self.course} dept:{self.dept}")
name=input("enter the name\n")
regno=input("enter the regno\n")
course=input("enter the course\n")
dept=input("enter the dept\n")
s1=student(name,regno,course,dept)
print("print the attributes of s1")
s1.view()

name=input("enter the name\n")
regno=input("enter the regno\n")
course=input("enter the course\n")
dept=input("enter the dept\n")
s2=student(name,regno,course,dept)
print("print the attributes of s2")
s2.view()
