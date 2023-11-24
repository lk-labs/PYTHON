class student:

    def write(self):
        self.name=input("enter your name:")
        self.age=int(input("enter your age:"))


    def view(self):
        print("your name is",self.name)
        print("your age is",self.age) 

print("object 1\n")
q=student()
q1=student()

print("object 1\n")
q.write()
q.view()
print("object 2\n")
q1.write()
q1.view()