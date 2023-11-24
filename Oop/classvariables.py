

class sample:
    count=5
    x=0
    def read(self):
        self.a=int(input("enter value of a:"))

    def display(self):
        print("value of a",self.a)    
    
s1=sample()
s2=sample()
print("properties for s1\n")
print("values of count",+s1.count)
s1.read()
print("values of count",+s1.count)

s1.display()
print("properties for s2\n")

s2.read()
print("values of count",+s2.count)
s2.display()




