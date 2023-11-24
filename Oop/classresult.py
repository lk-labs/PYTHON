class student:
    def __init__(self,regno):
        self.regno=regno
 
class results(student):
    def __init__(self, regno,english_mark,math_mark):
        super().__init__(regno)
        self.english_mark=english_mark
        self.math_mark=math_mark
        self.total_mark=self.results()
        
    
    def results(self):
        return self.english_mark+self.math_mark
        
student1=results("1045121",50,60)
student2=results("1045858",80,70)


print("the properties for student 1\n") 
print(f"the registration number is:{student1.regno}")
print(f"the english mark:{student1.english_mark}")
print(f"the math mark:{student1.math_mark}")
print(f"total mark is:{student1.total_mark}")

print("the properties for student 2\n") 
print(f"the registration number is:{student2.regno}")
print(f"the english mark:{student2.english_mark}")
print(f"the math mark:{student2.math_mark}")
print(f"total mark is:{student2.total_mark}")







