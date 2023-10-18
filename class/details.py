class person:
 def __init__(self):
     self.name=input("Enter the person name\n")
class staff(person):
 def __init__(self):
     self.staffid=input("Enter staff ID\n")
     super().__init__()
 def printStaff(self):
     print("Your name is\t"+ self.name+ "and staffId\t" +self.staffid)
s=staff()
s.printStaff()