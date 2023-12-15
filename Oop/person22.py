class person:
    def capture_information(self):
        self.name=input("enter the name:")
        self.weight=int(input("enter the weight:"))
        self.height=int(input("enter the height:"))
        self.gender=input("enter the gender:")
    def write(self):
        print("name",self.name)
        print("weight",self.weight)
        print("height",self.height)
        print("gender",self.gender)
p=person()
p.capture_information()
p.write()            