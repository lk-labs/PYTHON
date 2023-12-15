class students:
    def Capture_registration(self):
        self.regno=int(input("enter your regno:"))
class results(students):
    def  mark(self):
        self.English_mark=int(input("enter your english mark:"))
        self.math_mark=int(input("enter your math_mark:"))
    def total_mark(self):
        return self.English_mark+self.math_mark
    def view(self):
        print(f"regno:{self.regno} english_mark={self.English_mark} math_mark:{self.math_mark} total_mark:{self.total_mark}")    
