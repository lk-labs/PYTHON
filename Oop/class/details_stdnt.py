class Student:
 def __init__(self, name, regno):
    self.name = name
    self.regno = regno
 def viewStudent(self):
    print("Name : ", self.name, " Regno: ", self.regno)
s=Student("joel",100)
s.viewStudent()
s1=Student("Mary",101)
s1.viewStudent()
