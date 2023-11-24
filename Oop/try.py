class person:
    def read(self):
        self.name=input("enter the person name:")
        self.weight=input("enter the weight:")
        self.height=input("enter the height:")
        self.gender=input("enter the gender:")
    
        #display class variables
        print("name is",self.name)
        print("weight is",self.weight)
        print("the height is",self.height)
        print("the gender is",self.gender)

P1=person()
P1.read() 
            