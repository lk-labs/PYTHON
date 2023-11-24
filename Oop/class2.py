class student:
    def __init__(self,name,age,regno,weight):
        self.name=name
        self.age=age
        self.regno=regno
        self.weight=weight
    def view(self):
        print(f"name:{self.name} age:{self.age} regno:{self.regno} weight:{self.weight}") 
student1=student("lucy","18","1045121","60")
student2=student("angellah","20","1043454","54")
print("properties of student 1\n")
student1.view()
print("properties of student 2\n")

student2.view()
