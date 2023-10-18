class staff:
 def details(self):
   self.staffname=str(input("Name :"))
   self.regno=int(input("Reg no :"))
   self.department=str(input("Departmenr :"))
  
 def viewStaff(self):
    print("Staff name :", self.staffname, "Staff number :", self.regno, "Staff department :", self.department)
s=staff()
s.details()
s1=staff()
s1.details()
s.viewStaff()
s1.viewStaff()


