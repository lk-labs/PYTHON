class A:
    def __init__(self):
        print("constructor of base class")
class B(A):
    def __init__(self):
     A.__init__(self)
     super() .__init__()
     print("constructor of derived class")
b=B()        