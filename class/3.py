"""
student details
"""

class Student:
    def __init__(self,name,regno):
        self.name=name
        self.regno=regno
    def viewStudent(self):
        print("Name :" , self.name,"Registration number :" ,self.regno)
s=Student("Brian",1045858)
s.viewStudent()