class student:
    def __init__(self,name,regno,course,dept):
        self.name=name
        self.regno=regno
        self.course=course
        self.dept=dept
    def display(self):
        print(f"name:{self.name} regno:{self.regno} course:{self.course} dept:{self.dept}")
s1=student("mercy","289464","science","law")
s2=student("jenny","547383","theology","christian")
print("propertries of s1\n")
s1.display()
print("properties of s2\n")
s2.display()
