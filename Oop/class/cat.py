class house:
    def __int__(self,r):
        rprice=r
    def accept(self,hno,loc,name):
        self.huseno=hno
        self.location=loc
        self.hname=name
    def rentprice(self):
        self.rprice=input('Enter the rent price\n')
    def viewHouse(self):
        print(self.hname,self.location,self.houseno,self.rprice)

h=house()
h.accept(1001,'Karen','8020')
h.rentprice()
h.viewHouse()