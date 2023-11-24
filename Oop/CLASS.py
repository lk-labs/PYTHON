class student:
    def write(self):
        self.name=input("enter your name:")
        self.regno=int(input("enter the regno :"))


    def read(self):
        print("the name is",self.name)
        print("the regno is",self.regno) 


s=student()
s1=student()

print("object 1\n")
s.write()
s.read()

print("object 2\n")
s1.write()
s1.read()